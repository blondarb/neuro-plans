#!/usr/bin/env python3
"""
Citation verification script for neuro-plans.

Extracts PMIDs from plan files and verifies them against the PubMed API.
Uses NCBI E-utilities (ESummary) for deterministic, 100% accurate lookups.
No external dependencies — uses only Python stdlib (urllib, json, xml).

Usage:
    python scripts/verify_citations.py docs/plans/migraine.md
    python scripts/verify_citations.py docs/plans/migraine.md --verify
    python scripts/verify_citations.py --all --verify
    python scripts/verify_citations.py --all --verify --fix
    python scripts/verify_citations.py --all --verify --json report.json
    python scripts/verify_citations.py --all --repair --json repair-report.json
    python scripts/verify_citations.py --all --repair --apply

Modes:
    (default)   Extract and list citations with PMIDs
    --verify    Look up each PMID via PubMed API and check for mismatches
    --fix       Auto-correct citation text to match PubMed metadata (implies --verify)
    --repair    Find correct PMIDs for mismatched citations via PubMed search (implies --verify)
    --apply     Apply found corrections to markdown files (implies --repair)
    --json FILE Write verification/repair results to JSON file
    --quiet     Suppress per-citation output, show only summary
"""

import argparse
import json
import re
import sys
import time
import unicodedata
import urllib.request
import urllib.error
from pathlib import Path


# ---------------------------------------------------------------------------
# PubMed API helpers (stdlib only — no requests dependency)
# ---------------------------------------------------------------------------

ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

# NCBI requires tool + email for polite access. Rate limit: 3 req/sec without key.
API_PARAMS = {
    "tool": "neuro-plans-citation-verifier",
    "email": "neuro-plans@example.com",
}

# Seconds between API calls (3 req/sec without API key; use 0.5 for safety margin)
RATE_LIMIT_DELAY = 0.5


def _api_get(url: str, params: dict) -> dict:
    """Make a GET request to NCBI E-utilities and return parsed JSON."""
    all_params = {**API_PARAMS, **params}
    query = "&".join(f"{k}={urllib.request.quote(str(v))}" for k, v in all_params.items())
    full_url = f"{url}?{query}"

    req = urllib.request.Request(full_url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"  API error: {e.code} {e.reason}", file=sys.stderr)
        return {}
    except urllib.error.URLError as e:
        print(f"  Network error: {e.reason}", file=sys.stderr)
        return {}
    except Exception as e:
        print(f"  Unexpected error: {e}", file=sys.stderr)
        return {}


def fetch_pmid_metadata(pmids: list[str]) -> dict:
    """
    Batch-fetch metadata for a list of PMIDs via ESummary.
    Returns dict keyed by PMID with title, authors, journal, year, doi.
    Handles up to 200 PMIDs per request.
    """
    results = {}
    batch_size = 200

    for i in range(0, len(pmids), batch_size):
        batch = pmids[i:i + batch_size]
        data = _api_get(ESUMMARY_URL, {
            "db": "pubmed",
            "id": ",".join(batch),
            "retmode": "json",
        })

        result_data = data.get("result", {})
        for pmid in batch:
            record = result_data.get(pmid, {})
            if "error" in record or not record:
                results[pmid] = {"exists": False}
            else:
                # Extract DOI
                doi = None
                for aid in record.get("articleids", []):
                    if aid.get("idtype") == "doi":
                        doi = aid.get("value")
                        break

                # Extract authors
                authors = [a.get("name", "") for a in record.get("authors", [])]

                results[pmid] = {
                    "exists": True,
                    "title": record.get("title", ""),
                    "authors": authors,
                    "first_author": authors[0] if authors else "",
                    "last_author": record.get("lastauthor", ""),
                    "journal": record.get("fulljournalname", ""),
                    "journal_abbrev": record.get("source", ""),
                    "year": record.get("pubdate", "")[:4],
                    "volume": record.get("volume", ""),
                    "issue": record.get("issue", ""),
                    "pages": record.get("pages", ""),
                    "doi": doi,
                }

        # Rate limit between batches
        if i + batch_size < len(pmids):
            time.sleep(RATE_LIMIT_DELAY)

    return results


def search_pubmed(author: str = "", journal: str = "", year: str = "",
                  title_words: str = "", max_results: int = 5) -> list[str]:
    """Search PubMed by author/journal/year/title. Returns list of PMIDs."""
    parts = []
    if author:
        parts.append(f"{author}[Author]")
    if journal:
        parts.append(f"{journal}[Journal]")
    if year:
        parts.append(f"{year}[Date - Publication]")
    if title_words:
        parts.append(f"{title_words}[Title]")

    if not parts:
        return []

    term = " AND ".join(parts)
    data = _api_get(ESEARCH_URL, {
        "db": "pubmed",
        "term": term,
        "retmax": str(max_results),
        "retmode": "json",
    })

    return data.get("esearchresult", {}).get("idlist", [])


# ---------------------------------------------------------------------------
# Citation extraction from markdown
# ---------------------------------------------------------------------------

def extract_citations(file_path: Path) -> list[dict]:
    """
    Extract all citations with PubMed links from a markdown file.
    Searches the entire file (not just Evidence section) for PubMed URLs.
    """
    content = file_path.read_text(encoding="utf-8")
    citations = []
    seen_pmids = set()

    # Pattern: [Citation text](https://pubmed.ncbi.nlm.nih.gov/12345678/)
    # Can appear in table cells or inline text
    pattern = r'\[([^\]]+)\]\(https?://pubmed\.ncbi\.nlm\.nih\.gov/(\d+)/?\)'

    for match in re.finditer(pattern, content):
        citation_text = match.group(1).strip()
        pmid = match.group(2)

        # Find the line number and surrounding context
        start = match.start()
        line_num = content[:start].count("\n") + 1

        # Try to extract the evidence claim from the table row
        line = content[content.rfind("\n", 0, start) + 1:content.find("\n", start)]
        evidence = ""
        if "|" in line:
            cells = [c.strip() for c in line.split("|")]
            # First non-empty cell is usually the evidence claim
            for cell in cells:
                if cell and cell != citation_text and "pubmed" not in cell.lower():
                    evidence = cell
                    break

        citations.append({
            "citation": citation_text,
            "pmid": pmid,
            "line": line_num,
            "evidence": evidence[:120] if evidence else "",
            "match_text": match.group(0),
        })

    return citations


