#!/usr/bin/env python3
"""
Validate and clean enriched PubMed citations in plans.json.

Strategy: "reject the clearly wrong" rather than "prove the match is right."

Since this is a neurology reference app, most enriched citations SHOULD be
about neurological topics. The enrichment script matched on author + journal
+ year, which is usually right. The failures we want to catch are where PubMed
returned an article about a completely different field (cancer, botany,
dermatology, etc.) — those are the hallucinated matches.

So we:
1. Fetch the actual PubMed article title for each PMID
2. Check if the article is plausibly neurological/medical
3. ONLY reject articles that are clearly about an unrelated field
4. For rejected ones, optionally re-search with title-first validation

Usage:
    python scripts/validate_enriched_citations.py --check              # Report only
    python scripts/validate_enriched_citations.py --clean              # Remove bad links
    python scripts/validate_enriched_citations.py --clean --re-enrich  # Remove bad + re-search
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
# Config
# ---------------------------------------------------------------------------

PLANS_JSON = Path("ios/NeuroPlans/NeuroPlans/Resources/plans.json")
DOCS_JSON = Path("docs/data/plans.json")
ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
API_PARAMS = {"tool": "neuro-plans-validator", "email": "neuro-plans@example.com"}
RATE_LIMIT = 0.35

MD_LINK = re.compile(r'\[([^\]]+)\]\((https?://pubmed\.ncbi\.nlm\.nih\.gov/(\d+)/?)\)')


def _strip_diacritics(text):
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in nfkd if not unicodedata.combining(ch))


def _normalize(text):
    t = _strip_diacritics(text).lower()
    t = re.sub(r'[^a-z0-9\s]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def _api_get(url, params):
    all_params = {**API_PARAMS, **params}
    query = "&".join(f"{k}={urllib.request.quote(str(v))}" for k, v in all_params.items())
    full_url = f"{url}?{query}"
    for attempt in range(3):
        try:
            req = urllib.request.Request(full_url, headers={"Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            if attempt < 2:
                time.sleep(2 ** (attempt + 1))
            else:
                print(f"  API error: {e}", file=sys.stderr)
    return {}


# ---------------------------------------------------------------------------
# Negative-filter validation: is the article clearly NOT neurological?
# ---------------------------------------------------------------------------

# Neurology / neuroscience terms — if the article contains any of these
# in its title, it's almost certainly a valid match for a neurology app.
NEURO_TERMS = [
    # Anatomy & physiology
    "brain", "cerebr", "cortex", "cortical", "hippocampal", "hippocampus",
    "thalamic", "thalamus", "basal ganglia", "striatum", "striatal",
    "cerebellum", "cerebellar", "brainstem", "spinal cord", "spinal",
    "cranial nerve", "nerve", "neural", "neuron", "neuronal",
    "axon", "axonal", "myelin", "demyelinat", "synap",
    "meninges", "meningeal", "dura", "dural",
    "blood brain barrier", "bbb",
    # Conditions
    "stroke", "ischemic stroke", "hemorrhagic stroke", "cerebrovascular",
    "transient ischemic", "tia",
    "epilepsy", "seizure", "convuls", "status epilepticus",
    "parkinson", "alzheimer", "dementia", "cognitive",
    "multiple sclerosis", "neuromyelitis", "optic neuritis",
    "migraine", "headache", "cluster headache", "cephalgia",
    "neuropathy", "polyneuropathy", "mononeuropathy",
    "guillain barre", "guillain-barre", "myasthenia",
    "amyotrophic lateral sclerosis", "als", "motor neuron",
    "huntington", "chorea", "dystonia", "tremor", "ataxia",
    "meningitis", "encephalitis", "encephalopathy",
    "concussion", "traumatic brain", "tbi",
    "intracranial", "hydrocephalus", "brain death",
    "neuralgia", "trigeminal", "bell palsy", "facial palsy",
    "radiculopathy", "myelopathy", "plexopathy",
    "myopathy", "muscular dystrophy", "myositis", "myotonic",
    "neurodegen", "prion", "creutzfeldt",
    "vertigo", "dizziness", "nystagmus", "vestibular",
    "narcolepsy", "sleep disorder", "insomnia", "restless leg",
    "neurocysticercosis", "brain abscess",
    "tourette", "tics",
    "wilson disease", "wilson's disease",
    "subarachnoid", "subdural", "epidural hematoma",
    "aneurysm", "arteriovenous malformation", "avm",
    "cavernous malformation", "cavernoma",
    "brain tumor", "glioma", "glioblastoma", "meningioma",
    "neuro oncol", "neurooncol",
    # Procedures & diagnostics
    "lumbar puncture", "cerebrospinal fluid", "csf",
    "electroencephalog", "eeg", "emg", "electromyogr",
    "nerve conduction", "evoked potential",
    "mri brain", "ct brain", "neuroimaging",
    "thrombolysis", "thrombectomy", "mechanical thrombectomy",
    "craniotomy", "craniectomy", "shunt",
    "deep brain stimulation", "dbs", "vagus nerve stimulation", "vns",
    # Drugs commonly used in neurology
    "antiepileptic", "anticonvulsant", "antiseizure",
    "levetiracetam", "valproate", "valproic acid", "carbamazepine",
    "lamotrigine", "phenytoin", "topiramate", "lacosamide",
    "oxcarbazepine", "gabapentin", "pregabalin",
    "zonisamide", "clobazam", "brivaracetam", "perampanel",
    "levodopa", "carbidopa", "dopamine agonist",
    "pramipexole", "ropinirole", "entacapone", "rasagiline", "selegiline",
    "amantadine", "trihexyphenidyl",
    "donepezil", "rivastigmine", "galantamine", "memantine",
    "interferon beta", "glatiramer", "natalizumab", "fingolimod",
    "dimethyl fumarate", "teriflunomide", "ocrelizumab", "rituximab",
    "siponimod", "ofatumumab", "cladribine",
    "sumatriptan", "rizatriptan", "zolmitriptan", "eletriptan",
    "erenumab", "fremanezumab", "galcanezumab", "eptinezumab",
    "botulinum toxin", "botox", "onabotulinum",
    "alteplase", "tenecteplase", "tissue plasminogen activator", "tpa",
    "nimodipine", "mannitol", "hypertonic saline",
    "pyridostigmine", "edrophonium",
    "riluzole", "edaravone",
    "intravenous immunoglobulin", "ivig", "plasmapheresis",
    # Clinical concepts used in neurology literature
    "nihss", "glasgow coma", "gcs", "mmse", "moca",
    "modified rankin", "mrs", "barthel",
    "disability", "neurologic", "neurological",
    "consciousness", "coma", "stupor",
    "aphasia", "dysarthria", "dysphagia", "dysphonia",
    "hemiparesis", "hemiplegia", "paraparesis", "paraplegia",
    "quadriparesis", "quadriplegia", "tetraplegia",
    "paresthesia", "numbness", "weakness",
    "gait", "balance", "coordination",
    "cognitive decline", "memory loss", "amnesia",
    "pupil", "papilledema", "optic disc",
    # Trial design terms that are valid in context
    "neuroprotect", "neurorehabilit",
    # Imaging & diagnostics
    "diffusion weighted", "dwi", "perfusion", "angiography",
    "carotid", "vertebrobasilar",
    "transcranial doppler", "tcd",
    # Commonly comorbid — valid in neuro context
    "mortality", "death",
    "hypertens", "blood pressure",  # stroke risk factor
    "anticoagul", "antithrombo", "antiplatelet",  # stroke prevention
    "atrial fibrillation",  # stroke cause
    "diabetes",  # neuropathy cause
    "renal", "kidney",  # drug dosing
]

# Non-neurological topics — if the article title matches ONLY these
# and NONE of the neuro terms, it's almost certainly a wrong match.
NON_NEURO_TOPICS = [
    # Oncology (non-neuro)
    "cancer", "oncolog", "tumor", "tumour", "neoplasm", "carcinoma",
    "lymphoma", "leukemia", "leukaemia", "melanoma", "sarcoma",
    "metasta", "chemotherap", "radiation therapy", "immunotherapy",
    "myeloma",
    # Basic science / molecular biology (not clinical neurology)
    "cell state", "phenotypic switch", "gene expression", "transcriptom",
    "proteom", "genomic", "epigenom", "single cell", "single-cell",
    "signaling pathway", "phosphorylat", "methylat",
    "stem cell", "progenitor cell", "cell culture",
    "smooth muscle phenoty",
    # Cardiology (non-stroke)
    "heart failure", "cardiomyopath", "coronary artery",
    "myocardial infarction", "angina", "valvul", "valve replacement",
    "cardiac surgery", "bypass graft", "cabg",
    "pacemaker", "pacing", "defibrillat",
    "ejection fraction", "lvef",
    "echocardiog",
    # Dermatology
    "dermatol", "psoriasis", "eczema", "rash", "skin lesion",
    "melanocyte", "keratinocyte",
    # Orthopedics
    "joint replacement", "arthroplasty", "meniscus",
    "rotator cuff", "ligament reconstruction",
    # Ophthalmology (non-neuro-ophthal)
    "cataract", "macular degeneration", "glaucoma",
    "intraocular", "phacoemulsification",
    # Obstetrics/Gynecology
    "obstetric", "pregnan", "cesarean", "neonatal",
    "cervical", "uterine", "ovarian",
    "breastfeed", "lactation",
    # Gastroenterology
    "colonoscop", "endoscop gastro", "crohn", "colitis",
    "celiac", "gastroparesis",
    # Urology
    "prostate", "urolog", "bladder", "renal cell",
    # Dental
    "dental", "oral surgery", "periodontal", "orthodontic",
    # Veterinary / agricultural
    "veterinar", "animal model", "canine", "bovine", "porcine model",
    "plant", "botanical", "agricultur", "crop", "pollinator",
    "flower", "seed", "germination",
    # Non-medical
    "political", "econom", "sociolog", "anthropolog",
    "climate", "environmental", "ecolog",
    # Foreign-language articles that slipped through
    "recherche de l", "anemie", "manifestant",
    # Miscellaneous clearly wrong matches
    "smooth muscle cell phenotypic",
]

# Neuro-adjacent topics — these might be legitimate in a neurology context
# (e.g., psychiatry overlaps with neurology, pain management, ICU care).
NEURO_ADJACENT = [
    "psychiatr", "depression", "anxiety", "psychosis",
    "schizophren", "bipolar",
    "pain", "analges", "opioid",
    "critical care", "intensive care", "icu",
    "pneumonia", "sepsis",
    "anemia", "iron", "hemoglobin",
    "rehabilitation", "physical therapy", "occupational therapy",
    "quality of life",
    "elderly", "geriatric", "frailty",
    "pediatric", "child",
    "exercise", "physical activity",
    "smoking", "tobacco",
    "alcohol",
    "antibiotic", "infection",
    "immune", "immunosuppress",
    "cardiac", "heart",  # can overlap with stroke/AF
    "vascular", "arteri",  # overlap with cerebrovascular
]


def is_clearly_wrong(article_title, citation_text="", plan_topic=""):
    """
    Return (is_wrong, reason) — True if the article is clearly NOT
    about a neurological / neuroscience topic.

    Conservative: only rejects articles with strong non-neuro signals
    AND no neuro signals. If uncertain, returns False (assumed valid).

    If plan_topic is provided, cardiovascular terms are treated as valid when
    the plan itself is cardiovascular (e.g., stroke, AF-related).
    """
    if not article_title:
        return True, "No title"

    tn = _normalize(article_title)
    cn = _normalize(citation_text) if citation_text else ""

    # If the plan itself is cardiovascular, cardiology articles are valid matches.
    _CARDIO_PLAN_KEYWORDS = {
        "stroke", "tia", "ich", "sah", "cerebrovascular",
        "atrial-fibrillation", "anticoagul", "carotid",
        "cardiac-arrest", "syncope", "hypertens",
        "pots", "dysautonomia", "autonomic",
    }
    _CARDIO_NON_NEURO_TERMS = {
        "heart failure", "cardiomyopath", "coronary artery",
        "myocardial infarction", "angina", "valvul", "valve replacement",
        "cardiac surgery", "bypass graft", "cabg",
        "pacemaker", "pacing", "defibrillat",
        "ejection fraction", "lvef",
        "echocardiog",
    }
    plan_is_cardio = False
    if plan_topic:
        pt_lower = plan_topic.lower().replace(" ", "-")
        plan_is_cardio = any(kw in pt_lower for kw in _CARDIO_PLAN_KEYWORDS)

    # If the plan is neuro-oncology, oncology articles are valid matches.
    _NEUROONCOLOGY_PLAN_KEYWORDS = {
        "brain-metastas", "metastatic", "leptomeningeal",
        "glioma", "glioblastoma", "meningioma",
        "spinal-cord-compression-malignant", "cns-lymphoma",
        "brain-tumor", "neuro-oncol", "neurooncol",
        "carcinomatosis", "malignant",
    }
    _ONCOLOGY_NON_NEURO_TERMS = {
        "cancer", "oncolog", "tumor", "tumour", "neoplasm", "carcinoma",
        "lymphoma", "leukemia", "leukaemia", "melanoma", "sarcoma",
        "metasta", "chemotherap", "radiation therapy", "immunotherapy",
        "myeloma",
    }
    plan_is_neurooncology = False
    if plan_topic:
        pt_lower = plan_topic.lower().replace(" ", "-")
        plan_is_neurooncology = any(kw in pt_lower for kw in _NEUROONCOLOGY_PLAN_KEYWORDS)

    def _word_match(term, text):
        """Check if term appears in text as a word/phrase, not as a substring
        of a larger word. E.g., 'dental' should NOT match 'nonaccidental'."""
        if " " in term:
            return term in text
        pattern = r'(?:^|[\s/\-])' + re.escape(term)
        return bool(re.search(pattern, text))

    # Check for neurological terms in the article title
    has_neuro = False
    for term in NEURO_TERMS:
        if _word_match(term, tn):
            has_neuro = True
            break

    # Even if neuro-related, check for clinical vs basic-science mismatch.
    CLINICAL_CITATION_MARKERS = [
        "guideline", "consensus", "statement", "recommendation",
        "focused update", "expert",
    ]
    BASIC_SCIENCE_MARKERS = [
        "single cell", "single-cell", "genomics", "transcriptom",
        "proteom", "phenotypic switch", "cell state", "cell fate",
        "gene expression", "signaling pathway", "phosphorylat",
        "epigenom", "chromatin", "histone", "mirna", "lncrna",
        "in vitro", "in vivo", "mouse model", "murine",
        "cell culture", "differentiat",
    ]

    citation_is_clinical = any(m in cn for m in CLINICAL_CITATION_MARKERS)
    article_is_basic_science = any(_word_match(m, tn) for m in BASIC_SCIENCE_MARKERS)

    if has_neuro and citation_is_clinical and article_is_basic_science:
        return True, "Clinical citation → basic science article"

    # If the article has a clear neurological term, it's valid
    if has_neuro:
        return False, "Neurological topic"

    # Check for neuro-adjacent terms (might still be valid)
    has_adjacent = False
    for term in NEURO_ADJACENT:
        if _word_match(term, tn):
            has_adjacent = True
            break

    # Check for non-neuro signals (skip cardio/onc terms when plan is relevant)
    non_neuro_matches = []
    for term in NON_NEURO_TOPICS:
        if plan_is_cardio and term in _CARDIO_NON_NEURO_TERMS:
            continue
        if plan_is_neurooncology and term in _ONCOLOGY_NON_NEURO_TERMS:
            continue
        if _word_match(term, tn):
            non_neuro_matches.append(term)

    # Clear non-neuro topic with no neuro or adjacent signals = WRONG
    if non_neuro_matches and not has_adjacent:
        return True, f"Non-neuro topic ({non_neuro_matches[0]})"

    # Non-neuro with adjacent is borderline — check if citation context helps
    if non_neuro_matches and has_adjacent:
        for term in NEURO_ADJACENT:
            if term in tn and term in cn:
                return False, "Adjacent topic match"
        return True, f"Non-neuro despite adjacent ({non_neuro_matches[0]})"

    # No neuro terms AND no non-neuro terms — could be generic medical
    # article. Check if there's any word overlap with citation.
    c_words = set(w for w in cn.split() if len(w) >= 5)
    t_words = set(w for w in tn.split() if len(w) >= 5)
    shared = c_words & t_words
    if len(shared) >= 2:
        return False, f"Word overlap ({len(shared)} words)"

    # Check if the article title looks like it's in a foreign language
    foreign_indicators = ["le ", "la ", "les ", "des ", "une ", "del ", "der ",
                          "die ", "das ", "los ", "las ", "gli ", "degli "]
    for indicator in foreign_indicators:
        if tn.startswith(indicator) or f" {indicator}" in tn:
            return True, "Foreign language article"

    # No strong signal either way — assume valid (conservative approach)
    return False, "No strong signal (assumed valid)"


# ---------------------------------------------------------------------------
# Batch metadata fetch
# ---------------------------------------------------------------------------

def batch_fetch_metadata(pmids, cache):
    uncached = [p for p in pmids if p not in cache]
    if not uncached:
        return
    batch_size = 200
    for i in range(0, len(uncached), batch_size):
        batch = uncached[i:i + batch_size]
        time.sleep(RATE_LIMIT)
        data = _api_get(ESUMMARY_URL, {
            "db": "pubmed", "id": ",".join(batch), "retmode": "json"
        })
        result_data = data.get("result", {})
        for pmid in batch:
            record = result_data.get(pmid, {})
            if "error" in record or not record:
                cache[pmid] = None
            else:
                authors = [a.get("name", "") for a in record.get("authors", [])]
                cache[pmid] = {
                    "title": record.get("title", ""),
                    "first_author": authors[0] if authors else "",
                    "authors": authors,
                    "journal": record.get("fulljournalname", ""),
                    "journal_abbrev": record.get("source", ""),
                    "year": record.get("pubdate", "")[:4],
                }
        if i + batch_size < len(uncached):
            print(f"    Fetched {min(i + batch_size, len(uncached))}/{len(uncached)}...",
                  flush=True)


# ---------------------------------------------------------------------------
# Re-enrichment with title-first search
# ---------------------------------------------------------------------------

JOURNAL_MAP = {
    "nejm": "N Engl J Med", "lancet": "Lancet", "jama": "JAMA",
    "lancet neurol": "Lancet Neurol", "lancet neurology": "Lancet Neurol",
    "jama neurol": "JAMA Neurol", "jama neurology": "JAMA Neurol",
    "ann neurol": "Ann Neurol", "annals of neurology": "Ann Neurol",
    "neurology": "Neurology",
    "stroke": "Stroke",
    "brain": "Brain",
    "epilepsia": "Epilepsia",
    "cephalalgia": "Cephalalgia",
    "j neurol neurosurg psychiatry": "J Neurol Neurosurg Psychiatry",
    "jnnp": "J Neurol Neurosurg Psychiatry",
    "neurocrit care": "Neurocrit Care",
    "j neurosurg": "J Neurosurg",
    "neurosurgery": "Neurosurgery",
    "j neurol sci": "J Neurol Sci",
    "arch neurol": "Arch Neurol",
    "front neurol": "Front Neurol",
    "nat rev neurol": "Nat Rev Neurol",
    "semin neurol": "Semin Neurol",
    "j clin neurosci": "J Clin Neurosci",
    "j neurol": "J Neurol",
    "eur j neurol": "Eur J Neurol",
    "clin neurophysiol": "Clin Neurophysiol",
    "neurol clin": "Neurol Clin",
    "mov disord": "Mov Disord",
    "parkinsonism relat disord": "Parkinsonism Relat Disord",
    "mult scler": "Mult Scler",
    "j headache pain": "J Headache Pain",
    "headache": "Headache",
    "chest": "Chest",
    "crit care med": "Crit Care Med",
    "intensive care med": "Intensive Care Med",
    "blood": "Blood", "bmj": "BMJ",
    "ann intern med": "Ann Intern Med",
    "circulation": "Circulation",
    "n engl j med": "N Engl J Med",
    "new engl j med": "N Engl J Med",
    "mayo clin proc": "Mayo Clin Proc",
    "cns drugs": "CNS Drugs",
    "drugs": "Drugs",
    "expert rev neurother": "Expert Rev Neurother",
    "continuum": "Continuum (Minneap Minn)",
    "pract neurol": "Pract Neurol",
    "curr opin neurol": "Curr Opin Neurol",
}


def _parse_citation(text):
    result = {"author": "", "journal": "", "year": "", "title_words": ""}
    years = re.findall(r'\b((?:19|20)\d{2})\b', text)
    if years:
        result["year"] = years[-1]

    paren = re.search(
        r'\(([A-Z][a-zA-Zéèêëàâäùûüïîôöç\'\- ]+?)\s+et\s+al\.?\s*[.,]?\s*'
        r'([A-Za-z][A-Za-z .]+?)\s+((?:19|20)\d{2})',
        text
    )
    if paren:
        result["author"] = paren.group(1).strip().rstrip(',')
        result["journal"] = paren.group(2).strip().rstrip('.')
        result["year"] = paren.group(3)
    else:
        paren_auth = re.search(r'\(([A-Z][a-zA-Zéèêëàâäùûüïîôöç\'\-]+)\s+et\s+al\.?\)', text)
        if paren_auth:
            result["author"] = paren_auth.group(1).strip()

    # Build title search terms from the citation
    clean = text
    clean = re.sub(r'\([^)]*et al[^)]*\)', '', clean)
    clean = re.sub(r'\([^)]*\d{4}[^)]*\)', '', clean)
    clean = re.sub(r'\b(?:Guidelines?|Consensus|Statement|Update|Report)\b', '', clean, flags=re.I)
    words = [w for w in clean.split() if len(w) > 3 and not w.isdigit()
             and w.lower() not in ('trial', 'study', 'with', 'from', 'that', 'this',
                                    'were', 'been', 'have', 'also', 'expert')]
    if words:
        result["title_words"] = " ".join(words[:6])

    return result


def search_with_title_validation(citation_text, metadata_cache):
    """Search PubMed with title-first validation. Only accept results that
    pass the is_clearly_wrong check."""
    parsed = _parse_citation(citation_text)
    author = parsed["author"]
    journal = parsed["journal"]
    year = parsed["year"]
    title_words = parsed["title_words"]

    strategies = []

    if title_words and year:
        strategies.append(("title+year", "", "", year, title_words))
    if title_words and journal and year:
        resolved = JOURNAL_MAP.get(journal.lower().strip().rstrip('.'), journal)
        strategies.append(("title+journal+year", "", resolved, year, title_words))
    if author and journal and year:
        resolved = JOURNAL_MAP.get(journal.lower().strip().rstrip('.'), journal)
        strategies.append(("author+journal+year", author, resolved, year, ""))
    if author and year and title_words:
        strategies.append(("author+year+title", author, "", year, title_words[:30]))
    if title_words:
        strategies.append(("title_only", "", "", "", title_words))

    for name, auth, jour, yr, tw in strategies:
        time.sleep(RATE_LIMIT)
        parts = []
        if auth:
            surname = _strip_diacritics(auth.split()[0]).rstrip(',')
            parts.append(f"{surname}[Author]")
        if jour:
            parts.append(f'"{jour}"[Journal]')
        if yr:
            parts.append(f"{yr}[Date - Publication]")
        if tw:
            parts.append(f"{tw}[Title]")
        if not parts:
            continue

        term = " AND ".join(parts)
        data = _api_get(ESEARCH_URL, {
            "db": "pubmed", "term": term, "retmax": "5", "retmode": "json"
        })
        pmids = data.get("esearchresult", {}).get("idlist", [])
        if not pmids:
            continue

        batch_fetch_metadata(pmids[:5], metadata_cache)

        for pmid in pmids[:5]:
            meta = metadata_cache.get(pmid)
            if not meta:
                continue
            wrong, reason = is_clearly_wrong(meta["title"], citation_text)
            if not wrong:
                return {"pmid": pmid, "metadata": meta, "strategy": name}

    return {"pmid": None, "metadata": None, "strategy": None}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Validate enriched PubMed citations")
    parser.add_argument("--check", action="store_true", help="Report bad links only")
    parser.add_argument("--clean", action="store_true", help="Remove bad links from JSON")
    parser.add_argument("--re-enrich", action="store_true",
                        help="After cleaning, re-search with title validation (implies --clean)")
    args = parser.parse_args()

    if args.re_enrich:
        args.clean = True

    if not any([args.check, args.clean]):
        parser.print_help()
        sys.exit(1)

    with open(PLANS_JSON) as f:
        plans = json.load(f)

    # Collect all linked citations
    linked = []
    for plan_id in sorted(plans.keys()):
        for i, ev in enumerate(plans[plan_id].get("evidence", [])):
            rec = ev.get("recommendation", "")
            m = MD_LINK.search(rec)
            if m:
                linked.append({
                    "plan_id": plan_id,
                    "index": i,
                    "citation": m.group(1),
                    "url": m.group(2),
                    "pmid": m.group(3),
                    "full_rec": rec,
                })

    print(f"\nFound {len(linked)} linked citations to validate\n")

    # Batch-fetch all metadata
    all_pmids = list(set(item["pmid"] for item in linked))
    metadata_cache = {}
    print(f"Fetching metadata for {len(all_pmids)} unique PMIDs...")
    batch_fetch_metadata(all_pmids, metadata_cache)
    print(f"  Done.\n")

    # Validate each
    valid_count = 0
    invalid_count = 0
    not_found_count = 0
    invalid_items = []

    for item in linked:
        meta = metadata_cache.get(item["pmid"])
        if meta is None:
            not_found_count += 1
            invalid_items.append({**item, "reason": "PMID not found"})
            continue

        wrong, reason = is_clearly_wrong(meta["title"], item["citation"],
                                         plan_topic=item["plan_id"])

        if not wrong:
            valid_count += 1
        else:
            invalid_count += 1
            invalid_items.append({
                **item,
                "reason": reason,
                "article_title": meta["title"][:120],
                "article_author": meta.get("first_author", "?"),
            })

    print(f"{'='*70}")
    print(f"  VALIDATION RESULTS")
    print(f"{'='*70}")
    print(f"  Valid:      {valid_count}")
    print(f"  Invalid:    {invalid_count}")
    print(f"  Not found:  {not_found_count}")
    print(f"  Total:      {len(linked)}")
    print(f"{'='*70}\n")

    if invalid_items:
        print(f"INVALID CITATIONS ({len(invalid_items)}):\n")
        for item in invalid_items[:100]:
            print(f"  [{item['plan_id']}] PMID {item['pmid']} — {item['reason']}")
            print(f"    Citation: {item['citation'][:100]}")
            if item.get('article_title'):
                print(f"    Actual:   {item['article_title'][:100]}")
            print()

        if len(invalid_items) > 100:
            print(f"  ... and {len(invalid_items) - 100} more\n")

    # Clean mode
    if args.clean and invalid_items:
        removed = 0
        re_enriched = 0

        for item in invalid_items:
            plan_id = item["plan_id"]
            idx = item["index"]
            evidence = plans[plan_id]["evidence"]
            rec = evidence[idx]["recommendation"]

            m = MD_LINK.search(rec)
            if m:
                plain_text = m.group(1)

                if args.re_enrich:
                    result = search_with_title_validation(plain_text, metadata_cache)
                    if result["pmid"]:
                        new_rec = f"[{plain_text}](https://pubmed.ncbi.nlm.nih.gov/{result['pmid']}/)"
                        evidence[idx]["recommendation"] = new_rec
                        re_enriched += 1
                        meta = result["metadata"]
                        print(f"  ✓ [{plan_id}] → PMID {result['pmid']} "
                              f"via {result['strategy']}: {meta['title'][:60]}")
                        continue

                evidence[idx]["recommendation"] = plain_text
                removed += 1

        print(f"\n{'='*70}")
        print(f"  CLEANUP RESULTS")
        print(f"{'='*70}")
        print(f"  Bad links removed:   {removed}")
        if args.re_enrich:
            print(f"  Re-enriched:         {re_enriched}")
        print(f"{'='*70}")

        with open(PLANS_JSON, "w", encoding="utf-8") as f:
            json.dump(plans, f, indent=2, ensure_ascii=False)
        print(f"\n  ✓ Written to {PLANS_JSON}")

        if DOCS_JSON.exists():
            with open(DOCS_JSON, "w", encoding="utf-8") as f:
                json.dump(plans, f, indent=2, ensure_ascii=False)
            print(f"  ✓ Written to {DOCS_JSON}")

        total = sum(
            1 for p in plans.values()
            for ev in p.get("evidence", [])
            if MD_LINK.search(ev.get("recommendation", ""))
        )
        total_all = sum(len(p.get("evidence", [])) for p in plans.values())
        print(f"\n  Final: {total}/{total_all} citations have verified PubMed links "
              f"({total/total_all*100:.1f}%)")


if __name__ == "__main__":
    main()
