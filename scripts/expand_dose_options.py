#!/usr/bin/env python3
"""Expand doseOptions for medications across all plan JSON files.

Converts single-option doseOptions arrays to include clinically appropriate
dose ranges (2-6 options per medication) for use in the Sevaro Clinical app
dropdown selector.

Format:
    {
        "doseOptions": [
            { "text": "30 mg daily", "orderSentence": "Duloxetine 30 mg PO daily" },
            { "text": "60 mg daily", "orderSentence": "Duloxetine 60 mg PO daily" },
            ...
        ]
    }
"""

import json
import re
import sys
from pathlib import Path

# Import the central medication resolver for fallback dose lookups
try:
    from medication_resolver import MedicationResolver
    _resolver = MedicationResolver()
    _resolver_available = True
except ImportError:
    _resolver = None
    _resolver_available = False

# ---------------------------------------------------------------------------
# Comprehensive Medication Dose Database
# Key: normalized medication name (lowercase)
# Value: list of dose option tuples (text, route, frequency)
# ---------------------------------------------------------------------------
MEDICATION_DOSES = {
    # ===== SNRIs / Antidepressants =====
    "duloxetine": [
        ("30 mg", "PO", "daily"),
        ("60 mg", "PO", "daily"),
        ("90 mg", "PO", "daily"),
        ("120 mg", "PO", "daily"),
    ],
    "venlafaxine": [
        ("37.5 mg", "PO", "daily"),
        ("75 mg", "PO", "daily"),
        ("150 mg", "PO", "daily"),
        ("225 mg", "PO", "daily"),
    ],
    "venlafaxine xr": [
        ("37.5 mg", "PO", "daily"),
        ("75 mg", "PO", "daily"),
        ("150 mg", "PO", "daily"),
        ("225 mg", "PO", "daily"),
    ],
    "milnacipran": [
        ("12.5 mg", "PO", "daily"),
        ("25 mg", "PO", "BID"),
        ("50 mg", "PO", "BID"),
        ("100 mg", "PO", "BID"),
    ],

    # ===== TCAs (Tricyclic Antidepressants) =====
    "amitriptyline": [
        ("10 mg", "PO", "QHS"),
        ("25 mg", "PO", "QHS"),
        ("50 mg", "PO", "QHS"),
        ("75 mg", "PO", "QHS"),
        ("100 mg", "PO", "QHS"),
    ],
    "nortriptyline": [
        ("10 mg", "PO", "QHS"),
        ("25 mg", "PO", "QHS"),
        ("50 mg", "PO", "QHS"),
        ("75 mg", "PO", "QHS"),
        ("100 mg", "PO", "QHS"),
    ],
    "desipramine": [
        ("25 mg", "PO", "QHS"),
        ("50 mg", "PO", "QHS"),
        ("75 mg", "PO", "QHS"),
        ("100 mg", "PO", "QHS"),
        ("150 mg", "PO", "QHS"),
    ],
    "imipramine": [
        ("10 mg", "PO", "QHS"),
        ("25 mg", "PO", "QHS"),
        ("50 mg", "PO", "QHS"),
        ("75 mg", "PO", "QHS"),
    ],

    # ===== Gabapentinoids =====
    "gabapentin": [
        ("100 mg", "PO", "TID"),
        ("300 mg", "PO", "TID"),
        ("600 mg", "PO", "TID"),
        ("900 mg", "PO", "TID"),
        ("1200 mg", "PO", "TID"),
    ],
    "pregabalin": [
        ("50 mg", "PO", "TID"),
        ("75 mg", "PO", "BID"),
        ("100 mg", "PO", "TID"),
        ("150 mg", "PO", "BID"),
        ("200 mg", "PO", "BID"),
        ("300 mg", "PO", "BID"),
    ],

    # ===== Anti-epileptics =====
    "carbamazepine": [
        ("100 mg", "PO", "BID"),
        ("200 mg", "PO", "BID"),
        ("400 mg", "PO", "BID"),
        ("600 mg", "PO", "BID"),
    ],
    "oxcarbazepine": [
        ("150 mg", "PO", "BID"),
        ("300 mg", "PO", "BID"),
        ("600 mg", "PO", "BID"),
        ("900 mg", "PO", "BID"),
        ("1200 mg", "PO", "BID"),
    ],
    "lamotrigine": [
        ("25 mg", "PO", "daily"),
        ("50 mg", "PO", "daily"),
        ("100 mg", "PO", "daily"),
        ("200 mg", "PO", "daily"),
        ("400 mg", "PO", "daily"),
    ],
    "lacosamide": [
        ("50 mg", "PO", "BID"),
        ("100 mg", "PO", "BID"),
        ("150 mg", "PO", "BID"),
        ("200 mg", "PO", "BID"),
    ],
    "topiramate": [
        ("25 mg", "PO", "BID"),
        ("50 mg", "PO", "BID"),
        ("100 mg", "PO", "BID"),
        ("150 mg", "PO", "BID"),
        ("200 mg", "PO", "BID"),
    ],
    "valproic acid": [
        ("250 mg", "PO", "BID"),
        ("500 mg", "PO", "BID"),
        ("750 mg", "PO", "BID"),
        ("1000 mg", "PO", "BID"),
    ],
    "valproate": [
        ("250 mg", "PO", "BID"),
        ("500 mg", "PO", "BID"),
        ("750 mg", "PO", "BID"),
        ("1000 mg", "PO", "BID"),
    ],
    "levetiracetam": [
        ("250 mg", "PO", "BID"),
        ("500 mg", "PO", "BID"),
        ("750 mg", "PO", "BID"),
        ("1000 mg", "PO", "BID"),
        ("1500 mg", "PO", "BID"),
    ],
    "phenytoin": [
        ("100 mg", "PO", "TID"),
        ("200 mg", "PO", "BID"),
        ("300 mg", "PO", "daily"),
        ("400 mg", "PO", "daily"),
    ],
    "zonisamide": [
        ("100 mg", "PO", "daily"),
        ("200 mg", "PO", "daily"),
        ("300 mg", "PO", "daily"),
        ("400 mg", "PO", "daily"),
    ],
    "clobazam": [
        ("5 mg", "PO", "BID"),
        ("10 mg", "PO", "BID"),
        ("20 mg", "PO", "BID"),
    ],
    "clonazepam": [
        ("0.25 mg", "PO", "BID"),
        ("0.5 mg", "PO", "BID"),
        ("1 mg", "PO", "BID"),
        ("2 mg", "PO", "BID"),
    ],
    "brivaracetam": [
        ("25 mg", "PO", "BID"),
        ("50 mg", "PO", "BID"),
        ("75 mg", "PO", "BID"),
        ("100 mg", "PO", "BID"),
    ],
    "perampanel": [
        ("2 mg", "PO", "QHS"),
        ("4 mg", "PO", "QHS"),
        ("8 mg", "PO", "QHS"),
        ("12 mg", "PO", "QHS"),
    ],
    "cenobamate": [
        ("12.5 mg", "PO", "daily"),
        ("25 mg", "PO", "daily"),
        ("50 mg", "PO", "daily"),
        ("100 mg", "PO", "daily"),
        ("200 mg", "PO", "daily"),
    ],
    "primidone": [
        ("12.5 mg", "PO", "QHS"),
        ("25 mg", "PO", "QHS"),
        ("50 mg", "PO", "BID"),
        ("125 mg", "PO", "BID"),
        ("250 mg", "PO", "BID"),
    ],

    # ===== Benzodiazepines =====
    "lorazepam": [
        ("0.5 mg", "PO", "TID"),
        ("1 mg", "PO", "TID"),
        ("2 mg", "PO", "TID"),
    ],
    "diazepam": [
        ("2 mg", "PO", "TID"),
        ("5 mg", "PO", "TID"),
        ("10 mg", "PO", "TID"),
    ],
    "alprazolam": [
        ("0.25 mg", "PO", "TID"),
        ("0.5 mg", "PO", "TID"),
        ("1 mg", "PO", "TID"),
    ],
    "midazolam": [
        ("2 mg", "IV", "once"),
        ("5 mg", "IV", "once"),
        ("10 mg", "IV", "once"),
    ],

    # ===== Beta-blockers =====
    "propranolol": [
        ("20 mg", "PO", "BID"),
        ("40 mg", "PO", "BID"),
        ("60 mg", "PO", "TID"),
        ("80 mg", "PO", "TID"),
    ],
    "propranolol la": [
        ("60 mg", "PO", "daily"),
        ("80 mg", "PO", "daily"),
        ("120 mg", "PO", "daily"),
        ("160 mg", "PO", "daily"),
    ],
    "atenolol": [
        ("25 mg", "PO", "daily"),
        ("50 mg", "PO", "daily"),
        ("100 mg", "PO", "daily"),
    ],
    "metoprolol": [
        ("25 mg", "PO", "BID"),
        ("50 mg", "PO", "BID"),
        ("100 mg", "PO", "BID"),
    ],
    "nadolol": [
        ("40 mg", "PO", "daily"),
        ("80 mg", "PO", "daily"),
        ("120 mg", "PO", "daily"),
        ("160 mg", "PO", "daily"),
    ],
    "timolol": [
        ("10 mg", "PO", "BID"),
        ("20 mg", "PO", "BID"),
    ],

    # ===== Calcium Channel Blockers =====
    "verapamil": [
        ("80 mg", "PO", "TID"),
        ("120 mg", "PO", "TID"),
        ("240 mg", "PO", "daily"),
        ("360 mg", "PO", "daily"),
        ("480 mg", "PO", "daily"),
    ],
    "flunarizine": [
        ("5 mg", "PO", "QHS"),
        ("10 mg", "PO", "QHS"),
    ],
    "nimodipine": [
        ("30 mg", "PO", "q4h"),
        ("60 mg", "PO", "q4h"),
    ],

    # ===== Triptans =====
    "sumatriptan": [
        ("25 mg", "PO", "PRN"),
        ("50 mg", "PO", "PRN"),
        ("100 mg", "PO", "PRN"),
        ("6 mg", "SC", "PRN"),
    ],
    "rizatriptan": [
        ("5 mg", "PO", "PRN"),
        ("10 mg", "PO", "PRN"),
    ],
    "zolmitriptan": [
        ("2.5 mg", "PO", "PRN"),
        ("5 mg", "PO", "PRN"),
    ],
    "eletriptan": [
        ("20 mg", "PO", "PRN"),
        ("40 mg", "PO", "PRN"),
        ("80 mg", "PO", "PRN"),
    ],
    "naratriptan": [
        ("1 mg", "PO", "PRN"),
        ("2.5 mg", "PO", "PRN"),
    ],
    "frovatriptan": [
        ("2.5 mg", "PO", "PRN"),
    ],
    "almotriptan": [
        ("6.25 mg", "PO", "PRN"),
        ("12.5 mg", "PO", "PRN"),
    ],

    # ===== CGRP Monoclonal Antibodies =====
    "erenumab": [
        ("70 mg", "SC", "monthly"),
        ("140 mg", "SC", "monthly"),
    ],
    "fremanezumab": [
        ("225 mg", "SC", "monthly"),
        ("675 mg", "SC", "quarterly"),
    ],
    "galcanezumab": [
        ("120 mg", "SC", "monthly"),
        ("240 mg", "SC", "loading dose"),
    ],
    "eptinezumab": [
        ("100 mg", "IV", "q3mo"),
        ("300 mg", "IV", "q3mo"),
    ],

    # ===== CGRP Receptor Antagonists (Gepants) =====
    "ubrogepant": [
        ("50 mg", "PO", "PRN"),
        ("100 mg", "PO", "PRN"),
    ],
    "rimegepant": [
        ("75 mg", "PO", "PRN"),
        ("75 mg", "PO", "every other day"),
    ],
    "atogepant": [
        ("10 mg", "PO", "daily"),
        ("30 mg", "PO", "daily"),
        ("60 mg", "PO", "daily"),
    ],

    # ===== Parkinson's Disease Medications =====
    "carbidopa-levodopa": [
        ("25/100 mg", "PO", "TID"),
        ("25/100 mg", "PO", "QID"),
        ("50/200 mg", "PO", "TID"),
        ("50/200 mg", "PO", "QID"),
    ],
    "pramipexole": [
        ("0.125 mg", "PO", "TID"),
        ("0.25 mg", "PO", "TID"),
        ("0.5 mg", "PO", "TID"),
        ("1 mg", "PO", "TID"),
        ("1.5 mg", "PO", "TID"),
    ],
    "ropinirole": [
        ("0.25 mg", "PO", "TID"),
        ("0.5 mg", "PO", "TID"),
        ("1 mg", "PO", "TID"),
        ("2 mg", "PO", "TID"),
        ("3 mg", "PO", "TID"),
    ],
    "rotigotine": [
        ("2 mg/24h", "TD", "daily"),
        ("4 mg/24h", "TD", "daily"),
        ("6 mg/24h", "TD", "daily"),
        ("8 mg/24h", "TD", "daily"),
    ],
    "selegiline": [
        ("5 mg", "PO", "BID"),
        ("10 mg", "PO", "daily"),
    ],
    "rasagiline": [
        ("0.5 mg", "PO", "daily"),
        ("1 mg", "PO", "daily"),
    ],
    "safinamide": [
        ("50 mg", "PO", "daily"),
        ("100 mg", "PO", "daily"),
    ],
    "entacapone": [
        ("200 mg", "PO", "with each L-dopa dose"),
    ],
    "amantadine": [
        ("100 mg", "PO", "daily"),
        ("100 mg", "PO", "BID"),
        ("200 mg", "PO", "BID"),
    ],
    "trihexyphenidyl": [
        ("1 mg", "PO", "TID"),
        ("2 mg", "PO", "TID"),
        ("5 mg", "PO", "TID"),
    ],
    "benztropine": [
        ("0.5 mg", "PO", "BID"),
        ("1 mg", "PO", "BID"),
        ("2 mg", "PO", "BID"),
    ],

    # ===== Multiple Sclerosis Treatments =====
    "interferon beta-1a": [
        ("30 mcg", "IM", "weekly"),
        ("22 mcg", "SC", "TIW"),
        ("44 mcg", "SC", "TIW"),
    ],
    "interferon beta-1b": [
        ("0.25 mg", "SC", "every other day"),
    ],
    "glatiramer acetate": [
        ("20 mg", "SC", "daily"),
        ("40 mg", "SC", "TIW"),
    ],
    "dimethyl fumarate": [
        ("120 mg", "PO", "BID"),
        ("240 mg", "PO", "BID"),
    ],
    "fingolimod": [
        ("0.5 mg", "PO", "daily"),
    ],
    "siponimod": [
        ("0.25 mg", "PO", "daily"),
        ("1 mg", "PO", "daily"),
        ("2 mg", "PO", "daily"),
    ],
    "ozanimod": [
        ("0.23 mg", "PO", "daily"),
        ("0.46 mg", "PO", "daily"),
        ("0.92 mg", "PO", "daily"),
    ],
    "teriflunomide": [
        ("7 mg", "PO", "daily"),
        ("14 mg", "PO", "daily"),
    ],
    "natalizumab": [
        ("300 mg", "IV", "q4wk"),
    ],
    "ocrelizumab": [
        ("300 mg", "IV", "q2wk x2 then q6mo"),
        ("600 mg", "IV", "q6mo"),
    ],
    "ofatumumab": [
        ("20 mg", "SC", "q4wk"),
    ],
    "alemtuzumab": [
        ("12 mg", "IV", "daily x5 then x3"),
    ],
    "cladribine": [
        ("3.5 mg/kg", "PO", "per course"),
    ],

    # ===== Myasthenia Gravis =====
    "pyridostigmine": [
        ("30 mg", "PO", "TID"),
        ("60 mg", "PO", "TID"),
        ("60 mg", "PO", "QID"),
        ("90 mg", "PO", "TID"),
        ("120 mg", "PO", "TID"),
    ],
    "mestinon": [
        ("30 mg", "PO", "TID"),
        ("60 mg", "PO", "TID"),
        ("60 mg", "PO", "QID"),
        ("90 mg", "PO", "TID"),
    ],
    "neostigmine": [
        ("15 mg", "PO", "q3-4h"),
        ("0.5 mg", "IV", "once"),
        ("1 mg", "IV", "once"),
    ],

    # ===== Steroids =====
    "prednisone": [
        ("5 mg", "PO", "daily"),
        ("10 mg", "PO", "daily"),
        ("20 mg", "PO", "daily"),
        ("40 mg", "PO", "daily"),
        ("60 mg", "PO", "daily"),
        ("1 mg/kg", "PO", "daily"),
    ],
    "methylprednisolone": [
        ("500 mg", "IV", "daily"),
        ("1000 mg", "IV", "daily"),
        ("1 g", "IV", "daily x3-5 days"),
    ],
    "dexamethasone": [
        ("4 mg", "IV", "q6h"),
        ("10 mg", "IV", "once then 4 mg q6h"),
        ("16 mg", "PO", "daily"),
    ],

    # ===== Immunosuppressants =====
    "azathioprine": [
        ("50 mg", "PO", "daily"),
        ("100 mg", "PO", "daily"),
        ("150 mg", "PO", "daily"),
        ("2-3 mg/kg", "PO", "daily"),
    ],
    "mycophenolate": [
        ("500 mg", "PO", "BID"),
        ("1000 mg", "PO", "BID"),
        ("1500 mg", "PO", "BID"),
    ],
    "mycophenolate mofetil": [
        ("500 mg", "PO", "BID"),
        ("1000 mg", "PO", "BID"),
        ("1500 mg", "PO", "BID"),
    ],
    "rituximab": [
        ("375 mg/m2", "IV", "weekly x4"),
        ("500 mg", "IV", "q6mo"),
        ("1000 mg", "IV", "q6mo"),
    ],
    "cyclophosphamide": [
        ("500 mg/m2", "IV", "monthly"),
        ("1000 mg/m2", "IV", "monthly"),
    ],
    "methotrexate": [
        ("7.5 mg", "PO", "weekly"),
        ("10 mg", "PO", "weekly"),
        ("15 mg", "PO", "weekly"),
        ("20 mg", "PO", "weekly"),
        ("25 mg", "SC", "weekly"),
    ],
    "tacrolimus": [
        ("1 mg", "PO", "BID"),
        ("2 mg", "PO", "BID"),
        ("3 mg", "PO", "BID"),
    ],
    "cyclosporine": [
        ("100 mg", "PO", "BID"),
        ("150 mg", "PO", "BID"),
        ("200 mg", "PO", "BID"),
    ],

    # ===== IVIG/Plasma Exchange =====
    "ivig": [
        ("0.4 g/kg", "IV", "daily x5 days"),
        ("1 g/kg", "IV", "daily x2 days"),
        ("2 g/kg", "IV", "divided over 2-5 days"),
    ],

    # ===== Muscle Relaxants =====
    "baclofen": [
        ("5 mg", "PO", "TID"),
        ("10 mg", "PO", "TID"),
        ("20 mg", "PO", "TID"),
        ("20 mg", "PO", "QID"),
    ],
    "tizanidine": [
        ("2 mg", "PO", "TID"),
        ("4 mg", "PO", "TID"),
        ("8 mg", "PO", "TID"),
    ],
    "cyclobenzaprine": [
        ("5 mg", "PO", "TID"),
        ("10 mg", "PO", "TID"),
    ],
    "dantrolene": [
        ("25 mg", "PO", "daily"),
        ("25 mg", "PO", "BID"),
        ("50 mg", "PO", "TID"),
        ("100 mg", "PO", "TID"),
    ],
    "methocarbamol": [
        ("500 mg", "PO", "QID"),
        ("750 mg", "PO", "QID"),
        ("1500 mg", "PO", "QID"),
    ],

    # ===== Pain Medications =====
    "tramadol": [
        ("50 mg", "PO", "q6h PRN"),
        ("100 mg", "PO", "q6h PRN"),
    ],
    "tapentadol": [
        ("50 mg", "PO", "q4-6h PRN"),
        ("100 mg", "PO", "q12h ER"),
        ("150 mg", "PO", "q12h ER"),
        ("200 mg", "PO", "q12h ER"),
    ],
    "tapentadol er": [
        ("50 mg", "PO", "BID"),
        ("100 mg", "PO", "BID"),
        ("150 mg", "PO", "BID"),
        ("200 mg", "PO", "BID"),
        ("250 mg", "PO", "BID"),
    ],
    "morphine": [
        ("15 mg", "PO", "q4h PRN"),
        ("30 mg", "PO", "q4h PRN"),
        ("2 mg", "IV", "q4h PRN"),
        ("4 mg", "IV", "q4h PRN"),
    ],
    "oxycodone": [
        ("5 mg", "PO", "q4-6h PRN"),
        ("10 mg", "PO", "q4-6h PRN"),
        ("15 mg", "PO", "q4-6h PRN"),
    ],
    "hydrocodone": [
        ("5 mg", "PO", "q4-6h PRN"),
        ("7.5 mg", "PO", "q4-6h PRN"),
        ("10 mg", "PO", "q4-6h PRN"),
    ],
    "fentanyl": [
        ("25 mcg/hr", "TD", "q72h"),
        ("50 mcg/hr", "TD", "q72h"),
        ("75 mcg/hr", "TD", "q72h"),
        ("100 mcg/hr", "TD", "q72h"),
    ],

    # ===== Autonomic Agents =====
    "fludrocortisone": [
        ("0.1 mg", "PO", "daily"),
        ("0.2 mg", "PO", "daily"),
        ("0.3 mg", "PO", "daily"),
    ],
    "midodrine": [
        ("2.5 mg", "PO", "TID"),
        ("5 mg", "PO", "TID"),
        ("10 mg", "PO", "TID"),
    ],
    "droxidopa": [
        ("100 mg", "PO", "TID"),
        ("200 mg", "PO", "TID"),
        ("300 mg", "PO", "TID"),
        ("400 mg", "PO", "TID"),
        ("600 mg", "PO", "TID"),
    ],

    # ===== GI/Prokinetics =====
    "metoclopramide": [
        ("5 mg", "PO", "TID"),
        ("10 mg", "PO", "TID"),
        ("10 mg", "PO", "QID"),
    ],
    "domperidone": [
        ("10 mg", "PO", "TID"),
        ("20 mg", "PO", "TID"),
    ],
    "erythromycin": [
        ("250 mg", "PO", "TID"),
        ("500 mg", "PO", "TID"),
    ],

    # ===== Bladder Agents =====
    "oxybutynin": [
        ("5 mg", "PO", "BID"),
        ("5 mg", "PO", "TID"),
        ("10 mg", "PO", "daily XL"),
        ("15 mg", "PO", "daily XL"),
    ],
    "solifenacin": [
        ("5 mg", "PO", "daily"),
        ("10 mg", "PO", "daily"),
    ],
    "mirabegron": [
        ("25 mg", "PO", "daily"),
        ("50 mg", "PO", "daily"),
    ],
    "tolterodine": [
        ("1 mg", "PO", "BID"),
        ("2 mg", "PO", "BID"),
        ("4 mg", "PO", "daily LA"),
    ],

    # ===== Sexual Dysfunction =====
    "sildenafil": [
        ("25 mg", "PO", "PRN"),
        ("50 mg", "PO", "PRN"),
        ("100 mg", "PO", "PRN"),
    ],
    "tadalafil": [
        ("5 mg", "PO", "daily"),
        ("10 mg", "PO", "PRN"),
        ("20 mg", "PO", "PRN"),
    ],

    # ===== Sodium Channel Blockers =====
    "mexiletine": [
        ("150 mg", "PO", "TID"),
        ("200 mg", "PO", "TID"),
        ("300 mg", "PO", "TID"),
        ("400 mg", "PO", "TID"),
    ],

    # ===== Supplements/Vitamins =====
    "vitamin b12": [
        ("1000 mcg", "PO", "daily"),
        ("2000 mcg", "PO", "daily"),
        ("1000 mcg", "IM", "weekly"),
        ("1000 mcg", "IM", "monthly"),
    ],
    "b12 supplementation": [
        ("1000 mcg", "PO", "daily"),
        ("2000 mcg", "PO", "daily"),
        ("1000 mcg", "IM", "weekly"),
        ("1000 mcg", "IM", "monthly"),
    ],
    "thiamine": [
        ("100 mg", "PO", "daily"),
        ("100 mg", "IV", "daily"),
        ("500 mg", "IV", "TID"),
    ],
    "alpha-lipoic acid": [
        ("300 mg", "PO", "daily"),
        ("600 mg", "PO", "daily"),
        ("600 mg", "IV", "daily"),
    ],
    "coenzyme q10": [
        ("100 mg", "PO", "daily"),
        ("200 mg", "PO", "daily"),
        ("300 mg", "PO", "daily"),
    ],
    "riboflavin": [
        ("200 mg", "PO", "daily"),
        ("400 mg", "PO", "daily"),
    ],
    "magnesium": [
        ("200 mg", "PO", "daily"),
        ("400 mg", "PO", "daily"),
        ("600 mg", "PO", "daily"),
    ],

    # ===== Cholinesterase Inhibitors =====
    "donepezil": [
        ("5 mg", "PO", "daily"),
        ("10 mg", "PO", "daily"),
        ("23 mg", "PO", "daily"),
    ],
    "rivastigmine": [
        ("1.5 mg", "PO", "BID"),
        ("3 mg", "PO", "BID"),
        ("4.5 mg", "PO", "BID"),
        ("6 mg", "PO", "BID"),
        ("4.6 mg/24h", "TD", "daily"),
        ("9.5 mg/24h", "TD", "daily"),
        ("13.3 mg/24h", "TD", "daily"),
    ],
    "galantamine": [
        ("4 mg", "PO", "BID"),
        ("8 mg", "PO", "BID"),
        ("12 mg", "PO", "BID"),
        ("8 mg", "PO", "daily ER"),
        ("16 mg", "PO", "daily ER"),
        ("24 mg", "PO", "daily ER"),
    ],
    "memantine": [
        ("5 mg", "PO", "daily"),
        ("10 mg", "PO", "daily"),
        ("10 mg", "PO", "BID"),
        ("28 mg", "PO", "daily ER"),
    ],

    # ===== Movement Disorder Agents =====
    "tetrabenazine": [
        ("12.5 mg", "PO", "daily"),
        ("12.5 mg", "PO", "BID"),
        ("25 mg", "PO", "BID"),
        ("25 mg", "PO", "TID"),
    ],
    "deutetrabenazine": [
        ("6 mg", "PO", "BID"),
        ("9 mg", "PO", "BID"),
        ("12 mg", "PO", "BID"),
        ("18 mg", "PO", "BID"),
        ("24 mg", "PO", "BID"),
    ],
    "valbenazine": [
        ("40 mg", "PO", "daily"),
        ("60 mg", "PO", "daily"),
        ("80 mg", "PO", "daily"),
    ],

    # ===== Antiemetics =====
    "ondansetron": [
        ("4 mg", "IV", "q8h PRN"),
        ("8 mg", "PO", "q8h PRN"),
    ],
    "prochlorperazine": [
        ("5 mg", "PO", "TID PRN"),
        ("10 mg", "PO", "TID PRN"),
        ("10 mg", "IV", "q6h PRN"),
    ],
    "promethazine": [
        ("12.5 mg", "PO", "q6h PRN"),
        ("25 mg", "PO", "q6h PRN"),
        ("25 mg", "IV", "q6h PRN"),
    ],

    # ===== Antipsychotics =====
    "quetiapine": [
        ("12.5 mg", "PO", "QHS"),
        ("25 mg", "PO", "QHS"),
        ("50 mg", "PO", "QHS"),
        ("100 mg", "PO", "QHS"),
    ],
    "clozapine": [
        ("6.25 mg", "PO", "QHS"),
        ("12.5 mg", "PO", "QHS"),
        ("25 mg", "PO", "daily"),
        ("50 mg", "PO", "daily"),
    ],
    "risperidone": [
        ("0.25 mg", "PO", "daily"),
        ("0.5 mg", "PO", "daily"),
        ("1 mg", "PO", "daily"),
        ("2 mg", "PO", "daily"),
    ],
    "olanzapine": [
        ("2.5 mg", "PO", "daily"),
        ("5 mg", "PO", "daily"),
        ("10 mg", "PO", "daily"),
    ],
    "aripiprazole": [
        ("2 mg", "PO", "daily"),
        ("5 mg", "PO", "daily"),
        ("10 mg", "PO", "daily"),
        ("15 mg", "PO", "daily"),
    ],
    "pimavanserin": [
        ("34 mg", "PO", "daily"),
    ],
    "haloperidol": [
        ("0.5 mg", "PO", "BID"),
        ("1 mg", "PO", "BID"),
        ("2 mg", "PO", "BID"),
        ("5 mg", "IM", "q4h PRN"),
    ],

    # ===== Sleep Aids =====
    "melatonin": [
        ("1 mg", "PO", "QHS"),
        ("3 mg", "PO", "QHS"),
        ("5 mg", "PO", "QHS"),
        ("10 mg", "PO", "QHS"),
    ],
    "trazodone": [
        ("25 mg", "PO", "QHS"),
        ("50 mg", "PO", "QHS"),
        ("100 mg", "PO", "QHS"),
        ("150 mg", "PO", "QHS"),
    ],
    "mirtazapine": [
        ("7.5 mg", "PO", "QHS"),
        ("15 mg", "PO", "QHS"),
        ("30 mg", "PO", "QHS"),
        ("45 mg", "PO", "QHS"),
    ],
    "zolpidem": [
        ("5 mg", "PO", "QHS PRN"),
        ("10 mg", "PO", "QHS PRN"),
    ],

    # ===== Anticoagulants =====
    "warfarin": [
        ("2 mg", "PO", "daily"),
        ("5 mg", "PO", "daily"),
        ("7.5 mg", "PO", "daily"),
        ("10 mg", "PO", "daily"),
    ],
    "apixaban": [
        ("2.5 mg", "PO", "BID"),
        ("5 mg", "PO", "BID"),
    ],
    "rivaroxaban": [
        ("10 mg", "PO", "daily"),
        ("15 mg", "PO", "daily"),
        ("20 mg", "PO", "daily"),
    ],
    "dabigatran": [
        ("75 mg", "PO", "BID"),
        ("110 mg", "PO", "BID"),
        ("150 mg", "PO", "BID"),
    ],
    "edoxaban": [
        ("30 mg", "PO", "daily"),
        ("60 mg", "PO", "daily"),
    ],
    "heparin": [
        ("5000 units", "SC", "q8-12h"),
        ("80 units/kg bolus", "IV", "then 18 units/kg/hr"),
    ],
    "enoxaparin": [
        ("30 mg", "SC", "BID"),
        ("40 mg", "SC", "daily"),
        ("1 mg/kg", "SC", "BID"),
        ("1.5 mg/kg", "SC", "daily"),
    ],

    # ===== Antiplatelets =====
    "aspirin": [
        ("81 mg", "PO", "daily"),
        ("325 mg", "PO", "daily"),
    ],
    "clopidogrel": [
        ("75 mg", "PO", "daily"),
        ("300 mg", "PO", "loading dose"),
    ],
    "ticagrelor": [
        ("90 mg", "PO", "BID"),
        ("180 mg", "PO", "loading dose"),
    ],
    "dipyridamole": [
        ("200 mg", "PO", "BID ER"),
    ],

    # ===== Lipid Lowering =====
    "atorvastatin": [
        ("10 mg", "PO", "daily"),
        ("20 mg", "PO", "daily"),
        ("40 mg", "PO", "daily"),
        ("80 mg", "PO", "daily"),
    ],
    "rosuvastatin": [
        ("5 mg", "PO", "daily"),
        ("10 mg", "PO", "daily"),
        ("20 mg", "PO", "daily"),
        ("40 mg", "PO", "daily"),
    ],

    # ===== Antihypertensives =====
    "lisinopril": [
        ("2.5 mg", "PO", "daily"),
        ("5 mg", "PO", "daily"),
        ("10 mg", "PO", "daily"),
        ("20 mg", "PO", "daily"),
        ("40 mg", "PO", "daily"),
    ],
    "amlodipine": [
        ("2.5 mg", "PO", "daily"),
        ("5 mg", "PO", "daily"),
        ("10 mg", "PO", "daily"),
    ],
    "hydralazine": [
        ("10 mg", "PO", "QID"),
        ("25 mg", "PO", "QID"),
        ("50 mg", "PO", "QID"),
    ],
    "labetalol": [
        ("100 mg", "PO", "BID"),
        ("200 mg", "PO", "BID"),
        ("300 mg", "PO", "BID"),
        ("10 mg", "IV", "q10min PRN"),
        ("20 mg", "IV", "q10min PRN"),
    ],
    "nicardipine": [
        ("5 mg/hr", "IV", "infusion"),
        ("15 mg/hr", "IV", "max infusion"),
    ],

    # ===== Low-dose Naltrexone =====
    "low-dose naltrexone (ldn)": [
        ("1.5 mg", "PO", "QHS"),
        ("3 mg", "PO", "QHS"),
        ("4.5 mg", "PO", "QHS"),
    ],
    "naltrexone": [
        ("1.5 mg", "PO", "QHS"),
        ("3 mg", "PO", "QHS"),
        ("4.5 mg", "PO", "QHS"),
        ("50 mg", "PO", "daily"),
    ],

    # ===== Specialty/Other =====
    "edaravone": [
        ("60 mg", "IV", "daily x14 days then off 14 days"),
    ],
    "riluzole": [
        ("50 mg", "PO", "BID"),
    ],
    "tafamidis": [
        ("61 mg", "PO", "daily"),
        ("80 mg", "PO", "daily"),
    ],
    "patisiran": [
        ("0.3 mg/kg", "IV", "q3wk"),
    ],
    "inotersen": [
        ("284 mg", "SC", "weekly"),
    ],

    # ===== Common Analgesics / NSAIDs =====
    "acetaminophen": [
        ("325 mg", "PO", "q6h PRN"),
        ("500 mg", "PO", "q6h PRN"),
        ("650 mg", "PO", "q6h PRN"),
        ("1000 mg", "PO", "q6h PRN"),
    ],
    "ibuprofen": [
        ("200 mg", "PO", "q6h PRN"),
        ("400 mg", "PO", "q6h PRN"),
        ("600 mg", "PO", "q8h"),
        ("800 mg", "PO", "q8h"),
    ],
    "naproxen": [
        ("250 mg", "PO", "BID"),
        ("500 mg", "PO", "BID"),
    ],
    "naproxen sodium": [
        ("220 mg", "PO", "BID"),
        ("550 mg", "PO", "BID"),
    ],
    "ketorolac": [
        ("15 mg", "IV", "q6h"),
        ("30 mg", "IV", "q6h"),
    ],
    "meclizine": [
        ("12.5 mg", "PO", "q8h PRN"),
        ("25 mg", "PO", "q8h PRN"),
        ("50 mg", "PO", "q8h PRN"),
    ],
    "diphenhydramine": [
        ("25 mg", "IV/PO", "q6h PRN"),
        ("50 mg", "IV/PO", "q6h PRN"),
    ],

    # ===== SSRIs (not already in dict) =====
    "sertraline": [
        ("25 mg", "PO", "daily"),
        ("50 mg", "PO", "daily"),
        ("100 mg", "PO", "daily"),
        ("150 mg", "PO", "daily"),
        ("200 mg", "PO", "daily"),
    ],
    "escitalopram": [
        ("5 mg", "PO", "daily"),
        ("10 mg", "PO", "daily"),
        ("20 mg", "PO", "daily"),
    ],
    "citalopram": [
        ("10 mg", "PO", "daily"),
        ("20 mg", "PO", "daily"),
        ("40 mg", "PO", "daily"),
    ],
    "fluoxetine": [
        ("10 mg", "PO", "daily"),
        ("20 mg", "PO", "daily"),
        ("40 mg", "PO", "daily"),
        ("60 mg", "PO", "daily"),
    ],
    "paroxetine": [
        ("10 mg", "PO", "daily"),
        ("20 mg", "PO", "daily"),
        ("40 mg", "PO", "daily"),
    ],

    # ===== Stimulants / Wakefulness =====
    "modafinil": [
        ("100 mg", "PO", "daily"),
        ("200 mg", "PO", "daily"),
        ("400 mg", "PO", "daily"),
    ],
    "methylphenidate": [
        ("2.5 mg", "PO", "BID"),
        ("5 mg", "PO", "BID"),
        ("10 mg", "PO", "BID"),
        ("20 mg", "PO", "BID"),
    ],
    "armodafinil": [
        ("150 mg", "PO", "daily"),
        ("250 mg", "PO", "daily"),
    ],

    # ===== GI / Antiemetics (not already in dict) =====
    "pantoprazole": [
        ("20 mg", "IV/PO", "daily"),
        ("40 mg", "IV/PO", "daily"),
        ("40 mg", "IV/PO", "BID"),
    ],
    "omeprazole": [
        ("20 mg", "PO", "daily"),
        ("40 mg", "PO", "daily"),
    ],
    "docusate sodium": [
        ("100 mg", "PO", "daily"),
        ("100 mg", "PO", "BID"),
    ],
    "polyethylene glycol": [
        ("17 g", "PO", "daily"),
    ],
    "senna": [
        ("8.6 mg", "PO", "daily"),
        ("17.2 mg", "PO", "daily"),
    ],
    "buspirone": [
        ("5 mg", "PO", "BID"),
        ("10 mg", "PO", "BID"),
        ("15 mg", "PO", "BID"),
        ("20 mg", "PO", "BID"),
    ],

    # ===== Carbonic Anhydrase Inhibitors =====
    "acetazolamide": [
        ("125 mg", "PO", "BID"),
        ("250 mg", "PO", "BID"),
        ("500 mg", "PO", "BID"),
    ],

    # ===== Anticoagulation / DVT Prophylaxis =====
    "dvt prophylaxis: enoxaparin": [
        ("30 mg", "SC", "BID"),
        ("40 mg", "SC", "daily"),
    ],
    "dvt prophylaxis: heparin sc": [
        ("5000 units", "SC", "q8h"),
        ("5000 units", "SC", "q12h"),
    ],

    # ===== IV Steroids =====
    "methylprednisolone iv": [
        ("250 mg", "IV", "daily"),
        ("500 mg", "IV", "daily"),
        ("1000 mg", "IV", "daily x3-5 days"),
    ],
    "iv methylprednisolone": [
        ("250 mg", "IV", "daily"),
        ("500 mg", "IV", "daily"),
        ("1000 mg", "IV", "daily x3-5 days"),
    ],

    # ===== Antibiotics / Antivirals =====
    "acyclovir iv": [
        ("10 mg/kg", "IV", "q8h"),
        ("15 mg/kg", "IV", "q8h"),
    ],
    "acyclovir": [
        ("10 mg/kg", "IV", "q8h"),
        ("800 mg", "PO", "5x daily"),
    ],
    "valacyclovir": [
        ("500 mg", "PO", "BID"),
        ("1000 mg", "PO", "TID"),
    ],
    "ceftriaxone": [
        ("2 g", "IV", "q12h"),
        ("2 g", "IV", "daily"),
    ],
    "vancomycin": [
        ("15-20 mg/kg", "IV", "q8-12h"),
        ("25-30 mg/kg", "IV", "loading dose"),
    ],
    "ampicillin": [
        ("2 g", "IV", "q4h"),
    ],
    "fluconazole": [
        ("400 mg", "PO/IV", "daily"),
        ("800 mg", "PO/IV", "daily"),
        ("1200 mg", "PO/IV", "daily"),
    ],

    # ===== Osmotic Therapy =====
    "mannitol": [
        ("0.5 g/kg", "IV", "q6h"),
        ("1 g/kg", "IV", "q6h"),
        ("1.5 g/kg", "IV", "q6h"),
    ],
    "mannitol 20%": [
        ("0.5 g/kg", "IV", "q6h"),
        ("1 g/kg", "IV", "q6h"),
        ("1.5 g/kg", "IV", "q6h"),
    ],
    "hypertonic saline 23.4%": [
        ("30 mL", "IV", "bolus over 15 min"),
    ],
    "hypertonic saline 3%": [
        ("150 mL", "IV", "bolus over 20 min"),
        ("250 mL", "IV", "over 30 min"),
    ],

    # ===== Biologics / Monoclonal Antibodies =====
    "tocilizumab": [
        ("4 mg/kg", "IV", "q4wk"),
        ("8 mg/kg", "IV", "q4wk"),
    ],
    "eculizumab": [
        ("900 mg", "IV", "weekly x4 then 1200 mg q2wk"),
    ],

    # ===== Other Common Neuro Medications =====
    "glycopyrrolate": [
        ("1 mg", "PO", "BID"),
        ("1 mg", "PO", "TID"),
        ("2 mg", "PO", "TID"),
    ],
    "tamsulosin": [
        ("0.4 mg", "PO", "daily"),
        ("0.8 mg", "PO", "daily"),
    ],
    "4-aminopyridine": [
        ("5 mg", "PO", "BID"),
        ("10 mg", "PO", "BID"),
    ],
    "dalfampridine": [
        ("10 mg", "PO", "BID"),
    ],
    "capsaicin 8% patch": [
        ("1 patch", "Topical", "q3mo"),
        ("2 patches", "Topical", "q3mo"),
    ],
    "lidocaine 5% patch": [
        ("1 patch", "Topical", "12h on/12h off"),
        ("2 patches", "Topical", "12h on/12h off"),
        ("3 patches", "Topical", "12h on/12h off"),
    ],
    "alendronate": [
        ("35 mg", "PO", "weekly"),
        ("70 mg", "PO", "weekly"),
    ],
    "levothyroxine": [
        ("25 mcg", "PO", "daily"),
        ("50 mcg", "PO", "daily"),
        ("75 mcg", "PO", "daily"),
        ("100 mcg", "PO", "daily"),
    ],
    "ezetimibe": [
        ("10 mg", "PO", "daily"),
    ],
    "magnesium sulfate": [
        ("1 g", "IV", "bolus"),
        ("2 g", "IV", "bolus"),
        ("4 g", "IV", "loading dose"),
    ],
    "calcium + vitamin d": [
        ("500 mg Ca + 400 IU D", "PO", "daily"),
        ("500 mg Ca + 1000 IU D", "PO", "BID"),
        ("1000 mg Ca + 2000 IU D", "PO", "daily"),
    ],
    "onabotulinumtoxina": [
        ("100 units", "IM", "q3mo"),
        ("155 units", "IM", "q3mo"),
        ("200 units", "IM", "q3mo"),
    ],
}