def extract_unlinked_citations(file_path: Path) -> list[dict]:
    """Find citations in the Evidence section that don't have PubMed links."""
    content = file_path.read_text(encoding="utf-8")
    unlinked = []

    evidence_section = re.search(r'## 8\. EVIDENCE.*?(?=\n## |\Z)', content, re.DOTALL)
    if not evidence_section:
        return unlinked

    section = evidence_section.group(0)
    for line in section.split("\n"):
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 4:
            continue

        # Last substantive cell is usually the source
        source_cell = cells[-2] if cells[-1] == "" else cells[-1]

        # Skip header/separator rows
        if source_cell.startswith("---") or source_cell == "Source":
            continue

        # Check if this row has a PubMed link
        if "pubmed.ncbi.nlm.nih.gov" not in line and source_cell:
            # Has text but no PubMed link
            if len(source_cell) > 5 and not source_cell.startswith("---"):
                unlinked.append({
                    "source_text": source_cell,
                    "evidence": cells[1] if len(cells) > 2 else "",
                })

    return unlinked


# ---------------------------------------------------------------------------
# Citation comparison / matching
# ---------------------------------------------------------------------------

def _strip_diacritics(text: str) -> str:
    """Remove diacritics/accents for fuzzy matching (e.g., Wickström → Wickstrom)."""
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in nfkd if not unicodedata.combining(ch))


# Words/phrases that indicate a guideline, consensus, or trial citation.
# These are commonly cited by organization name rather than first author.
GUIDELINE_INDICATORS = [
    "guideline", "guidelines", "consensus", "practice parameter",
    "recommendation", "recommendations", "position statement",
    "advisory", "scientific statement", "white paper",
    "evidence assessment", "evidence-based", "standards of care",
    "expert opinion", "task force", "working group",
    # Organization acronyms
    "aha", "aha/asa", "aan", "aes", "ncs", "ilae", "ichd", "ean",
    "efns", "who", "nice", "sign", "acr", "aans", "cns",
    "ers", "aasm", "acns", "naemsp",
    "ahs", "ihs", "ens", "wfn", "abpn", "acep",
    # Trial names (commonly cited by trial name, not lead author)
    "trial", "study group", "investigators",
    "esett", "rampart", "preempt", "arise", "dawn", "defuse",
    "escape", "extend-ia", "mr clean", "revascat", "swift prime",
    "clots", "interact", "atach", "mistie", "clear",
    "isat", "brat", "coss", "sampris",
]


