# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 2.4 · Two gaps, two names
#
# Day 2 · Session 4 (Naming the bias) · 25 min.
#
# The comparison found two clear gaps. A gap is an observation; a bias type is an explanation, and
# one gap usually has more than one candidate. For each gap you pick two bias types from SDAIA's
# AI Bias Reference Guide, design the check whose result would differ between them, run it, and
# record what you conclude and what stays open.
#
# **Reference state.** `data/reference/lab23_gaps.json` (the gaps of Lab 2.3, supplied),
# `data/bias_types.json`, `data/analysis_extract.csv` and `data/roll_call_audit.csv`. You do not
# need your own result of Lab 2.3.
#
# **Tasks**
# - [ ] 1 · Read the two gaps and their intervals (3')
# - [ ] 2 · Pick two candidate bias types for each gap (6')
# - [ ] 3 · Design the check that separates them (6')
# - [ ] 4 · Run the two checks (7')
# - [ ] 5 · Record the conclusion and what stays open (3')
# - [ ] ✱ Stretch · Change the rule to equalise false referrals and report what happens to missed students

# %%
import os, sys, subprocess
from pathlib import Path

IN_COLAB = "google.colab" in sys.modules
if IN_COLAB:
    REPO_URL = "https://github.com/SDAIAAcademy/ds-207.git"
    if not Path("/content/ds-207").exists():
        subprocess.run(["git", "clone", "-q", REPO_URL, "/content/ds-207"], check=True)
    os.chdir("/content/ds-207/labs")
else:
    while not Path("qimam.py").exists() and Path.cwd() != Path.cwd().parent:
        os.chdir("..")  # solutions/ notebooks run from labs/
sys.path.insert(0, os.getcwd())

import pandas as pd
import qimam as U
import json

BIAS_TYPES = U.json("bias_types.json")
NAMES = [b["type"] for b in BIAS_TYPES]
extract = U.load("analysis_extract.csv")
extract["attendance_rate"] = extract["attendance_rate"].astype(float)
extract["referred"] = extract["awn_referred"] == "yes"
extract["struggled"] = extract["term_outcome"] == "struggled"
audit = U.load("roll_call_audit.csv")

# %% [markdown]
# ## 1 · The two gaps (3')

# %%
supplied = json.loads((U.REF / "lab23_gaps.json").read_text(encoding="utf-8"))
GAPS = {"A": next(g for g in supplied if g["group"] == "disability_status"),
        "B": next(g for g in supplied if g["group"] == "nationality_group")}
for key, g in GAPS.items():
    print(f"Gap {key}: {g['rate']} rate, {g['compare']}: {g['difference']:+.1%} ({g['low']:+.1%} to {g['high']:+.1%})")

# %% [markdown]
# - **Gap A.** Students with a registered disability who did not struggle are referred far more
#   often than others.
# - **Gap B.** Struggling non-Saudi students are missed more often than struggling Saudi students.
#
# ## 2 · Two candidates per gap (6')
#
# Ten entries of the guide, each in one line (our wording; read the guide's own definition,
# example and mitigation before you use a name in a report):

# %%
for b in BIAS_TYPES:
    print(f"{b['type']:20s} {b['in_short']}")

# %% [markdown]
# ✏️ **Exercise** · Return two candidate types for each gap. Choose candidates that are both
# plausible and that would call for **different fixes**; that is what makes separating them
# worth a check.

# %%
def candidates() -> dict[str, list[str]]:
    # BEGIN SOLUTION
    return {
        "A": ["measurement bias", "aggregation bias"],
        "B": ["coverage bias", "aggregation bias"],
    }
    # END SOLUTION

# %%
try:
    cand = candidates()
except NotImplementedError:
    cand = U.reference("lab24_candidates")
U.check(all(len(set(v)) == 2 and set(v) <= set(NAMES) for v in cand.values()), "two different types from the guide for each gap")
print(cand)

# %% [markdown]
# The reasoning behind the reference answer. **Gap A:** either attendance is *recorded* too low
# for these students (measurement: fix the record), or it is recorded correctly and one limit of
# 75% does not fit students whose approved pattern of attendance differs (aggregation: fix the
# rule). **Gap B:** either the data does not cover these students (marks missing: fix the feed),
# or it covers them and one pair of limits does not fit them (aggregation: fix the rule).