# ---------------------------------------------------------------------------
# Medication name normalization
# ---------------------------------------------------------------------------
def normalize_med_name(name):
    """Normalize medication name for lookup."""
    # Remove bold markers, parenthetical brand names, extra whitespace
    name = name.lower()
    name = re.sub(r'\*+', '', name)
    name = re.sub(r'\([^)]*\)', '', name)  # Remove (Brand Name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def extract_med_base_name(item_name):
    """Extract the base medication name from an item."""
    norm = normalize_med_name(item_name)

    # Try direct match first
    if norm in MEDICATION_DOSES:
        return norm

    # Try first word(s) match
    words = norm.split()
    for i in range(len(words), 0, -1):
        partial = ' '.join(words[:i])
        if partial in MEDICATION_DOSES:
            return partial

    return None


# ---------------------------------------------------------------------------
# Order sentence generation
# ---------------------------------------------------------------------------
def generate_order_sentence(med_name, dose, route, frequency):
    """Generate a complete order sentence."""
    # Capitalize medication name properly
    cap_name = ' '.join(w.capitalize() for w in med_name.split())

    # Build order sentence
    if route and route != '-':
        return f"{cap_name} {dose} {route} {frequency}"
    else:
        return f"{cap_name} {dose} {frequency}"


# ---------------------------------------------------------------------------
# Medication database fallback lookup
# ---------------------------------------------------------------------------
def lookup_dose_options_from_db(item_name):
    """Look up dose options from the central medications.json database.

    Returns a list of doseOption dicts (with 'text' and 'orderSentence')
    or None if not found or only 1 option available.
    """
    if not _resolver_available:
        return None

    # Normalize the name the same way the resolver does
    norm = normalize_med_name(item_name)

    # Try direct lookup
    options = _resolver.get_dose_options(norm)
    if options and len(options) > 1:
        return options

    # Try progressively shorter prefixes (same strategy as extract_med_base_name)
    words = norm.split()
    for i in range(len(words), 0, -1):
        partial = ' '.join(words[:i])
        options = _resolver.get_dose_options(partial)
        if options and len(options) > 1:
            return options

    return None