def compare_citation(citation_text: str, pubmed_meta: dict) -> dict:
    """
    Compare claimed citation text against actual PubMed metadata.
    Returns a result dict with match status and any issues found.

    Uses Unicode normalization for author matching and relaxed rules
    for guideline/consensus/trial citations.
    """
    if not pubmed_meta.get("exists"):
        return {
            "status": "NOT_FOUND",
            "issues": ["PMID does not exist in PubMed"],
        }

    issues = []
    ct = _strip_diacritics(citation_text).lower()
    first_author = pubmed_meta.get("first_author", "")
    last_author = pubmed_meta.get("last_author", "")
    journal = pubmed_meta.get("journal", "")
    journal_abbrev = pubmed_meta.get("journal_abbrev", "")
    year = pubmed_meta.get("year", "")

    # Detect guideline/consensus/trial citations early — these follow
    # different conventions (org name instead of first author, etc.)
    is_guideline = any(gw in ct for gw in GUIDELINE_INDICATORS)

    # --- Author check ---
    # For guidelines, skip author matching entirely — they cite by org name
    if not is_guideline:
        first_author_last = first_author.split()[0] if first_author else ""
        last_author_last = last_author.split()[0] if last_author else ""

        # Normalize author names too (handle diacritics in PubMed data)
        fa_norm = _strip_diacritics(first_author_last).lower()
        la_norm = _strip_diacritics(last_author_last).lower()

        author_found = False
        if fa_norm and fa_norm in ct:
            author_found = True
        elif la_norm and la_norm in ct:
            author_found = True

        # Also check first 5 co-author surnames
        if not author_found:
            for author in pubmed_meta.get("authors", [])[:5]:
                surname = author.split()[0] if author else ""
                surname_norm = _strip_diacritics(surname).lower()
                if surname_norm and len(surname_norm) > 2 and surname_norm in ct:
                    author_found = True
                    break

        if not author_found and first_author_last:
            issues.append(f"Author: expected '{first_author}', not found in citation text")

    # --- Year check ---
    if year and year not in citation_text:
        issues.append(f"Year: expected '{year}', not found in citation text")

    # --- Journal check (fuzzy — abbreviations vary widely) ---
    jl = _strip_diacritics(journal).lower()
    jal = _strip_diacritics(journal_abbrev).lower()

    # Common journal abbreviation mappings
    journal_aliases = {
        "the new england journal of medicine": ["nejm", "n engl j med"],
        "the lancet": ["lancet"],
        "the lancet. neurology": ["lancet neurol"],
        "the lancet neurology": ["lancet neurol"],
        "jama neurology": ["jama neurol"],
        "annals of neurology": ["ann neurol"],
        "neurology": ["neurology"],
        "epilepsia": ["epilepsia"],
        "cephalalgia": ["cephalalgia"],
        "stroke": ["stroke"],
        "brain": ["brain"],
        "journal of neurology, neurosurgery, and psychiatry": ["j neurol neurosurg psychiatry", "jnnp"],
        "annals of emergency medicine": ["ann emerg med"],
        "academic emergency medicine": ["acad emerg med"],
        "critical care medicine": ["crit care med"],
        "neurocritical care": ["neurocrit care"],
        "journal of neuroimmunology": ["j neuroimmunol"],
        "movement disorders": ["mov disord"],
        "headache": ["headache"],
        "journal of neurosurgery": ["j neurosurg"],
        "neurosurgery": ["neurosurgery"],
        "journal of stroke and cerebrovascular diseases": ["j stroke cerebrovasc dis"],
        "journal of the neurological sciences": ["j neurol sci"],
        "multiple sclerosis": ["mult scler"],
        "archives of neurology": ["arch neurol"],
        "current neurology and neuroscience reports": ["curr neurol neurosci rep"],
        "seizure": ["seizure"],
        "epilepsy & behavior": ["epilepsy behav"],
        "journal of clinical neuroscience": ["j clin neurosci"],
        "frontiers in neurology": ["front neurol"],
        "nature reviews. neurology": ["nat rev neurol"],
        "lancet neurology": ["lancet neurol"],
    }

    journal_found = False
    if jal and jal in ct:
        journal_found = True
    elif jl and jl in ct:
        journal_found = True
    else:
        for full_name, abbrevs in journal_aliases.items():
            if jl.startswith(full_name) or full_name.startswith(jl):
                for abbr in abbrevs:
                    if abbr in ct:
                        journal_found = True
                        break
            if journal_found:
                break

    # Don't flag journal mismatch for guidelines (commonly cited by org name)
    if not journal_found and journal and not is_guideline:
        issues.append(f"Journal: expected '{journal_abbrev or journal}', not found in citation text")

    # --- Determine status ---
    if not issues:
        status = "VERIFIED"
    elif len(issues) == 1 and "Journal" in issues[0]:
        status = "PARTIAL"  # Journal name mismatches are often just abbreviation differences
    else:
        status = "MISMATCH"

    return {
        "status": status,
        "issues": issues,
        "pubmed": {
            "title": pubmed_meta.get("title", ""),
            "first_author": first_author,
            "journal": journal_abbrev or journal,
            "year": year,
            "doi": pubmed_meta.get("doi", ""),
        },
    }


# ---------------------------------------------------------------------------
# Citation text parser — extract author, journal, year from citation text
# ---------------------------------------------------------------------------

# Map common abbreviations used in citation text to PubMed-searchable journal names
JOURNAL_SEARCH_MAP = {
    "nejm": "N Engl J Med",
    "n engl j med": "N Engl J Med",
    "lancet": "Lancet",
    "lancet neurol": "Lancet Neurol",
    "jama neurol": "JAMA Neurol",
    "ann neurol": "Ann Neurol",
    "neurology": "Neurology",
    "epilepsia": "Epilepsia",
    "cephalalgia": "Cephalalgia",
    "stroke": "Stroke",
    "brain": "Brain",
    "headache": "Headache",
    "jnnp": "J Neurol Neurosurg Psychiatry",
    "j neurol neurosurg psychiatry": "J Neurol Neurosurg Psychiatry",
    "ann emerg med": "Ann Emerg Med",
    "acad emerg med": "Acad Emerg Med",
    "crit care med": "Crit Care Med",
    "neurocrit care": "Neurocrit Care",
    "j neuroimmunol": "J Neuroimmunol",
    "mov disord": "Mov Disord",
    "j neurosurg": "J Neurosurg",
    "neurosurgery": "Neurosurgery",
    "cochrane": "Cochrane Database Syst Rev",
    "cochrane review": "Cochrane Database Syst Rev",
    "muscle nerve": "Muscle Nerve",
    "j neurol sci": "J Neurol Sci",
    "mult scler": "Mult Scler",
    "arch neurol": "Arch Neurol",
    "seizure": "Seizure",
    "epilepsy behav": "Epilepsy Behav",
    "front neurol": "Front Neurol",
    "nat rev neurol": "Nat Rev Neurol",
    "semin neurol": "Semin Neurol",
    "j clin neurosci": "J Clin Neurosci",
    "curr neurol neurosci rep": "Curr Neurol Neurosci Rep",
    "jama": "JAMA",
    "bmj": "BMJ",
    "ann intern med": "Ann Intern Med",
    "n engl j med": "N Engl J Med",
    "j neurol": "J Neurol",
    "eur j neurol": "Eur J Neurol",
    "j clin neurophysiol": "J Clin Neurophysiol",
    "clin neurophysiol": "Clin Neurophysiol",
    "j stroke cerebrovasc dis": "J Stroke Cerebrovasc Dis",
    "int j stroke": "Int J Stroke",
    "cerebrovasc dis": "Cerebrovasc Dis",
    "parkinsonism relat disord": "Parkinsonism Relat Disord",
    "j parkinsons dis": "J Parkinsons Dis",
    "amyotroph lateral scler": "Amyotroph Lateral Scler",
    "j peripher nerv syst": "J Peripher Nerv Syst",
    "autoimmun rev": "Autoimmun Rev",
    "mult scler relat disord": "Mult Scler Relat Disord",
    "j neuroophthalmol": "J Neuroophthalmol",
    "neurol clin": "Neurol Clin",
    "neurol clin pract": "Neurol Clin Pract",
    "ther adv neurol disord": "Ther Adv Neurol Disord",
    "expert rev neurother": "Expert Rev Neurother",
    "continuum": "Continuum (Minneap Minn)",
    "pract neurol": "Pract Neurol",
    "curr opin neurol": "Curr Opin Neurol",
    "j child neurol": "J Child Neurol",
    "dev med child neurol": "Dev Med Child Neurol",
    "j headache pain": "J Headache Pain",
    "j emerg med": "J Emerg Med",
    "emerg med clin north am": "Emerg Med Clin North Am",
    "crit care": "Crit Care",
    "intensive care med": "Intensive Care Med",
    "j intensive care med": "J Intensive Care Med",
    "chest": "Chest",
    "mayo clin proc": "Mayo Clin Proc",
    "ther clin risk manag": "Ther Clin Risk Manag",
    "drugs": "Drugs",
    "cns drugs": "CNS Drugs",
    "clin infect dis": "Clin Infect Dis",
    "j infect dis": "J Infect Dis",
    "j antimicrob chemother": "J Antimicrob Chemother",
    "j neurovirol": "J Neurovirol",
    "j neuropathol exp neurol": "J Neuropathol Exp Neurol",
    "acta neuropathol": "Acta Neuropathol",
    "acta neurol scand": "Acta Neurol Scand",
    "j neurooncol": "J Neurooncol",
    "neuro oncol": "Neuro Oncol",
    "cancer": "Cancer",
    "j clin oncol": "J Clin Oncol",
}


