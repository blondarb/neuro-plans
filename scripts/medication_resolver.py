#!/usr/bin/env python3
"""Medication Reference Resolver for Neuro Plans.

This module provides functions to resolve medication references from the
central medication database (medications.json) and merge them with
plan-specific context overrides.

Key Features:
- Central medication data lookup with indication-specific dosing
- Safety data inclusion (contraindications, black box warnings, drug interactions)
- Renal/hepatic adjustment tiers
- Plan-specific context overrides
- Formulary and institutional flag support

Hospital Safety Features:
- Max dose limits per indication
- Black box warning visibility
- Critical drug interactions flagged
- Renal adjustment reminders

Usage:
    from medication_resolver import MedicationResolver

    resolver = MedicationResolver()

    # Get medication with specific context
    gabapentin = resolver.get_medication("gabapentin", context="neuropathic-pain")

    # Get all available contexts for a medication
    contexts = resolver.get_contexts("gabapentin")

    # Check if medication exists
    exists = resolver.has_medication("gabapentin")
"""

import json
import re
from pathlib import Path
from typing import Optional


class MedicationResolver:
    """Resolves medication references from the central database."""

    def __init__(self, db_path: Optional[Path] = None):
        """Initialize the resolver with the medication database.

        Args:
            db_path: Path to medications.json. Defaults to docs/data/medications.json
        """
        if db_path is None:
            # Try common locations
            possible_paths = [
                Path("docs/data/medications.json"),
                Path("../docs/data/medications.json"),
                Path(__file__).parent.parent / "docs" / "data" / "medications.json"
            ]
            for path in possible_paths:
                if path.exists():
                    db_path = path
                    break

        self.db_path = db_path
        self._medications = {}
        self._metadata = {}
        self._loaded = False

    def _load(self):
        """Load the medication database if not already loaded."""
        if self._loaded:
            return

        if self.db_path and self.db_path.exists():
            try:
                with open(self.db_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self._metadata = data.get('_metadata', {})
                    self._medications = data.get('medications', {})
                    self._loaded = True
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not load medication database: {e}")
                self._medications = {}
                self._loaded = True

    def _normalize_name(self, name: str) -> str:
        """Normalize medication name for lookup."""
        name = name.lower().strip()
        name = re.sub(r'\*+', '', name)  # Remove bold markers
        name = re.sub(r'\([^)]*\)', '', name)  # Remove (Brand Name)
        name = re.sub(r'\s+', ' ', name).strip()
        return name

    def has_medication(self, name: str) -> bool:
        """Check if medication exists in the database."""
        self._load()
        normalized = self._normalize_name(name)
        return normalized in self._medications

    def get_medication(self, name: str, context: Optional[str] = None) -> Optional[dict]:
        """Get medication data, optionally with specific context.

        Args:
            name: Medication name (case-insensitive, brand or generic)
            context: Specific indication context (e.g., "neuropathic-pain", "epilepsy")

        Returns:
            Medication data dict with safety info, or None if not found
        """
        self._load()
        normalized = self._normalize_name(name)

        if normalized not in self._medications:
            return None

        med = self._medications[normalized].copy()

        # If context specified, get context-specific data
        if context and 'contexts' in med:
            context_data = med['contexts'].get(context)
            if context_data:
                med['activeContext'] = context
                med['contextData'] = context_data
                med['doseOptions'] = context_data.get('doseOptions', [])
                med['maxDose'] = context_data.get('maxDose', '')
                med['startingDose'] = context_data.get('startingDose', '')
                med['titration'] = context_data.get('titration', '')
                med['contextNotes'] = context_data.get('notes', '')

        return med

    def get_contexts(self, name: str) -> list:
        """Get all available contexts/indications for a medication."""
        self._load()
        normalized = self._normalize_name(name)

        if normalized not in self._medications:
            return []

        med = self._medications[normalized]
        return list(med.get('contexts', {}).keys())

    def get_safety_data(self, name: str) -> Optional[dict]:
        """Get safety data for a medication.

        Returns dict with:
            - blackBoxWarnings: List of FDA black box warnings
            - contraindications: List of absolute contraindications
            - precautions: List of warnings/precautions
            - drugInteractions: List of significant interactions
            - renalAdjustment: Renal dosing tiers
            - hepaticAdjustment: Hepatic dosing notes
        """
        self._load()
        normalized = self._normalize_name(name)

        if normalized not in self._medications:
            return None

        med = self._medications[normalized]

        return {
            'blackBoxWarnings': med.get('safety', {}).get('blackBoxWarnings', []),
            'contraindications': med.get('safety', {}).get('contraindications', []),
            'precautions': med.get('safety', {}).get('precautions', []),
            'drugInteractions': med.get('safety', {}).get('drugInteractions', []),
            'pregnancyCategory': med.get('safety', {}).get('pregnancyCategory', ''),
            'lactation': med.get('safety', {}).get('lactation', ''),
            'renalAdjustment': med.get('renalAdjustment', {}),
            'hepaticAdjustment': med.get('hepaticAdjustment', {}),
            'monitoring': med.get('monitoring', {}),
            'patientCounseling': med.get('patientCounseling', [])
        }

    def get_renal_adjustment(self, name: str, gfr: int) -> Optional[str]:
        """Get renal dosing adjustment recommendation for a GFR value.

        Args:
            name: Medication name
            gfr: GFR in mL/min (use -1 for HD)

        Returns:
            Adjustment recommendation string, or None if not found
        """
        self._load()
        normalized = self._normalize_name(name)

        if normalized not in self._medications:
            return None

        med = self._medications[normalized]
        renal = med.get('renalAdjustment', {})

        if not renal.get('required', False):
            return "No renal adjustment needed"

        tiers = renal.get('tiers', [])

        for tier in tiers:
            gfr_range = tier.get('gfr', '')
            adjustment = tier.get('adjustment', '')

            # Handle special cases
            if gfr == -1 and 'HD' in gfr_range.upper():
                return adjustment

            # Parse GFR range
            if '≥' in gfr_range:
                threshold = int(re.search(r'\d+', gfr_range).group())
                if gfr >= threshold:
                    return adjustment
            elif '<' in gfr_range and '-' not in gfr_range:
                threshold = int(re.search(r'\d+', gfr_range).group())
                if gfr < threshold:
                    return adjustment
            elif '-' in gfr_range:
                match = re.search(r'(\d+)-(\d+)', gfr_range)
                if match:
                    low, high = int(match.group(1)), int(match.group(2))
                    if low <= gfr <= high:
                        return adjustment

        return None

    def get_dose_options(self, name: str, context: Optional[str] = None) -> list:
        """Get dose options for a medication.

        Args:
            name: Medication name
            context: Optional indication context

        Returns:
            List of dose option dicts with 'text' and 'orderSentence'
        """
        self._load()
        normalized = self._normalize_name(name)

        if normalized not in self._medications:
            return []

        med = self._medications[normalized]

        if context and 'contexts' in med:
            context_data = med['contexts'].get(context, {})
            if context_data:
                return context_data.get('doseOptions', [])

        # Return first available context's dose options if no specific context
        for ctx_data in med.get('contexts', {}).values():
            if ctx_data.get('doseOptions'):
                return ctx_data['doseOptions']

        return []

    def get_black_box_warnings(self, name: str) -> list:
        """Get FDA black box warnings for a medication.

        Args:
            name: Medication name

        Returns:
            List of black box warning strings
        """
        self._load()
        normalized = self._normalize_name(name)

        if normalized not in self._medications:
            return []

        med = self._medications[normalized]
        return med.get('safety', {}).get('blackBoxWarnings', [])

    def has_black_box_warning(self, name: str) -> bool:
        """Check if medication has any black box warnings."""
        return len(self.get_black_box_warnings(name)) > 0

    def get_high_risk_interactions(self, name: str) -> list:
        """Get high-severity drug interactions.

        Returns:
            List of interaction dicts with severity 'high' or 'contraindicated'
        """
        self._load()
        normalized = self._normalize_name(name)

        if normalized not in self._medications:
            return []

        med = self._medications[normalized]
        interactions = med.get('safety', {}).get('drugInteractions', [])

        return [i for i in interactions if i.get('severity') in ('high', 'contraindicated')]

    def enrich_plan_medication(self, plan_med: dict, context: Optional[str] = None) -> dict:
        """Enrich a plan medication item with central database data.

        Merges central database info with plan-specific overrides.
        Plan-specific values take precedence.

        Args:
            plan_med: Original medication dict from plan
            context: Indication context to use

        Returns:
            Enriched medication dict
        """
        item_name = plan_med.get('item', '')
        if not item_name:
            return plan_med

        # Check if medication exists in central DB
        central = self.get_medication(item_name, context=context)
        if not central:
            return plan_med

        # Create enriched copy
        enriched = plan_med.copy()

        # Add central data that's not overridden by plan
        safety = self.get_safety_data(item_name)
        if safety:
            # Add safety data for display
            if safety.get('blackBoxWarnings'):
                enriched['_blackBoxWarnings'] = safety['blackBoxWarnings']
            if safety.get('renalAdjustment', {}).get('required'):
                enriched['_renalAdjustmentRequired'] = True
                enriched['_renalAdjustmentTiers'] = safety['renalAdjustment'].get('tiers', [])

        # Enrich dose options if not fully specified in plan
        dosing = enriched.get('dosing', {})
        if isinstance(dosing, dict):
            plan_options = dosing.get('doseOptions', [])

            # If plan has only 1 option, enrich with central options
            if len(plan_options) <= 1:
                central_options = self.get_dose_options(item_name, context)
                if central_options:
                    dosing['doseOptions'] = central_options
                    enriched['dosing'] = dosing

        # Add patient counseling if not present
        if not enriched.get('_patientCounseling') and safety:
            enriched['_patientCounseling'] = safety.get('patientCounseling', [])

        return enriched

    def generate_treatment_row(self, name: str, context_id: Optional[str] = None,
                               include_header: bool = False) -> Optional[str]:
        """Generate a 10-column markdown treatment table row.

        Format: | Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |

        Dosing uses structured format: dose_options :: route :: :: full_instructions

        Args:
            name: Medication name
            context_id: Specific context/indication ID. If None, uses first available context.
            include_header: If True, prepend the table header row.

        Returns:
            Markdown table row string, or None if medication not found.
        """
        self._load()
        normalized = self._normalize_name(name)

        if normalized not in self._medications:
            return None

        med = self._medications[normalized]
        contexts = med.get('contexts', {})

        if not contexts:
            return None

        # Select context
        if context_id and context_id in contexts:
            ctx = contexts[context_id]
        elif context_id:
            # Try fuzzy match on indication text
            for cid, cdata in contexts.items():
                if context_id.lower() in cdata.get('indication', '').lower():
                    ctx = cdata
                    context_id = cid
                    break
            else:
                # Fall back to first context
                context_id = list(contexts.keys())[0]
                ctx = contexts[context_id]
        else:
            context_id = list(contexts.keys())[0]
            ctx = contexts[context_id]

        # Build display name
        display_name = med.get('name', name)

        # Build route
        route = med.get('routes', ['-'])[0] if med.get('routes') else '-'
        # If context has a dosing route, prefer that
        dose_options = ctx.get('doseOptions', [])

        # Build indication
        indication = ctx.get('indication', '-')

        # Build structured dosing string
        dosing_str = self._build_dosing_string(dose_options, route, ctx)

        # Build contraindications
        contras = med.get('safety', {}).get('contraindications', [])
        contras_str = '; '.join(contras[:5]) if contras else '-'  # Limit to 5 for table width

        # Build monitoring
        monitoring = med.get('monitoring', {}).get('ongoing', [])
        monitoring_str = '; '.join(monitoring[:5]) if monitoring else '-'

        # Build settings
        settings = ctx.get('settings', {})
        ed = settings.get('ED', '-')
        hosp = settings.get('HOSP', '-')
        opd = settings.get('OPD', '-')
        icu = settings.get('ICU', '-')

        # Assemble row
        row = f"| {display_name} | {route} | {indication} | {dosing_str} | {contras_str} | {monitoring_str} | {ed} | {hosp} | {opd} | {icu} |"

        if include_header:
            header = "| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |"
            separator = "| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |"
            return f"{header}\n{separator}\n{row}"

        return row

    def _build_dosing_string(self, dose_options: list, route: str, ctx: dict) -> str:
        """Build the structured dosing string in :: format.

        Format: dose_options :: route :: :: full_instructions
        """
        instructions = ctx.get('notes', '') or ctx.get('titration', '')
        if not instructions:
            # Build from startingDose + maxDose
            parts = []
            if ctx.get('startingDose'):
                parts.append(f"Start {ctx['startingDose']}")
            if ctx.get('titration'):
                parts.append(ctx['titration'])
            if ctx.get('maxDose'):
                parts.append(f"max {ctx['maxDose']}")
            instructions = '; '.join(parts) if parts else '-'

        if dose_options:
            # Join dose option texts with semicolons
            dose_texts = [opt.get('text', '') for opt in dose_options if opt.get('text')]
            dose_field = '; '.join(dose_texts) if dose_texts else '-'
            return f"{dose_field} :: {route} :: :: {instructions}"
        else:
            return instructions

    def generate_treatment_rows(self, name: str, include_header: bool = False) -> list:
        """Generate treatment table rows for ALL contexts of a medication.

        Returns:
            List of markdown row strings, one per context.
        """
        self._load()
        normalized = self._normalize_name(name)

        if normalized not in self._medications:
            return []

        med = self._medications[normalized]
        contexts = med.get('contexts', {})

        rows = []
        for i, ctx_id in enumerate(contexts):
            row = self.generate_treatment_row(name, context_id=ctx_id,
                                              include_header=(include_header and i == 0))
            if row:
                rows.append(row)

        return rows

    def list_medications(self) -> list:
        """List all medication IDs in the database."""
        self._load()
        return list(self._medications.keys())

    def get_medications_with_black_box(self) -> list:
        """List all medications with black box warnings."""
        self._load()
        result = []
        for med_id, med in self._medications.items():
            if med.get('safety', {}).get('blackBoxWarnings'):
                result.append({
                    'id': med_id,
                    'name': med.get('name', med_id),
                    'warnings': med['safety']['blackBoxWarnings']
                })
        return result

    def get_medications_requiring_renal_adjustment(self) -> list:
        """List all medications requiring renal adjustment."""
        self._load()
        result = []
        for med_id, med in self._medications.items():
            if med.get('renalAdjustment', {}).get('required'):
                result.append({
                    'id': med_id,
                    'name': med.get('name', med_id),
                    'tiers': med['renalAdjustment'].get('tiers', [])
                })
        return result


# Convenience functions for direct usage
_resolver = None

def get_resolver() -> MedicationResolver:
    """Get or create the global resolver instance."""
    global _resolver
    if _resolver is None:
        _resolver = MedicationResolver()
    return _resolver

def get_medication(name: str, context: Optional[str] = None) -> Optional[dict]:
    """Get medication from central database."""
    return get_resolver().get_medication(name, context)

def get_dose_options(name: str, context: Optional[str] = None) -> list:
    """Get dose options for a medication."""
    return get_resolver().get_dose_options(name, context)

def get_safety_data(name: str) -> Optional[dict]:
    """Get safety data for a medication."""
    return get_resolver().get_safety_data(name)

def has_black_box_warning(name: str) -> bool:
    """Check if medication has black box warning."""
    return get_resolver().has_black_box_warning(name)


# CLI usage
def main():
    import sys

    resolver = MedicationResolver()

    if len(sys.argv) < 2:
        print("Usage: python medication_resolver.py <medication-name> [context]")
        print("\nExamples:")
        print("  python medication_resolver.py gabapentin")
        print("  python medication_resolver.py gabapentin neuropathic-pain")
        print("  python medication_resolver.py --list")
        print("  python medication_resolver.py --black-box")
        print("  python medication_resolver.py --renal")
        sys.exit(1)

    arg = sys.argv[1]

    if arg == '--list':
        print(f"\nMedications in database ({len(resolver.list_medications())}):")
        for med_id in sorted(resolver.list_medications()):
            contexts = resolver.get_contexts(med_id)
            print(f"  {med_id}: {', '.join(contexts)}")
        return

    if arg == '--black-box':
        print("\nMedications with Black Box Warnings:")
        for med in resolver.get_medications_with_black_box():
            print(f"\n  {med['name']}:")
            for warning in med['warnings']:
                print(f"    - {warning}")
        return

    if arg == '--renal':
        print("\nMedications Requiring Renal Adjustment:")
        for med in resolver.get_medications_requiring_renal_adjustment():
            print(f"\n  {med['name']}:")
            for tier in med['tiers']:
                print(f"    GFR {tier['gfr']}: {tier['adjustment']}")
        return

    med_name = arg
    context = sys.argv[2] if len(sys.argv) > 2 else None

    med = resolver.get_medication(med_name, context=context)

    if not med:
        print(f"Medication '{med_name}' not found in database.")
        sys.exit(1)

    print(f"\n{'=' * 60}")
    print(f"  {med['name']} ({med['genericName']})")
    print(f"{'=' * 60}")

    print(f"\n  Brand Names: {', '.join(med.get('brandNames', []))}")
    print(f"  Drug Class: {med.get('drugClass', 'N/A')}")
    print(f"  Routes: {', '.join(med.get('routes', []))}")

    # Available contexts
    contexts = resolver.get_contexts(med_name)
    print(f"\n  Available Contexts: {', '.join(contexts)}")

    # Context-specific info
    if context and 'contextData' in med:
        ctx = med['contextData']
        print(f"\n  Context: {context}")
        print(f"  Starting Dose: {ctx.get('startingDose', 'N/A')}")
        print(f"  Max Dose: {ctx.get('maxDose', 'N/A')}")
        print(f"  Titration: {ctx.get('titration', 'N/A')}")
        print(f"  Notes: {ctx.get('notes', 'N/A')}")

        print(f"\n  Dose Options:")
        for opt in ctx.get('doseOptions', []):
            print(f"    - {opt['text']}: {opt['orderSentence']}")

    # Safety info
    safety = resolver.get_safety_data(med_name)
    if safety:
        if safety['blackBoxWarnings']:
            print(f"\n  BLACK BOX WARNINGS:")
            for w in safety['blackBoxWarnings']:
                print(f"    - {w}")

        if safety['contraindications']:
            print(f"\n  Contraindications:")
            for c in safety['contraindications']:
                print(f"    - {c}")

        high_risk = resolver.get_high_risk_interactions(med_name)
        if high_risk:
            print(f"\n  High-Risk Interactions:")
            for i in high_risk:
                print(f"    - {i['drug']}: {i['effect']}")

        if safety['renalAdjustment'].get('required'):
            print(f"\n  Renal Adjustment Required:")
            for tier in safety['renalAdjustment'].get('tiers', []):
                print(f"    GFR {tier['gfr']}: {tier['adjustment']}")

    print()


if __name__ == '__main__':
    main()