# ---------------------------------------------------------------------------
# Dose options expansion
# ---------------------------------------------------------------------------
def expand_dose_options(item, med_name):
    """Expand doseOptions for a medication item.

    Uses two-tier lookup:
      1. Hardcoded MEDICATION_DOSES dict (176 manually curated medications)
      2. Central medications.json database via MedicationResolver (936 medications)
    """
    dosing = item.get('dosing', {})
    if not isinstance(dosing, dict):
        return None

    current_options = dosing.get('doseOptions', [])
    if not current_options:
        return None

    # Already has multiple options
    if len(current_options) > 1:
        return None

    # --- Tier 1: Try hardcoded MEDICATION_DOSES dict ---
    base_name = extract_med_base_name(med_name)
    if base_name:
        dose_list = MEDICATION_DOSES.get(base_name)
        if dose_list:
            item_route = dosing.get('route', item.get('route', 'PO'))
            new_options = []
            for dose, route, freq in dose_list:
                use_route = item_route if item_route and item_route != '-' else route
                text = f"{dose} {freq}"
                order_sentence = generate_order_sentence(base_name, dose, use_route, freq)
                new_options.append({
                    "text": text,
                    "orderSentence": order_sentence
                })
            return new_options

    # --- Tier 2: Fall back to medications.json database ---
    db_options = lookup_dose_options_from_db(med_name)
    if db_options and len(db_options) > 1:
        return db_options

    return None