def parse_citation_text(text: str) -> dict:
    """
    Parse citation text into searchable components.

    Handles patterns like:
      "Author et al. Journal Year;vol:pages"
      "Author, Author2. Journal Year"
      "Author. Journal Year"
      "Org Guidelines Year"
      "PubMed: 12345678"

    Returns dict with keys: author, journal, year, is_guideline
    """
    result = {"author": "", "journal": "", "year": "", "is_guideline": False}

    # Skip bare PMID references
    if re.match(r'^PubMed:\s*\d+$', text.strip()):
        return result

    # Extract year (4-digit number 19xx or 20xx)
    year_match = re.search(r'\b((?:19|20)\d{2})\b', text)
    if year_match:
        result["year"] = year_match.group(1)

    # Check if guideline-style citation
    ct_lower = _strip_diacritics(text).lower()
    result["is_guideline"] = any(gw in ct_lower for gw in GUIDELINE_INDICATORS)

    # Remove trial name in parens, volume/pages, DOI
    clean = re.sub(r'\([^)]*\)', '', text)        # Remove (REGAIN), (CHAMPION-MG)
    clean = re.sub(r';\s*\d+[^,]*$', '', clean)   # Remove ;337:689-695
    clean = re.sub(r'\bdoi:?\s*\S+', '', clean, flags=re.IGNORECASE)
    clean = clean.strip().rstrip('.')

    # Extract author - everything before "et al.", "&", "and", or first period
    author = ""
    remainder = clean

    # Pattern 1: "Author et al. Journal Year"
    et_al_match = re.match(r'(.+?)\s+et\s+al\.?\s*[.,]?\s*', clean)
    if et_al_match:
        author = et_al_match.group(1).strip().rstrip(',')
        remainder = clean[et_al_match.end():].strip().rstrip('.')
    else:
        # Pattern 2: "Author1 & Author2. Journal Year" or "Author1 and Author2. Journal Year"
        amp_match = re.match(r'([A-Z][a-zA-Zéèêëàâäùûüïîôöç\'-]+(?:\s+[A-Z]{1,3})?)\s*(?:&|and)\s*[A-Z].+?\.\s*(.+)', clean)
        if amp_match:
            author = amp_match.group(1).strip()
            remainder = amp_match.group(2).strip().rstrip('.')
        else:
            # Pattern 3: "Author1, Author2. Journal Year" (two named authors, may have Jr/Sr)
            two_auth_match = re.match(r'([A-Z][a-zA-Zéèêëàâäùûüïîôöç\'-]+(?:\s+[A-Z]{1,3})?(?:\s+(?:Jr|Sr|III?|IV))?),\s*[A-Z][a-zA-Z\'-]+(?:\s+[A-Z]{1,3})?(?:\s+(?:Jr|Sr|III?|IV))?\.\s*(.+)', clean)
            if two_auth_match:
                author = two_auth_match.group(1).strip()
                remainder = two_auth_match.group(2).strip().rstrip('.')
            else:
                # Pattern 4: "Author. Journal Year" (single author)
                dot_match = re.match(r'([A-Z][a-zA-Zéèêëàâäùûüïîôöç\'-]+(?:\s+[A-Z]{1,3})?)\.\s*(.+)', clean)
                if dot_match:
                    author = dot_match.group(1).strip()
                    remainder = dot_match.group(2).strip().rstrip('.')

    # Fallback: check for parenthetical author — "Trial Name (Author et al.)"
    if not author:
        paren_match = re.search(r'\(([A-Z][a-zA-Z\'-]+)\s+et\s+al\.?\)', text)
        if paren_match:
            author = paren_match.group(1).strip()

    result["author"] = author

    # Extract journal from remainder (strip year and extra whitespace)
    if result["year"] and remainder:
        journal = remainder.replace(result["year"], "").strip().rstrip('.').strip()
        # Remove leading/trailing punctuation
        journal = journal.strip('.,;: ')
        if journal:
            result["journal"] = journal
    elif remainder and not author:
        # Entire text might be like "NCS Guidelines 2012" — journal = ""
        pass
    elif remainder:
        result["journal"] = remainder.strip('.,;: ')

    return result


