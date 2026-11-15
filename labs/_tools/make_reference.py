"""Write labs/data/reference/*.json, the results the safety-net cells fall back on.

    cd labs
    uv run python _tools/make_reference.py            # every lab
    uv run python _tools/make_reference.py D1_2       # the labs whose name starts so

Each lab source in _src/ is run with its solutions, as the solution notebook runs, and the
values named below are read from it and saved. Run it after changing a lab or the data.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

LABS = Path(__file__).resolve().parents[1]
REF = LABS / "data" / "reference"

# lab source -> {reference name: expression evaluated after the lab ran}
REFS = {
    "D1_1_five_requests": {
        "lab11_kinds": "kind", "lab11_rules": "engaged", "lab11_dpo": "dpo", "lab11_note": "{'text': note}",
    },
    "D1_2_cut_extract": {
        "lab12_decision": "decision", "lab12_note_counts": "counts", "lab12_extract": "{'columns': list(extract.columns)}",
    },
    "D1_3_classify_control": {
        "lab13_datasets": "datasets", "lab13_outputs": "outputs", "lab13_joined": "{'level': joined}",
        "lab13_controls": "ctrl", "lab13_ai": "ok",
    },
    "D1_4_sharing_request": {
        "lab14_parties": "who", "lab14_tests": "tests", "lab14_form": "form", "lab14_conditions": "conds",
        "lab14_record": "record",
    },
    "D2_1_small_cells": {
        "lab21_small": "small", "lab21_leaked": "leaked", "lab21_after": "after",
        "lab21_mask3": "full3.to_dict()", "lab21_difference": "revealed",
    },
    "D2_2_bias_entry_points": {
        "lab22_points": "points", "lab22_gap": "gap", "lab22_missing": "missing", "lab22_order": "order",
    },
    "D2_3_group_rates": {
        "lab23_counts": "{g: t.to_dict('index') for g, t in table.items()}", "lab23_rates": "rt.to_dict('records')",
        "lab23_probe": "probe", "lab23_gaps": "gaps", "lab23_within": "inside.to_dict('records')",
        "lab23_sentences": "lines",
    },
    "D2_4_name_the_bias": {
        "lab24_candidates": "cand", "lab24_designs": "design", "lab24_check_a": "check_a",
        "lab24_check_b": "{' | '.join(k): v for k, v in check_b.items()}", "lab24_conclusions": "concl",
    },
}


def run(name: str, wanted: dict[str, str]) -> None:
    src = LABS / "_src" / f"{name}.py"
    ns: dict = {"__name__": "__lab__"}
    cwd = os.getcwd()
    os.chdir(LABS)
    try:
        exec(compile(src.read_text(encoding="utf-8"), str(src), "exec"), ns)
    finally:
        os.chdir(cwd)
    for ref, expr in wanted.items():
        value = eval(expr, ns)
        (REF / f"{ref}.json").write_text(json.dumps(value, ensure_ascii=False, indent=1, default=str) + "\n",
                                         encoding="utf-8", newline="\n")
        print("wrote", ref)


if __name__ == "__main__":
    sys.path.insert(0, str(LABS))
    REF.mkdir(parents=True, exist_ok=True)
    prefixes = sys.argv[1:]
    for name, wanted in REFS.items():
        if not prefixes or any(name.startswith(p) for p in prefixes):
            run(name, wanted)