# ---------------------------------------------------------------------------
# File processing
# ---------------------------------------------------------------------------
def process_treatment_section(section, section_name, changes):
    """Process a treatment section and expand dose options."""
    if not isinstance(section, list):
        return

    for item in section:
        if not isinstance(item, dict):
            continue

        item_name = item.get('item', '')
        if not item_name:
            continue

        # Check if this is a medication with dosing
        dosing = item.get('dosing')
        if not isinstance(dosing, dict):
            continue

        # Skip non-medication items
        if dosing.get('route') in (None, '-', 'N/A', 'External', 'Diet', 'Implant'):
            continue

        # Try to expand dose options
        new_options = expand_dose_options(item, item_name)
        if new_options:
            old_options = dosing.get('doseOptions', [])
            dosing['doseOptions'] = new_options

            # Update main orderSentence to first option
            if new_options:
                dosing['orderSentence'] = new_options[0]['orderSentence']

            changes.append({
                'section': section_name,
                'item': item_name[:50],
                'old_count': len(old_options),
                'new_count': len(new_options),
            })


def process_json_file(filepath, dry_run=False):
    """Process a single JSON plan file."""
    path = Path(filepath)

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"  Error reading {path.name}: {e}")
        return []

    changes = []

    # Look for Treatment sections
    sections = data.get('sections', {})
    if not isinstance(sections, dict):
        return []

    for section_name, section_data in sections.items():
        if 'treatment' in section_name.lower():
            if isinstance(section_data, dict):
                # Treatment section with subsections
                for subsection_name, subsection_data in section_data.items():
                    full_name = f"{section_name} > {subsection_name}"
                    process_treatment_section(subsection_data, full_name, changes)
            elif isinstance(section_data, list):
                # Direct list of treatments
                process_treatment_section(section_data, section_name, changes)

    # Write changes
    if changes and not dry_run:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write('\n')

    return changes