def _resolve_journal_for_search(journal_hint: str) -> str:
    """Convert a journal abbreviation from citation text to PubMed-searchable form."""
    if not journal_hint:
        return ""
    hint_lower = journal_hint.lower().strip()
    # Direct lookup
    if hint_lower in JOURNAL_SEARCH_MAP:
        return JOURNAL_SEARCH_MAP[hint_lower]
    # Try without trailing period
    hint_clean = hint_lower.rstrip('.')
    if hint_clean in JOURNAL_SEARCH_MAP:
        return JOURNAL_SEARCH_MAP[hint_clean]
    # Return as-is (PubMed may still recognize it)
    return journal_hint


def find_correct_pmid(citation_text: str, wrong_pmid: str) -> dict:
    """
    Search PubMed to find the correct PMID for a mismatched citation.

    Tries multiple search strategies:
    1. Author + Journal + Year (most specific)
    2. Author + Year (broader — journal abbreviation might not match)
    3. Author + Journal (no year — date might be off by 1)

    Returns dict: {pmid, confidence, method, metadata} or {pmid: None, ...}
    """
    parsed = parse_citation_text(citation_text)
    author = parsed["author"]
    journal_hint = parsed["journal"]
    year = parsed["year"]

    if not author and not year:
        return {"pmid": None, "confidence": "none", "method": "no_searchable_info",
                "citation": citation_text}

    journal_search = _resolve_journal_for_search(journal_hint)

    # Extract author surname for search (e.g., "Mayo-Smith MF" → "Mayo-Smith")
    author_surname = ""
    if author:
        # Handle "Last First" or "Last FM" format
        parts = author.split()
        if parts:
            author_surname = _strip_diacritics(parts[0]).rstrip(',')

    strategies = []

    # Strategy 1: Author + Journal + Year (most specific)
    if author_surname and journal_search and year:
        strategies.append({
            "name": "author+journal+year",
            "author": author_surname,
            "journal": journal_search,
            "year": year,
        })

    # Strategy 2: Author + Year (broader)
    if author_surname and year:
        strategies.append({
            "name": "author+year",
            "author": author_surname,
            "journal": "",
            "year": year,
        })

    # Strategy 3: Author + Journal (year might be off by 1)
    if author_surname and journal_search:
        strategies.append({
            "name": "author+journal",
            "author": author_surname,
            "journal": journal_search,
            "year": "",
        })

    # Strategy 4: Just author surname (last resort for uncommon names)
    if author_surname and len(author_surname) > 5:
        strategies.append({
            "name": "author_only",
            "author": author_surname,
            "journal": "",
            "year": "",
        })

    for strategy in strategies:
        time.sleep(RATE_LIMIT_DELAY)

        results = search_pubmed(
            author=strategy["author"],
            journal=strategy["journal"],
            year=strategy["year"],
            max_results=5,
        )

        if not results:
            continue

        # Filter out the known-wrong PMID
        candidates = [r for r in results if r != wrong_pmid]
        if not candidates:
            continue

        # If we got exactly 1 candidate, high confidence
        if len(candidates) == 1:
            return {
                "pmid": candidates[0],
                "confidence": "high",
                "method": strategy["name"],
                "citation": citation_text,
                "all_candidates": candidates,
            }

        # Multiple candidates — fetch metadata and pick the best match
        time.sleep(RATE_LIMIT_DELAY)
        candidate_meta = fetch_pmid_metadata(candidates[:5])

        best = None
        best_score = -1

        for cand_pmid in candidates[:5]:
            meta = candidate_meta.get(cand_pmid, {})
            if not meta.get("exists"):
                continue

            score = _score_candidate(citation_text, parsed, meta)
            if score > best_score:
                best_score = score
                best = cand_pmid

        if best and best_score >= 2:
            confidence = "high" if best_score >= 3 else "medium"
            return {
                "pmid": best,
                "confidence": confidence,
                "method": strategy["name"],
                "citation": citation_text,
                "score": best_score,
                "all_candidates": candidates[:5],
            }

    return {"pmid": None, "confidence": "none", "method": "exhausted",
            "citation": citation_text}


def _score_candidate(citation_text: str, parsed: dict, meta: dict) -> int:
    """Score how well a PubMed record matches the citation text. Higher = better."""
    score = 0
    ct = _strip_diacritics(citation_text).lower()

    # Author match (+2 for first author, +1 for any author)
    first_author = meta.get("first_author", "")
    if first_author:
        fa_surname = _strip_diacritics(first_author.split()[0]).lower() if first_author.split() else ""
        if fa_surname and fa_surname in ct:
            score += 2
        else:
            # Check any of the first 5 authors
            for auth in meta.get("authors", [])[:5]:
                surname = _strip_diacritics(auth.split()[0]).lower() if auth.split() else ""
                if surname and len(surname) > 2 and surname in ct:
                    score += 1
                    break

    # Year match (+1)
    year = meta.get("year", "")
    if year and year in citation_text:
        score += 1

    # Journal match (+1)
    journal_abbrev = _strip_diacritics(meta.get("journal_abbrev", "")).lower()
    journal_full = _strip_diacritics(meta.get("journal", "")).lower()
    journal_hint = parsed.get("journal", "").lower()
    if journal_abbrev and journal_abbrev in ct:
        score += 1
    elif journal_full and journal_full in ct:
        score += 1
    elif journal_hint:
        resolved = _resolve_journal_for_search(journal_hint).lower()
        if resolved and (resolved in journal_abbrev or journal_abbrev in resolved
                         or resolved in journal_full or journal_full in resolved):
            score += 1

    return score