# %% [markdown]
# ## 3 · The check that separates them (6')
#
# ✏️ **Exercise** · For each gap, write the check and the result each candidate predicts. A check is
# useful only if the two predictions differ.

# %%
def designs() -> dict[str, dict]:
    # BEGIN SOLUTION
    return {
        "A": {"check": "Compare the card record with the instructors' roll call for audited students, and compute the false-referral rate of students with a registered disability separately for those with and without a remote accommodation.",
              "if_first": "The record is far below the roll call for remote-accommodation students, and the gap in false referrals is confined to them.",
              "if_second": "The record matches the roll call, and false referrals are high for all students with a registered disability."},
        "B": {"check": "Split struggling students by whether a midterm mark is in the registry, and compare the missed rate of non-Saudi and Saudi students inside each part.",
              "if_first": "Inside each part the two groups are missed about equally; the gap comes from more non-Saudi students having no mark.",
              "if_second": "Non-Saudi students are missed more often even when their marks are present."},
    }
    # END SOLUTION

# %%
try:
    design = designs()
except NotImplementedError:
    design = U.reference("lab24_designs")
U.check(all(d["if_first"] != d["if_second"] and len(d["check"]) > 40 for d in design.values()), "each check has two different predictions")
for key, d in design.items():
    print(f"Gap {key}\n  check: {d['check']}\n  if {cand[key][0]}: {d['if_first']}\n  if {cand[key][1]}: {d['if_second']}\n")

# %% [markdown]
# ## 4 · Run the checks (7')
#
# ✏️ **Exercise** · Write `false_referral(df)` and `missed(df)`: each returns `(rate, low, high)` for
# the rows it is given, with `U.wilson`. The cells below apply them to the right subgroups.

# %%
def false_referral(df: pd.DataFrame) -> tuple[float, float, float]:
    # BEGIN SOLUTION
    fine = df[~df["struggled"]]
    k, n = int(fine["referred"].sum()), len(fine)
    return (k / n, *U.wilson(k, n))
    # END SOLUTION

def missed(df: pd.DataFrame) -> tuple[float, float, float]:
    # BEGIN SOLUTION
    s = df[df["struggled"]]
    k, n = int((~s["referred"]).sum()), len(s)
    return (k / n, *U.wilson(k, n))
    # END SOLUTION

# %%
def fmt(r):
    return f"{r[0]:.1%} ({r[1]:.1%} to {r[2]:.1%})"

reg = extract[extract["disability_status"] == "registered"]
try:
    check_a = {"registered, remote accommodation": false_referral(reg[reg["remote_accommodation"] == "yes"]),
               "registered, no remote accommodation": false_referral(reg[reg["remote_accommodation"] == "no"]),
               "no registered disability": false_referral(extract[extract["disability_status"] == "none"])}
except NotImplementedError:
    check_a = {k: tuple(v) for k, v in U.reference("lab24_check_a").items()}
j = audit.merge(extract, on="pid")
record_gap = (j["roll_call_rate"].astype(float) - j["attendance_rate"]).groupby(j["remote_accommodation"]).mean().round(3).to_dict()
print("Check A · false-referral rate")
for k, v in check_a.items():
    print(f"  {k:38s} {fmt(v)}")
print("  roll call minus card record:", record_gap)
U.check(check_a["registered, remote accommodation"][1] > 0.4, "with a remote accommodation: more than 40% referred without need")
U.check(check_a["registered, no remote accommodation"][1] < check_a["no registered disability"][0] < check_a["registered, no remote accommodation"][2],
        "without one: the same rate as everyone else, within the interval")

# %%
extract["has_mark"] = extract["midterm_gpa"] != ""
try:
    check_b = {(grp, "mark present" if has else "mark missing"): missed(d)
               for (grp, has), d in extract.groupby(["nationality_group", "has_mark"])}
except NotImplementedError:
    check_b = {tuple(k.split(" | ")): tuple(v) for k, v in U.reference("lab24_check_b").items()}
