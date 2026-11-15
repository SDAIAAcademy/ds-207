"""Shared helpers for the DS-207 labs (Al-Qimam University, synthetic data).

    import qimam as U

U.DATA            the data folder (labs/data)
U.QUICK           True when DS207_QUICK=1: smaller runs where a lab resamples
U.pick(a, b)      a normally, b in quick mode
U.load(name)      a CSV of labs/data as a pandas DataFrame (text kept as text)
U.json(name)      a JSON file of labs/data
U.text(name)      a text file of labs/data
U.reference(n)    the reference result of an exercise, for the safety-net cells
U.check(ok, m)    prints a tick or raises AssertionError with the message
U.table(rows)     a list of dicts as a DataFrame, for display
U.wilson(k, n)    the 95% Wilson interval of a proportion k / n, as (low, high)
U.diff_ci(...)    the 95% interval of a difference of two proportions (Newcombe)
U.pseudonym(id)   the project pseudonym of a student number
U.THRESHOLD       the release threshold of the unit's policy: no count of 1 to 9
"""

from __future__ import annotations

import hashlib
import hmac
import json as _json
import math
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REF = DATA / "reference"
QUICK = os.environ.get("DS207_QUICK", "0") == "1"
THRESHOLD = 10
PROJECT_KEY = "awn-evaluation-2026-t1-lab-key"
Z95 = 1.959964


def pick(full, quick):
    return quick if QUICK else full


def load(name: str):
    import pandas as pd
    return pd.read_csv(DATA / name, dtype=str, keep_default_na=False)


def json(name: str):
    return _json.loads((DATA / name).read_text(encoding="utf-8"))


def text(name: str) -> str:
    return (DATA / name).read_text(encoding="utf-8")


def reference(name: str):
    """The reference result of exercise `name`, so later cells run when it is not done yet."""
    print(f"(safety net: using the reference result for {name})")
    return _json.loads((REF / f"{name}.json").read_text(encoding="utf-8"))


def check(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError("not yet: " + message)
    print("✅", message)


def table(rows, columns=None):
    import pandas as pd
    return pd.DataFrame(rows, columns=columns)


def wilson(k: int, n: int, z: float = Z95) -> tuple[float, float]:
    """The Wilson score interval of the proportion k / n."""
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return (max(0.0, centre - half), min(1.0, centre + half))


def diff_ci(k1: int, n1: int, k2: int, n2: int) -> tuple[float, float, float]:
    """p1 - p2 with its 95% interval (Newcombe's method, from the two Wilson intervals)."""
    p1, p2 = k1 / n1, k2 / n2
    l1, u1 = wilson(k1, n1)
    l2, u2 = wilson(k2, n2)
    d = p1 - p2
    return (d, d - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2), d + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2))


def pseudonym(student_id: str, key: str = PROJECT_KEY) -> str:
    return "P" + hmac.new(key.encode(), student_id.encode(), hashlib.sha256).hexdigest()[:10]