def repair_mismatches(plan_citations: dict, metadata: dict, quiet: bool = False) -> dict:
    """
    For all MISMATCH citations, attempt to find correct PMIDs via PubMed search.
    Returns dict keyed by plan stem, each containing list of repair results.
    """
    repairs = {}
    total_mismatches = 0
    total_found = 0
    total_high = 0
    total_medium = 0

    # Pre-count mismatches per plan for progress display
    plans_with_mismatches = []
    for plan in sorted(plan_citations.keys()):
        count = 0
        for cit in plan_citations[plan]:
            pmid = cit["pmid"]
            meta = metadata.get(pmid, {"exists": False})
            result = compare_citation(cit["citation"], meta)
            if result["status"] in ("MISMATCH", "NOT_FOUND"):
                count += 1
        if count > 0:
            plans_with_mismatches.append((plan, count))

    total_plans = len(plans_with_mismatches)
    total_expected = sum(c for _, c in plans_with_mismatches)

    for plan_idx, (plan, _) in enumerate(plans_with_mismatches, 1):
        citations = plan_citations[plan]
        plan_repairs = []

        # Progress: always show which plan we're on
        print(f"  [{plan_idx}/{total_plans}] {plan}...", end="", flush=True)

        for cit in citations:
            pmid = cit["pmid"]
            meta = metadata.get(pmid, {"exists": False})
            result = compare_citation(cit["citation"], meta)

            if result["status"] not in ("MISMATCH", "NOT_FOUND"):
                continue

            total_mismatches += 1
            repair = find_correct_pmid(cit["citation"], pmid)
            repair["old_pmid"] = pmid
            repair["line"] = cit.get("line")
            repair["match_text"] = cit.get("match_text", "")

            if repair["pmid"]:
                total_found += 1
                if repair["confidence"] == "high":
                    total_high += 1
                else:
                    total_medium += 1

            plan_repairs.append(repair)

        if plan_repairs:
            repairs[plan] = plan_repairs
            found_count = sum(1 for r in plan_repairs if r["pmid"])
            print(f" {found_count}/{len(plan_repairs)} found "
                  f"(total: {total_found}/{total_mismatches})", flush=True)
        else:
            print(" no mismatches", flush=True)

    print(f"\n{'='*70}")
    print(f"  REPAIR SUMMARY")
    print(f"{'='*70}")
    print(f"  Total mismatches processed: {total_mismatches}")
    print(f"  Correct PMIDs found:        {total_found} "
          f"({total_found/total_mismatches*100:.0f}%)" if total_mismatches else "")
    print(f"    High confidence:           {total_high}")
    print(f"    Medium confidence:          {total_medium}")
    print(f"  Not found:                   {total_mismatches - total_found}")
    print(f"{'='*70}")

    return repairs


def apply_pmid_repairs(md_files: list, repairs: dict, confidence_threshold: str = "high") -> int:
    """
    Apply PMID corrections to markdown files.
    Only applies repairs at or above the confidence threshold.
    Returns total number of fixes applied.
    """
    min_confidence = {"high": 2, "medium": 1, "low": 0}
    threshold = min_confidence.get(confidence_threshold, 2)
    confidence_rank = {"high": 2, "medium": 1, "low": 0, "none": -1}

    total_fixes = 0

    for plan, plan_repairs in repairs.items():
        md_path = next((f for f in md_files if f.stem == plan), None)
        if not md_path:
            continue

        content = md_path.read_text(encoding="utf-8")
        fixes_in_plan = 0

        for repair in plan_repairs:
            if not repair.get("pmid"):
                continue
            if confidence_rank.get(repair["confidence"], -1) < threshold:
                continue

            old_pmid = repair["old_pmid"]
            new_pmid = repair["pmid"]

            # Replace the PubMed URL, preserving the citation text
            old_url = f"https://pubmed.ncbi.nlm.nih.gov/{old_pmid}/"
            new_url = f"https://pubmed.ncbi.nlm.nih.gov/{new_pmid}/"

            # Also handle URLs without trailing slash
            old_url_noslash = f"https://pubmed.ncbi.nlm.nih.gov/{old_pmid}"

            if old_url in content:
                content = content.replace(old_url, new_url)
                fixes_in_plan += 1
            elif old_url_noslash in content:
                content = content.replace(old_url_noslash, new_url)
                fixes_in_plan += 1

        if fixes_in_plan > 0:
            md_path.write_text(content, encoding="utf-8")
            print(f"  ✏️  Fixed {fixes_in_plan} PMID(s) in {md_path.name}")
            total_fixes += fixes_in_plan

    return total_fixes


# ---------------------------------------------------------------------------
# Fix mode — update citation text in markdown
# ---------------------------------------------------------------------------

def build_corrected_citation(pubmed_meta: dict) -> str:
    """Build a corrected citation string from PubMed metadata."""
    first_author = pubmed_meta.get("first_author", "Unknown")
    journal = pubmed_meta.get("journal_abbrev", "") or pubmed_meta.get("journal", "")
    year = pubmed_meta.get("year", "")
    title = pubmed_meta.get("title", "")

    # Shorten title for display
    if len(title) > 80:
        title = title[:77] + "..."

    # Format: "Author et al. Journal Year"
    num_authors = len(pubmed_meta.get("authors", []))
    if num_authors > 2:
        author_str = f"{first_author} et al."
    elif num_authors == 2:
        second = pubmed_meta["authors"][1]
        author_str = f"{first_author}, {second}"
    else:
        author_str = first_author

    parts = [author_str]
    if journal:
        parts.append(journal)
    if year:
        parts.append(year)

    return " ".join(parts)