print("Check B · missed rate among struggling students")
for k, v in sorted(check_b.items(), key=lambda kv: (kv[0][1], kv[0][0])):
    print(f"  {k[1]:13s} {k[0]:10s} {fmt(v)}")
ns_p, sa_p = check_b[("non-Saudi", "mark present")], check_b[("Saudi", "mark present")]
ns_m, sa_m = check_b[("non-Saudi", "mark missing")], check_b[("Saudi", "mark missing")]
U.check(ns_p[1] < sa_p[0] < ns_p[2], "marks present: non-Saudi and Saudi students are missed at the same rate, within the interval")
U.check(ns_m[0] > 0.7 and sa_m[0] > 0.7, "marks missing: more than 70% missed in both groups")

# %% [markdown]
# **Look at** both results against your predictions. Gap A is confined to students whose
# attendance is under-recorded. Gap B disappears when you compare like with like, and reappears,
# for Saudi students too, wherever the mark is missing.

# %% [markdown]
# ## 5 · Conclusion and what stays open (3')
#
# ✏️ **Exercise** · Record the conclusion for each gap: the type the evidence supports, the fix it
# points to, and one thing the check did not settle.

# %%
def conclusions() -> dict[str, dict]:
    # BEGIN SOLUTION
    return {
        "A": {"supported": "measurement bias",
              "evidence": "The card record is about 17 points below the roll call for students with a remote accommodation; their false-referral rate is 59% against 4% for other students with a registered disability.",
              "fix": "Feed approved remote attendance into the record, or exclude the attendance signal for these students until it is.",
              "open": "The 187 students with a registered disability and no remote accommodation are a small group: a moderate gap for them could hide inside the interval."},
        "B": {"supported": "coverage bias",
              "evidence": "With a mark present, non-Saudi and Saudi students are missed at similar rates; with the mark missing, both are missed more than 70% of the time.",
              "fix": "Bring the bridging programme's midterm marks into the registry; until then report bridging-year entrants separately.",
              "open": "Whether the limits of 2023 fit bridging-year entrants once their marks are present cannot be known before the marks exist."},
    }
    # END SOLUTION

# %%
try:
    concl = conclusions()
except NotImplementedError:
    concl = U.reference("lab24_conclusions")
U.check(concl["A"]["supported"] == "measurement bias" and concl["B"]["supported"] == "coverage bias", "the evidence supports measurement bias for A and coverage bias for B")
U.check(all(len(c["open"]) > 20 and len(c["fix"]) > 20 for c in concl.values()), "each conclusion names a fix and what stays open")
out = Path("artifacts"); out.mkdir(exist_ok=True)
(out / "lab24_bias_findings.json").write_text(json.dumps({"candidates": cand, "designs": design, "conclusions": concl}, indent=1), encoding="utf-8")
U.table([{"gap": k, **v} for k, v in concl.items()])

# %% [markdown]
# ## ✱ Stretch · Equalise one error
#
# Change the rule so that students with a remote accommodation are referred on the midterm mark
# only. Recompute both error rates for students with a registered disability. Which error fell,
# which rose, and who should decide whether that trade is acceptable?

# %% [markdown]
# ## Check yourself
#
# 1. Nationality showed Gap B, yet the cause is the admission route. Why does that matter for the fix?
# 2. Both checks used fields the Awn evaluation itself did not need. What made that lawful?
# 3. After both fixes, will Awn be fair?
#
# <details><summary>Answers</summary>
#
# 1. A fix aimed at nationality (a different limit for non-Saudi students) would treat students
#    by a protected characteristic and miss Saudi bridging-year entrants. A fix aimed at the feed
#    repairs it for everyone.
# 2. A separate, recorded decision: the data protection officer approved the group fields for
#    this comparison, on the pseudonymised extract, reported in aggregate (log entry L002).
# 3. It will have two known errors fewer. Whether equal false-referral rates or equal missed
#    rates matter more, and how large a remaining gap is acceptable, is not a statistical
#    question: the unit's director and the data protection officer decide it, on your numbers.
# </details>
#
# **Carry forward.** `artifacts/lab24_bias_findings.json` is the model for the second half of the
# capstone's group comparison: two candidates, the check, the result, what stays open.