def main():
    dry_run = '--dry-run' in sys.argv
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    files = []

    # Priority plans to process first
    priority_plans = [
        'small-fiber-neuropathy.json',
        'diabetic-neuropathy.json',
        'peripheral-neuropathy.json',
        'chronic-migraine.json',
        'migraine-with-aura.json',
        'epilepsy-chronic-management.json',
        'essential-tremor.json',
        'tremor-unspecified.json',
        'cluster-headache.json',
        'tension-headache.json',
        'headache-evaluation.json',
        'headache-unspecified.json',
        'status-migrainosus.json',
    ]

    if '--all' in sys.argv:
        plans_dir = Path('docs/plans')
        # Process priority plans first, then others
        all_files = list(plans_dir.glob('*.json'))

        # Skip report files
        all_files = [f for f in all_files if not any(x in f.name for x in ['report', 'citation', 'cpt-synonym', 'icd-synonym'])]

        priority_files = [plans_dir / p for p in priority_plans if (plans_dir / p).exists()]
        other_files = [f for f in all_files if f not in priority_files]

        files = priority_files + sorted(other_files)
    elif '--priority' in sys.argv:
        plans_dir = Path('docs/plans')
        files = [plans_dir / p for p in priority_plans if (plans_dir / p).exists()]
    else:
        for arg in sys.argv[1:]:
            if not arg.startswith('--') and not arg.startswith('-'):
                files.append(Path(arg))

    if not files:
        print("Usage: python scripts/expand_dose_options.py --all [--dry-run] [--verbose]")
        print("       python scripts/expand_dose_options.py --priority [--dry-run]")
        print("       python scripts/expand_dose_options.py docs/plans/file.json [--dry-run]")
        sys.exit(1)

    total_expanded = 0
    files_modified = 0
    all_changes = []

    for filepath in files:
        if not filepath.exists():
            continue

        changes = process_json_file(filepath, dry_run=dry_run)
        if changes:
            files_modified += 1
            total_expanded += len(changes)
            all_changes.extend([(filepath.name, c) for c in changes])

            print(f"\n  {filepath.name}: {len(changes)} medications expanded")
            if verbose:
                for c in changes:
                    print(f"    [{c['section'][:40]}] {c['item']}: {c['old_count']} -> {c['new_count']} options")

    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n{'=' * 70}")
    print(f"  {mode}: {total_expanded} medications expanded across {files_modified} files")
    print(f"{'=' * 70}")

    # Summary of medication categories expanded
    if all_changes and verbose:
        meds = {}
        for _, c in all_changes:
            item = c['item'].lower()
            # Extract base name
            base = extract_med_base_name(item)
            if base:
                meds[base] = meds.get(base, 0) + 1

        print("\n  By medication:")
        for med, count in sorted(meds.items(), key=lambda x: -x[1])[:20]:
            print(f"    {med}: {count}")


if __name__ == '__main__':
    main()