def apply_fixes(file_path: Path, citations: list[dict], metadata: dict) -> int:
    """Update citation text in the file to match PubMed metadata. Returns fix count."""
    content = file_path.read_text(encoding="utf-8")
    fixes = 0

    for cit in citations:
        pmid = cit["pmid"]
        meta = metadata.get(pmid, {})
        if not meta.get("exists"):
            continue

        result = compare_citation(cit["citation"], meta)
        if result["status"] == "MISMATCH":
            corrected = build_corrected_citation(meta)
            old_link = f'[{cit["citation"]}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)'
            new_link = f'[{corrected}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)'
            if old_link in content:
                content = content.replace(old_link, new_link, 1)
                fixes += 1

    if fixes > 0:
        file_path.write_text(content, encoding="utf-8")

    return fixes


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

SYMBOLS = {
    "VERIFIED": "✅",
    "PARTIAL": "⚠️",
    "MISMATCH": "❌",
    "NOT_FOUND": "💀",
}


def print_plan_report(plan_name: str, citations: list[dict], metadata: dict,
                      unlinked: list[dict], quiet: bool = False):
    """Print verification report for a single plan."""
    if not citations and not unlinked:
        return

    counts = {"VERIFIED": 0, "PARTIAL": 0, "MISMATCH": 0, "NOT_FOUND": 0}
    results = []

    for cit in citations:
        pmid = cit["pmid"]
        meta = metadata.get(pmid, {"exists": False})
        result = compare_citation(cit["citation"], meta)
        counts[result["status"]] += 1
        results.append((cit, result))

    total = len(citations)
    verified_pct = (counts["VERIFIED"] + counts["PARTIAL"]) / total * 100 if total else 0

    print(f"\n{'='*70}")
    print(f"  {plan_name}")
    print(f"{'='*70}")
    print(f"  Linked citations: {total}   |   "
          f"✅ {counts['VERIFIED']}  ⚠️  {counts['PARTIAL']}  "
          f"❌ {counts['MISMATCH']}  💀 {counts['NOT_FOUND']}   |   "
          f"{verified_pct:.0f}% verified")

    if unlinked:
        print(f"  Unlinked citations: {len(unlinked)}")

    if quiet and counts["MISMATCH"] == 0 and counts["NOT_FOUND"] == 0:
        return counts  # Skip detail output but still return counts

    # Print issues
    for cit, result in results:
        if result["status"] in ("MISMATCH", "NOT_FOUND"):
            sym = SYMBOLS[result["status"]]
            print(f"\n  {sym} PMID {cit['pmid']}: {result['status']}")
            print(f"     Claimed:  {cit['citation']}")
            if result.get("pubmed"):
                pm = result["pubmed"]
                print(f"     Actual:   {pm.get('first_author', '?')} — "
                      f"{pm.get('journal', '?')} {pm.get('year', '?')}")
                print(f"     Title:    {pm.get('title', '?')[:90]}")
            for issue in result.get("issues", []):
                print(f"     → {issue}")

        elif result["status"] == "PARTIAL" and not quiet:
            sym = SYMBOLS[result["status"]]
            print(f"\n  {sym}  PMID {cit['pmid']}: {result['status']}")
            print(f"     Claimed:  {cit['citation']}")
            for issue in result.get("issues", []):
                print(f"     → {issue}")

    return counts


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Verify PubMed citations in neuro-plan templates",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("markdown_file", nargs="*",
                        help="Path to one or more plan markdown files")
    parser.add_argument("--all", action="store_true",
                        help="Process all plans in docs/plans/")
    parser.add_argument("--verify", action="store_true",
                        help="Verify PMIDs against PubMed API")
    parser.add_argument("--fix", action="store_true",
                        help="Auto-correct mismatched citation text (implies --verify)")
    parser.add_argument("--repair", action="store_true",
                        help="Find correct PMIDs for mismatched citations (implies --verify)")
    parser.add_argument("--apply", action="store_true",
                        help="Apply PMID corrections to files (implies --repair)")
    parser.add_argument("--confidence", choices=["high", "medium"],
                        default="high",
                        help="Minimum confidence for --apply (default: high)")
    parser.add_argument("--json", metavar="FILE",
                        help="Write results to JSON file")
    parser.add_argument("--quiet", "-q", action="store_true",
                        help="Only show plans with issues")

    args = parser.parse_args()

    if args.apply:
        args.repair = True
    if args.repair:
        args.verify = True
    if args.fix:
        args.verify = True

    # Determine files
    if args.all:
        plans_dir = Path("docs/plans")
        md_files = sorted(plans_dir.glob("*.md"))
        md_files = [f for f in md_files
                    if f.name != "index.md" and "-report-" not in f.name]
    elif args.markdown_file:
        md_files = [Path(f) for f in args.markdown_file]
    else:
        parser.print_help()
        sys.exit(1)

    # Phase 1: Extract all PMIDs from all files
    plan_citations = {}  # plan_stem -> list of citation dicts
    plan_unlinked = {}   # plan_stem -> list of unlinked citations
    all_pmids = set()

    for md_path in md_files:
        if not md_path.exists():
            print(f"File not found: {md_path}", file=sys.stderr)
            continue

        citations = extract_citations(md_path)
        unlinked = extract_unlinked_citations(md_path)
        plan_citations[md_path.stem] = citations
        plan_unlinked[md_path.stem] = unlinked

        for c in citations:
            all_pmids.add(c["pmid"])

    total_citations = sum(len(v) for v in plan_citations.values())
    total_unlinked = sum(len(v) for v in plan_unlinked.values())

    print(f"\nExtracted {total_citations} linked citations "
          f"({len(all_pmids)} unique PMIDs) from {len(plan_citations)} plans")
    if total_unlinked:
        print(f"Found {total_unlinked} unlinked citations (no PubMed URL)")

    if not args.verify:
        # Extract-only mode — just list what we found
        for plan, citations in sorted(plan_citations.items()):
            if not citations:
                continue
            print(f"\n{'='*60}")
            print(f"PLAN: {plan}")
            print(f"{'='*60}")
            for i, c in enumerate(citations, 1):
                print(f"  {i}. PMID {c['pmid']}: {c['citation']}")

        pmids_sorted = sorted(all_pmids)
        print(f"\nUnique PMIDs ({len(pmids_sorted)}):")
        print(", ".join(pmids_sorted))
        return

    # Phase 2: Batch-verify all PMIDs via PubMed API
    print(f"\nVerifying {len(all_pmids)} unique PMIDs against PubMed API...")
    pmid_list = sorted(all_pmids)
    metadata = fetch_pmid_metadata(pmid_list)

    found = sum(1 for v in metadata.values() if v.get("exists"))
    not_found = sum(1 for v in metadata.values() if not v.get("exists"))
    print(f"  API results: {found} found, {not_found} not found\n")

    # Phase 3: Compare and report
    grand_totals = {"VERIFIED": 0, "PARTIAL": 0, "MISMATCH": 0, "NOT_FOUND": 0}
    json_results = {}
    total_fixes = 0

    for plan in sorted(plan_citations.keys()):
        citations = plan_citations[plan]
        unlinked = plan_unlinked.get(plan, [])
        if not citations:
            continue

        counts = print_plan_report(plan, citations, metadata, unlinked, args.quiet)
        if counts:
            for k in grand_totals:
                grand_totals[k] += counts.get(k, 0)

        # Fix mode
        if args.fix:
            md_path = next((f for f in md_files if f.stem == plan), None)
            if md_path:
                fixes = apply_fixes(md_path, citations, metadata)
                if fixes:
                    print(f"  ✏️  Fixed {fixes} citation(s) in {md_path.name}")
                    total_fixes += fixes

        # Build JSON output
        if args.json:
            plan_results = []
            for cit in citations:
                pmid = cit["pmid"]
                meta = metadata.get(pmid, {"exists": False})
                result = compare_citation(cit["citation"], meta)
                plan_results.append({
                    "pmid": pmid,
                    "claimed": cit["citation"],
                    "line": cit.get("line"),
                    "status": result["status"],
                    "issues": result.get("issues", []),
                    "pubmed": result.get("pubmed"),
                })
            json_results[plan] = {
                "linked": plan_results,
                "unlinked": unlinked,
            }

    # Grand summary
    grand_total = sum(grand_totals.values())
    verified_pct = (grand_totals["VERIFIED"] + grand_totals["PARTIAL"]) / grand_total * 100 if grand_total else 0

    print(f"\n{'='*70}")
    print(f"  VERIFICATION SUMMARY")
    print(f"{'='*70}")
    print(f"  Plans checked:       {len([p for p in plan_citations if plan_citations[p]])}")
    print(f"  Citations verified:  {grand_total}")
    print(f"  ✅ Verified:          {grand_totals['VERIFIED']}")
    print(f"  ⚠️  Partial match:    {grand_totals['PARTIAL']}")
    print(f"  ❌ Mismatch:          {grand_totals['MISMATCH']}")
    print(f"  💀 Not found:         {grand_totals['NOT_FOUND']}")
    print(f"  Accuracy:            {verified_pct:.1f}%")
    if total_unlinked:
        print(f"  Unlinked citations:  {total_unlinked}")
    if total_fixes:
        print(f"  Auto-fixed:          {total_fixes}")
    print(f"{'='*70}")

    if grand_totals["NOT_FOUND"] > 0:
        print(f"\n⚠️  {grand_totals['NOT_FOUND']} PMID(s) do not exist in PubMed!")

    # Phase 4: Repair — find correct PMIDs for mismatches
    repairs = {}
    total_pmid_fixes = 0
    if args.repair and (grand_totals["MISMATCH"] + grand_totals["NOT_FOUND"]) > 0:
        mismatch_count = grand_totals["MISMATCH"] + grand_totals["NOT_FOUND"]
        print(f"\n{'='*70}")
        print(f"  REPAIR PHASE — searching for correct PMIDs ({mismatch_count} mismatches)")
        print(f"{'='*70}\n")

        repairs = repair_mismatches(plan_citations, metadata, quiet=args.quiet)

        # Apply corrections if requested
        if args.apply and repairs:
            print(f"\nApplying corrections (confidence >= {args.confidence})...\n")
            total_pmid_fixes = apply_pmid_repairs(md_files, repairs,
                                                  confidence_threshold=args.confidence)
            if total_pmid_fixes:
                print(f"\n  Total PMIDs corrected: {total_pmid_fixes}")
            else:
                print("  No corrections met the confidence threshold.")

    # Write JSON
    if args.json:
        json_output = {
            "summary": {
                "total_citations": grand_total,
                "verified": grand_totals["VERIFIED"],
                "partial": grand_totals["PARTIAL"],
                "mismatch": grand_totals["MISMATCH"],
                "not_found": grand_totals["NOT_FOUND"],
                "accuracy_pct": round(verified_pct, 1),
                "unlinked": total_unlinked,
                "pmids_corrected": total_pmid_fixes,
            },
            "plans": json_results,
        }
        if repairs:
            # Add repair results to JSON
            repair_json = {}
            for plan, plan_repairs in repairs.items():
                repair_json[plan] = [
                    {
                        "citation": r["citation"],
                        "old_pmid": r["old_pmid"],
                        "new_pmid": r.get("pmid"),
                        "confidence": r.get("confidence", "none"),
                        "method": r.get("method", ""),
                        "line": r.get("line"),
                    }
                    for r in plan_repairs
                ]
            json_output["repairs"] = repair_json

        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(json_output, f, indent=2, ensure_ascii=False)
        print(f"\nResults written to {args.json}")


if __name__ == "__main__":
    main()
