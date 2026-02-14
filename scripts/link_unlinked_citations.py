#!/usr/bin/env python3
"""
Link unlinked citations in neuro-plans evidence tables.

Searches PubMed for citations that currently have no PubMed link and adds
high-confidence links where found.  Reuses the PubMed API helpers and
citation-parsing logic from verify_citations.py.

Usage:
    # Report mode (no changes)
    python scripts/link_unlinked_citations.py --all --json docs/data/link-report.json

    # Apply high-confidence links
    python scripts/link_unlinked_citations.py --all --apply --confidence high

    # Single plan
    python scripts/link_unlinked_citations.py docs/plans/migraine.md

    # Batch of plans (by index range) — avoids PubMed API timeouts
    python scripts/link_unlinked_citations.py --all --batch 1-15 --json docs/data/link-batch1.json

Modes:
    (default)     Scan and report unlinked citations that could be linked
    --apply       Write PubMed links into markdown files
    --confidence  Minimum confidence to apply: high (default), medium, any
    --json FILE   Write results to JSON file
    --quiet       Suppress per-citation output, show only summary
    --batch N-M   Only process plans N through M (1-indexed, inclusive)
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path
from typing import Optional

# Import shared functions from verify_citations.py (same directory)
sys.path.insert(0, str(Path(__file__).parent))
from verify_citations import (
    search_pubmed,
    fetch_pmid_metadata,
    load_cache,
    save_cache,
    update_cache_from_metadata,
    check_api_connectivity,
    _strip_diacritics,
    _resolve_journal_for_search,
    _score_candidate,
    parse_citation_text,
    extract_unlinked_citations,
    RATE_LIMIT_DELAY,
    JOURNAL_SEARCH_MAP,
    APIError,
)


# ---------------------------------------------------------------------------
# Guideline organization → PubMed journal mapping
# ---------------------------------------------------------------------------

# Maps organization acronyms to the PubMed journals where their guidelines
# are typically published.  Used for searching guideline-style citations.
ORG_JOURNAL_MAP = {
    # Neurology / Stroke
    "aha": ["Stroke", "Circulation"],
    "aha/asa": ["Stroke", "Circulation"],
    "asa": ["Stroke"],
    "aan": ["Neurology"],
    "aes": ["Epilepsy Curr", "Epilepsia"],
    "ncs": ["Neurocrit Care"],
    "ilae": ["Epilepsia"],
    "ean": ["Eur J Neurol"],
    "efns": ["Eur J Neurol"],
    "aasm": ["J Clin Sleep Med", "Sleep"],
    "acns": ["J Clin Neurophysiol"],
    "naemsp": ["Prehosp Emerg Care"],
    "ahs": ["Headache"],
    "ihs": ["Cephalalgia"],
    "ichd": ["Cephalalgia"],
    "ens": ["Eur J Neurol"],
    "wfn": ["J Neurol Sci"],
    # Neurosurgery
    "aans": ["J Neurosurg", "Neurosurgery"],
    "cns": ["Neurosurgery"],
    # General / specialty
    "acr": ["Radiology", "J Am Coll Radiol"],
    "who": ["Lancet", "Bull World Health Organ"],
    "nice": ["BMJ"],
    "sign": ["BMJ"],
    "acep": ["Ann Emerg Med"],
    "esc": ["Eur Heart J"],
    "acc": ["J Am Coll Cardiol"],
    "idsa": ["Clin Infect Dis"],
    "ats": ["Am J Respir Crit Care Med"],
    "ers": ["Eur Respir J"],
    "erc": ["Resuscitation"],
    "btf": ["J Neurotrauma"],
    "mds": ["Mov Disord"],
    "sccm": ["Crit Care Med"],
    "fda": [],  # not a journal publisher
    "cdc": ["MMWR Morb Mortal Wkly Rep"],
}

# Known trial names → typical journal(s) of the primary publication
TRIAL_JOURNAL_MAP = {
    "esett": "N Engl J Med",
    "rampart": "N Engl J Med",
    "preempt": "Cephalalgia",
    "arise": "Lancet Neurol",
    "dawn": "N Engl J Med",
    "defuse": "N Engl J Med",
    "escape": "N Engl J Med",
    "extend-ia": "N Engl J Med",
    "mr clean": "N Engl J Med",
    "revascat": "N Engl J Med",
    "swift prime": "N Engl J Med",
    "clots": "Lancet",
    "interact": "Lancet Neurol",
    "interact2": "N Engl J Med",
    "atach": "N Engl J Med",
    "atach-2": "N Engl J Med",
    "mistie": "Lancet",
    "clear": "N Engl J Med",
    "isat": "Lancet",
    "brat": "J Neurosurg",
    "coss": "JAMA",
    "sampris": "N Engl J Med",
    "thales": "N Engl J Med",
    "nascet": "N Engl J Med",
    "ecass": "N Engl J Med",
    "sits-most": "Lancet",
    "ninds": "N Engl J Med",
    "champion-mg": "Lancet Neurol",
    "regain": "Lancet Neurol",
    "endorse": "Epilepsia",
    "boost": "N Engl J Med",
    "stich": "Lancet",
    "stich ii": "Lancet",
    "enact": "Lancet Neurol",
    "spotlight": "Lancet Neurol",
    "halt-ms": "Neurology",
    "decide": "N Engl J Med",
    "care-ms": "Lancet Neurol",
    "opera": "N Engl J Med",
}


# ---------------------------------------------------------------------------
# Citation classification — determine search strategy
# ---------------------------------------------------------------------------

def classify_citation(source_text: str) -> str:
    """
    Classify an unlinked citation into a search strategy category.

    Returns one of:
        "author"     — author + year citation (e.g., "Smith et al. Brain 2019")
        "guideline"  — org/guideline citation (e.g., "AHA/ASA 2019 Guidelines")
        "trial"      — named trial (e.g., "THALES trial (Hao et al. NEJM 2020)")
        "skip"       — not searchable (clinical description, table fragment, etc.)
    """
    text = source_text.strip()

    # Too short to be a real citation
    if len(text) < 8:
        return "skip"

    text_lower = _strip_diacritics(text).lower()

    # Skip obvious non-citations
    skip_patterns = [
        r'^\d+[\s-]*(?:min|hour|day|week|month|year)',  # Time targets
        r'^(?:standard|clinical|general|based on|per|routine)',
        r'^(?:first|second|third|early|late|initial)\s+line',
        r'^(?:varies|depends|individualized|as needed)',
        r'^(?:level|class|grade)\s+[a-z0-9]',
        r'^(?:monitor|assess|evaluate|consider)',
        r'^\d+%',
        r'^(?:iv|im|po|sc|sq|prn|bid|tid|qid)\s',
        r'^(?:mg|ml|mcg|units?)[\s/]',
        r'^(?:low|moderate|high)\s+(?:risk|dose|quality)',
        r'^(?:good|poor|fair)\s+(?:prognosis|outcome)',
        r'^\d+\s*[-–]\s*\d+\s*(?:mg|ml|%)',
    ]
    for pat in skip_patterns:
        if re.match(pat, text_lower):
            return "skip"

    # Check for trial names
    for trial in TRIAL_JOURNAL_MAP:
        if trial in text_lower:
            return "trial"

    # Check for guideline indicators
    guideline_words = [
        "guideline", "guidelines", "consensus", "practice parameter",
        "recommendation", "recommendations", "position statement",
        "advisory", "scientific statement", "evidence assessment",
        "task force", "working group",
    ]
    if any(gw in text_lower for gw in guideline_words):
        return "guideline"

    # Check for organization acronyms (only if paired with year)
    has_year = bool(re.search(r'\b(?:19|20)\d{2}\b', text))
    if has_year:
        for org in ORG_JOURNAL_MAP:
            # Match org as whole word (case-insensitive)
            if re.search(r'\b' + re.escape(org) + r'\b', text_lower):
                return "guideline"

    # Check for author + year pattern
    # Must start with a capital letter (author name) and contain a year
    if has_year and re.match(r'^[A-Z]', text):
        # Check for "Author et al." or "Author, Author."  or "Author. Journal"
        if re.search(r'et\s+al', text_lower):
            return "author"
        if re.match(r'^[A-Z][a-zA-Zéèêëàâäùûüïîôöç\'-]+(?:\s+[A-Z]{1,3})?\s*[.,&]', text):
            return "author"
        # Heuristic: capital letter + something + year
        if re.match(r'^[A-Z][a-zA-Z\'-]+\s+', text):
            return "author"

    return "skip"


# ---------------------------------------------------------------------------
# Search strategies
# ---------------------------------------------------------------------------

def search_for_author_citation(source_text: str, cache: dict = None,
                               evidence_context: str = "",
                               plan_topic: str = "") -> dict:
    """
    Search PubMed for an author+year citation.
    Uses the same parse_citation_text() logic as the repair tool.
    """
    parsed = parse_citation_text(source_text)
    author = parsed["author"]
    journal_hint = parsed["journal"]
    year = parsed["year"]

    if not author and not year:
        return _no_result(source_text, "no_author_or_year")

    journal_search = _resolve_journal_for_search(journal_hint)

    # Extract author surname
    author_surname = ""
    if author:
        parts = author.split()
        if parts:
            author_surname = _strip_diacritics(parts[0]).rstrip(',')

    if not author_surname:
        return _no_result(source_text, "no_author_surname")

    # Try strategies in decreasing specificity
    strategies = []

    if author_surname and journal_search and year:
        strategies.append(("author+journal+year", author_surname, journal_search, year))

    if author_surname and year:
        strategies.append(("author+year", author_surname, "", year))

    if author_surname and journal_search:
        strategies.append(("author+journal", author_surname, journal_search, ""))

    for name, auth, jour, yr in strategies:
        time.sleep(RATE_LIMIT_DELAY)
        try:
            results = search_pubmed(author=auth, journal=jour, year=yr, max_results=5)
        except APIError as e:
            return _no_result(source_text, "api_error", str(e))

        if not results:
            continue

        # Score all candidates (even single results) to validate match quality
        best = _pick_best_candidate(results, source_text, parsed, cache,
                                    evidence_context=evidence_context,
                                    plan_topic=plan_topic)
        if best:
            return best

    return _no_result(source_text, "exhausted")


def search_for_guideline(source_text: str, cache: dict = None,
                         evidence_context: str = "",
                         plan_topic: str = "") -> dict:
    """
    Search PubMed for a guideline citation.
    Maps organization acronyms to known PubMed journals and searches by year.
    """
    text_lower = _strip_diacritics(source_text).lower()
    year_match = re.search(r'\b((?:19|20)\d{2})\b', source_text)
    year = year_match.group(1) if year_match else ""

    # Find which org this is about
    matched_org = None
    for org in sorted(ORG_JOURNAL_MAP.keys(), key=len, reverse=True):
        if re.search(r'\b' + re.escape(org) + r'\b', text_lower):
            matched_org = org
            break

    if not matched_org and not year:
        return _no_result(source_text, "no_org_or_year")

    journals = ORG_JOURNAL_MAP.get(matched_org, []) if matched_org else []

    # Extract title keywords from the citation text
    # Remove the org name, year, and common words to get meaningful keywords
    title_words = text_lower
    if matched_org:
        title_words = re.sub(r'\b' + re.escape(matched_org) + r'\b', '', title_words)
    if year:
        title_words = title_words.replace(year, '')
    # Remove common guideline words
    for w in ["guideline", "guidelines", "consensus", "recommendation",
              "recommendations", "update", "updated", "statement",
              "practice", "parameter", "parameters", "scientific",
              "advisory", "position", "evidence", "assessment", "report",
              "review", "management", "treatment", "diagnosis"]:
        title_words = title_words.replace(w, '')
    title_words = ' '.join(title_words.split()).strip('., ')

    # Strategy 1: Search each known journal + year + title keywords
    for journal in journals:
        time.sleep(RATE_LIMIT_DELAY)
        try:
            kw = title_words[:60] if title_words else ""
            results = search_pubmed(
                journal=journal,
                year=year if year else "",
                title_words=kw if kw else "",
                max_results=5,
            )
        except APIError as e:
            continue

        if results:
            parsed = parse_citation_text(source_text)
            best = _pick_best_candidate(results, source_text, parsed, cache,
                                        is_guideline=True,
                                        evidence_context=evidence_context,
                                        plan_topic=plan_topic)
            if best:
                return best

    # Strategy 2: Search by org name as author + year (some guidelines list org as author)
    if matched_org and year:
        time.sleep(RATE_LIMIT_DELAY)
        try:
            # Some orgs are listed as corporate authors
            org_author_names = {
                "aha": "American Heart Association",
                "aha/asa": "American Heart Association",
                "asa": "American Stroke Association",
                "aan": "American Academy of Neurology",
                "ilae": "International League Against Epilepsy",
                "idsa": "Infectious Diseases Society",
                "nice": "National Institute for Health",
                "who": "World Health Organization",
                "acep": "American College of Emergency",
                "btf": "Brain Trauma Foundation",
                "sccm": "Society of Critical Care",
                "mds": "Movement Disorder Society",
            }
            org_full = org_author_names.get(matched_org, "")
            if org_full:
                results = search_pubmed(
                    title_words=org_full + " " + year,
                    max_results=5,
                )
                if results:
                    parsed = parse_citation_text(source_text)
                    best = _pick_best_candidate(results, source_text, parsed, cache,
                                                is_guideline=True,
                                                evidence_context=evidence_context,
                                                plan_topic=plan_topic)
                    if best:
                        return best
        except APIError:
            pass

    # Strategy 3: Title keyword search without journal constraint
    if title_words and year:
        time.sleep(RATE_LIMIT_DELAY)
        try:
            results = search_pubmed(
                year=year,
                title_words=title_words[:80],
                max_results=5,
            )
        except APIError as e:
            return _no_result(source_text, "api_error", str(e))

        if results:
            parsed = parse_citation_text(source_text)
            best = _pick_best_candidate(results, source_text, parsed, cache,
                                        is_guideline=True,
                                        evidence_context=evidence_context,
                                        plan_topic=plan_topic)
            if best:
                return best

    return _no_result(source_text, "exhausted")


def search_for_trial(source_text: str, cache: dict = None,
                     evidence_context: str = "",
                     plan_topic: str = "") -> dict:
    """
    Search PubMed for a named trial citation.
    Uses the trial name + known journal to find the primary publication.
    """
    text_lower = _strip_diacritics(source_text).lower()
    year_match = re.search(r'\b((?:19|20)\d{2})\b', source_text)
    year = year_match.group(1) if year_match else ""

    # Find which trial this is
    matched_trial = None
    for trial in sorted(TRIAL_JOURNAL_MAP.keys(), key=len, reverse=True):
        if trial in text_lower:
            matched_trial = trial
            break

    if not matched_trial:
        return _no_result(source_text, "no_trial_name")

    journal = TRIAL_JOURNAL_MAP[matched_trial]

    # Also check if there's an author in the citation text
    parsed = parse_citation_text(source_text)
    author_surname = ""
    if parsed["author"]:
        parts = parsed["author"].split()
        if parts:
            author_surname = _strip_diacritics(parts[0]).rstrip(',')

    # Strategy 1: Trial name as title keyword + journal + year
    if journal and year:
        time.sleep(RATE_LIMIT_DELAY)
        try:
            results = search_pubmed(
                journal=journal,
                year=year,
                title_words=matched_trial.upper(),
                max_results=5,
            )
        except APIError as e:
            return _no_result(source_text, "api_error", str(e))

        if results:
            best = _pick_best_candidate(results, source_text, parsed, cache,
                                        is_guideline=True,
                                        evidence_context=evidence_context,
                                        plan_topic=plan_topic)
            if best:
                return best

    # Strategy 2: Author + journal + year (if author present)
    if author_surname and journal and year:
        time.sleep(RATE_LIMIT_DELAY)
        try:
            results = search_pubmed(
                author=author_surname,
                journal=journal,
                year=year,
                max_results=5,
            )
        except APIError:
            pass
        else:
            if results:
                best = _pick_best_candidate(results, source_text, parsed, cache,
                                            evidence_context=evidence_context,
                                            plan_topic=plan_topic)
                if best:
                    return best

    # Strategy 3: Trial name + year (no journal)
    if year:
        time.sleep(RATE_LIMIT_DELAY)
        try:
            results = search_pubmed(
                year=year,
                title_words=matched_trial.upper(),
                max_results=5,
            )
        except APIError:
            pass
        else:
            if results:
                best = _pick_best_candidate(results, source_text, parsed, cache,
                                            is_guideline=True,
                                            evidence_context=evidence_context,
                                            plan_topic=plan_topic)
                if best:
                    return best

    # Strategy 4: Trial name only (no year)
    time.sleep(RATE_LIMIT_DELAY)
    try:
        results = search_pubmed(
            title_words=matched_trial.upper(),
            journal=journal if journal else "",
            max_results=5,
        )
    except APIError:
        return _no_result(source_text, "api_error")

    if results:
        best = _pick_best_candidate(results, source_text, parsed, cache,
                                    is_guideline=True,
                                    evidence_context=evidence_context,
                                    plan_topic=plan_topic)
        if best:
            return best

    return _no_result(source_text, "exhausted")


# ---------------------------------------------------------------------------
# Candidate scoring and result helpers
# ---------------------------------------------------------------------------

def _fetch_and_validate(pmid: str, source_text: str, parsed: dict,
                        cache: dict = None) -> Optional[dict]:
    """Fetch metadata for a PMID and return it if it looks like a plausible match."""
    try:
        time.sleep(RATE_LIMIT_DELAY)
        meta = fetch_pmid_metadata([pmid], cache)
        m = meta.get(pmid, {})
        if m.get("exists"):
            return m
    except APIError:
        pass
    return None


def _pick_best_candidate(pmids: list[str], source_text: str, parsed: dict,
                         cache: dict = None, is_guideline: bool = False,
                         evidence_context: str = "",
                         plan_topic: str = "") -> Optional[dict]:
    """
    From a list of candidate PMIDs, pick the best match for the source text.
    Returns a result dict or None if no good match.
    """
    try:
        time.sleep(RATE_LIMIT_DELAY)
        meta_all = fetch_pmid_metadata(pmids[:5], cache)
    except APIError:
        return None

    best_pmid = None
    best_score = -1
    best_meta = None

    for pmid in pmids[:5]:
        m = meta_all.get(pmid, {})
        if not m.get("exists"):
            continue

        score = _score_candidate(source_text, parsed, m)

        # CRITICAL: Penalize year mismatches.  If the citation explicitly states
        # a year (e.g., "Brain 2015") but the PubMed result is from a different
        # year, this is a strong negative signal — likely the wrong paper.
        citation_year = parsed.get("year", "")
        pubmed_year = m.get("year", "")
        if citation_year and pubmed_year and citation_year != pubmed_year:
            score -= 2  # Heavy penalty — year mismatch almost always means wrong paper

        # Penalize first-author mismatch for author-style citations.
        # If the citation says "Grossberg et al." but PubMed's first author
        # is "Davies", that's likely the wrong paper.
        if not is_guideline and parsed.get("author"):
            cited_surname = _strip_diacritics(parsed["author"].split()[0]).lower().rstrip(',')
            pm_first = m.get("first_author", "")
            if pm_first:
                pm_surname = _strip_diacritics(pm_first.split()[0]).lower()
                if cited_surname and pm_surname and cited_surname != pm_surname:
                    # Check if cited author appears anywhere in the author list
                    found_in_authors = False
                    for a in m.get("authors", []):
                        a_surname = _strip_diacritics(a.split()[0]).lower() if a else ""
                        if a_surname == cited_surname:
                            found_in_authors = True
                            break
                    if not found_in_authors:
                        score -= 1  # Moderate penalty — cited author not in author list

        # Penalize journal mismatch for author-style citations that explicitly
        # name a journal.  "Grossberg et al. NEJM 2024" should NOT match a paper
        # in "J Emerg Trauma Shock".
        if not is_guideline and parsed.get("journal"):
            journal_search = _resolve_journal_for_search(parsed["journal"]).lower()
            pm_journal = _strip_diacritics(m.get("journal_abbrev", "")).lower()
            pm_journal_full = _strip_diacritics(m.get("journal", "")).lower()
            if journal_search:
                # Guard against empty-string substring bug: "" in "x" == True in Python.
                # Only compare non-empty strings.
                journal_match = (
                    (pm_journal and (journal_search in pm_journal or pm_journal in journal_search))
                    or (pm_journal_full and (journal_search in pm_journal_full or pm_journal_full in journal_search))
                )
                if not journal_match:
                    score -= 1  # Penalty — journal explicitly named but doesn't match
                    # If _score_candidate falsely gave +1 due to empty-string bug
                    # (empty journal_full always matches via "" in resolved),
                    # apply extra -1 to cancel the false bonus.
                    if not pm_journal_full:
                        score -= 1

        # For guidelines, also check if key terms from the citation appear in the title
        if is_guideline:
            title_lower = _strip_diacritics(m.get("title", "")).lower()
            text_lower = _strip_diacritics(source_text).lower()
            # Bonus for guideline-related words in the PubMed title
            for word in ["guideline", "consensus", "recommendation", "statement",
                         "practice parameter", "advisory"]:
                if word in title_lower:
                    score += 1
                    break
            # Bonus for matching disease/condition terms
            # Extract significant words from citation (> 4 chars, not stopwords)
            stopwords = {"with", "from", "that", "this", "have", "were", "been",
                         "their", "which", "about", "would", "should", "could",
                         "update", "updated", "guidelines", "guideline",
                         "consensus", "recommendation", "recommendations",
                         "management", "treatment", "diagnosis", "clinical",
                         "practice", "parameter", "statement", "scientific"}
            sig_words = [w for w in text_lower.split()
                         if len(w) > 4 and w not in stopwords and w.isalpha()]
            matches = sum(1 for w in sig_words if w in title_lower)
            if matches >= 2:
                score += 1

        # TITLE RELEVANCE CHECK: The PubMed article title should be clinically
        # relevant to the citation context.  This is the strongest signal that
        # we've found the right paper vs a random paper by the same author.
        title_lower = _strip_diacritics(m.get("title", "")).lower()
        if title_lower and evidence_context:
            ev_lower = _strip_diacritics(evidence_context).lower()
            ev_words = set(w for w in ev_lower.split()
                          if len(w) > 4 and w.isalpha())
            # Remove very common medical stopwords
            med_stops = {"study", "trial", "group", "patients", "patient",
                         "results", "analysis", "effect", "effects",
                         "between", "among", "based", "using", "review",
                         "compared", "associated", "significant", "versus",
                         "treated", "treatment", "outcomes", "outcome",
                         "showed", "found", "reported", "evidence", "level",
                         "class", "grade", "score", "total", "initial",
                         "first", "second", "early", "after", "before",
                         "during", "within", "without", "other", "these",
                         "those", "their", "there", "which", "about"}
            ev_words -= med_stops
            title_matches = sum(1 for w in ev_words if w in title_lower)
            if title_matches >= 2:
                score += 1  # Bonus: PubMed title overlaps with evidence claim

        # Also check plan topic relevance (filename-derived)
        if title_lower and plan_topic:
            topic_words = set(w for w in plan_topic.lower().replace('-', ' ').split()
                              if len(w) > 3)
            topic_matches = sum(1 for w in topic_words if w in title_lower)
            if topic_matches >= 1:
                score += 1  # Bonus: PubMed title mentions the plan topic

        if score > best_score:
            best_score = score
            best_pmid = pmid
            best_meta = m

    # Stricter thresholds for new links (we're adding links, not repairing).
    # Score 4+ = high confidence, Score 3 = medium
    # Final gate: if citation names a specific first author but PubMed first
    # author is different, downgrade to medium (likely a co-authored paper).
    if best_pmid and best_score >= 4:
        confidence = "high"
        if not is_guideline and parsed.get("author") and best_meta:
            cited_surname = _strip_diacritics(parsed["author"].split()[0]).lower().rstrip(',')
            pm_first = best_meta.get("first_author", "")
            if pm_first and cited_surname:
                pm_surname = _strip_diacritics(pm_first.split()[0]).lower()
                if cited_surname != pm_surname:
                    confidence = "medium"  # Right topic/journal but wrong first author
        return _found_result(source_text, best_pmid, confidence,
                             "scored_candidates", best_meta, best_score)

    if best_pmid and best_score == 3:
        return _found_result(source_text, best_pmid, "medium",
                             "scored_candidates", best_meta, best_score)

    # Single result that exists but didn't score well enough
    if len(pmids) == 1 and best_meta and best_score >= 1:
        return _found_result(source_text, best_pmid, "low",
                             "single_result_low_score", best_meta, best_score)

    return None


def _found_result(source_text: str, pmid: str, confidence: str,
                  method: str, meta: dict, score: int = 0) -> dict:
    """Build a successful search result."""
    return {
        "source_text": source_text,
        "pmid": pmid,
        "confidence": confidence,
        "method": method,
        "score": score,
        "pubmed_title": meta.get("title", ""),
        "pubmed_author": meta.get("first_author", ""),
        "pubmed_journal": meta.get("journal_abbrev", "") or meta.get("journal", ""),
        "pubmed_year": meta.get("year", ""),
    }


def _no_result(source_text: str, method: str, error: str = "") -> dict:
    """Build a not-found result."""
    return {
        "source_text": source_text,
        "pmid": None,
        "confidence": "none",
        "method": method,
        "error": error,
    }


# ---------------------------------------------------------------------------
# Apply links to markdown files
# ---------------------------------------------------------------------------

def apply_links_to_file(file_path: Path, links: list[dict],
                        min_confidence: str = "high") -> int:
    """
    Replace plain citation text with PubMed-linked text in a markdown file.

    Converts:
        "Smith et al. Brain 2019"
    To:
        "[Smith et al. Brain 2019](https://pubmed.ncbi.nlm.nih.gov/XXXXX/)"

    Returns the number of links applied.
    """
    content = file_path.read_text(encoding="utf-8")
    applied = 0

    conf_levels = {"high": 3, "medium": 2, "low": 1, "any": 0}
    min_level = conf_levels.get(min_confidence, 3)

    for link in links:
        if not link.get("pmid"):
            continue

        link_conf = conf_levels.get(link.get("confidence", "none"), -1)
        if link_conf < min_level:
            continue

        source = link["source_text"]
        pmid = link["pmid"]
        url = "https://pubmed.ncbi.nlm.nih.gov/{}/".format(pmid)

        # Build the linked version
        linked = "[{}]({})".format(source, url)

        # Only replace if the source text appears without already being linked
        # Make sure we don't double-link (check it's not already inside [...](...)  )
        # Use a negative lookbehind for [ and negative lookahead for ](
        pattern = re.compile(
            r'(?<!\[)' + re.escape(source) + r'(?!\]\()',
        )

        new_content = pattern.sub(linked, content, count=1)
        if new_content != content:
            content = new_content
            applied += 1

    if applied > 0:
        file_path.write_text(content, encoding="utf-8")

    return applied


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def process_plan(file_path: Path, cache: dict = None,
                 quiet: bool = False) -> list[dict]:
    """
    Process a single plan: extract unlinked citations, classify, search PubMed.
    Returns a list of search results.
    """
    unlinked = extract_unlinked_citations(file_path)
    if not unlinked:
        return []

    # Extract plan topic from filename (e.g., "chronic-migraine" → "chronic migraine")
    plan_topic = file_path.stem  # e.g. "chronic-migraine", "bacterial-meningitis"

    results = []
    # De-duplicate by source_text
    seen = set()

    for item in unlinked:
        source = item["source_text"].strip()
        if source in seen:
            continue
        seen.add(source)

        category = classify_citation(source)
        if category == "skip":
            continue

        # Evidence context from the same table row
        evidence = item.get("evidence", "")

        if not quiet:
            print("    {} [{}]: {}".format(
                category.upper().ljust(10), source[:60],
                "searching..." if category != "skip" else "skipped"))

        try:
            if category == "author":
                result = search_for_author_citation(
                    source, cache, evidence_context=evidence, plan_topic=plan_topic)
            elif category == "guideline":
                result = search_for_guideline(
                    source, cache, evidence_context=evidence, plan_topic=plan_topic)
            elif category == "trial":
                result = search_for_trial(
                    source, cache, evidence_context=evidence, plan_topic=plan_topic)
            else:
                continue

            result["category"] = category
            results.append(result)

            if not quiet and result.get("pmid"):
                conf = result.get("confidence", "none")
                print("      → PMID {} ({}) - {}".format(
                    result["pmid"], conf,
                    result.get("pubmed_title", "")[:70]))
            elif not quiet:
                print("      → not found ({})".format(result.get("method", "")))

        except Exception as e:
            if not quiet:
                print("      → ERROR: {}".format(e))
            results.append({
                "source_text": source,
                "pmid": None,
                "confidence": "none",
                "method": "error",
                "error": str(e),
                "category": category,
            })

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Link unlinked citations in neuro-plans evidence tables.")
    parser.add_argument("files", nargs="*", help="Plan markdown files to process")
    parser.add_argument("--all", action="store_true",
                        help="Process all plans in docs/plans/")
    parser.add_argument("--apply", action="store_true",
                        help="Apply found links to markdown files")
    parser.add_argument("--confidence", default="high",
                        choices=["high", "medium", "low", "any"],
                        help="Minimum confidence for --apply (default: high)")
    parser.add_argument("--json", dest="json_file",
                        help="Write results to JSON file")
    parser.add_argument("--quiet", action="store_true",
                        help="Suppress per-citation output")
    parser.add_argument("--batch", help="Process only plans N-M (e.g., 1-15)")
    parser.add_argument("--cache", action="store_true", default=True,
                        help="Use PMID cache (default: on)")
    parser.add_argument("--no-cache", action="store_true",
                        help="Disable PMID cache")

    args = parser.parse_args()

    # Collect files
    if args.all:
        plans_dir = Path("docs/plans")
        files = sorted(plans_dir.glob("*.md"))
    elif args.files:
        files = [Path(f) for f in args.files]
    else:
        parser.error("Provide plan files or use --all")

    # Apply batch filter
    if args.batch:
        try:
            start, end = args.batch.split("-")
            start, end = int(start), int(end)
            files = files[start - 1:end]  # 1-indexed
        except ValueError:
            parser.error("--batch must be N-M (e.g., 1-15)")

    if not files:
        print("No plan files found.", file=sys.stderr)
        sys.exit(1)

    # Load cache
    cache = None
    if args.cache and not args.no_cache:
        cache = load_cache()
        print("Loaded PMID cache: {} entries".format(len(cache.get("pmids", {}))))

    # API connectivity check
    print("Checking PubMed API connectivity...")
    if not check_api_connectivity():
        print("ERROR: Cannot reach PubMed API. Check network.", file=sys.stderr)
        sys.exit(1)
    print("API OK.\n")

    # Process plans
    all_results = {}
    total_searched = 0
    total_found = 0
    total_high = 0
    total_medium = 0
    total_skipped = 0
    total_applied = 0

    for i, fpath in enumerate(files, 1):
        plan_name = fpath.stem
        print("[{}/{}] {}...".format(i, len(files), plan_name))

        try:
            results = process_plan(fpath, cache=cache, quiet=args.quiet)
        except APIError as e:
            print("  API ERROR: {} — stopping batch".format(e), file=sys.stderr)
            # Save what we have so far
            break

        if not results:
            if not args.quiet:
                print("  (no searchable unlinked citations)")
            continue

        all_results[plan_name] = results

        # Count results
        for r in results:
            total_searched += 1
            if r.get("pmid"):
                total_found += 1
                if r["confidence"] == "high":
                    total_high += 1
                elif r["confidence"] == "medium":
                    total_medium += 1

        # Apply links if requested
        if args.apply:
            links_to_apply = [r for r in results if r.get("pmid")]
            if links_to_apply:
                n_applied = apply_links_to_file(fpath, links_to_apply,
                                                min_confidence=args.confidence)
                total_applied += n_applied
                if not args.quiet and n_applied:
                    print("  → Applied {} links".format(n_applied))

    # Save cache
    if cache:
        save_cache(cache)
        print("\nCache saved.")

    # Summary
    print("\n" + "=" * 60)
    print("LINKING SUMMARY")
    print("=" * 60)
    print("Plans processed:  {}".format(len(files)))
    print("Citations searched: {}".format(total_searched))
    print("PubMed links found: {} ({:.0f}%)".format(
        total_found,
        100 * total_found / total_searched if total_searched else 0))
    print("  High confidence:  {}".format(total_high))
    print("  Medium confidence: {}".format(total_medium))
    print("  Low / none:       {}".format(total_searched - total_found))
    if args.apply:
        print("Links applied:      {}".format(total_applied))
    print("=" * 60)

    # Write JSON report
    if args.json_file:
        report = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "plans_processed": len(files),
            "citations_searched": total_searched,
            "found": total_found,
            "high_confidence": total_high,
            "medium_confidence": total_medium,
            "applied": total_applied if args.apply else None,
            "min_confidence": args.confidence if args.apply else None,
            "plans": {},
        }

        for plan_name, results in all_results.items():
            report["plans"][plan_name] = []
            for r in results:
                entry = {
                    "source_text": r.get("source_text", ""),
                    "category": r.get("category", ""),
                    "pmid": r.get("pmid"),
                    "confidence": r.get("confidence", "none"),
                    "method": r.get("method", ""),
                }
                if r.get("pmid"):
                    entry["pubmed_title"] = r.get("pubmed_title", "")
                    entry["pubmed_author"] = r.get("pubmed_author", "")
                    entry["pubmed_journal"] = r.get("pubmed_journal", "")
                    entry["pubmed_year"] = r.get("pubmed_year", "")
                if r.get("score"):
                    entry["score"] = r["score"]
                if r.get("error"):
                    entry["error"] = r["error"]
                report["plans"][plan_name].append(entry)

        json_path = Path(args.json_file)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False),
                             encoding="utf-8")
        print("\nReport written to: {}".format(args.json_file))


if __name__ == "__main__":
    main()
