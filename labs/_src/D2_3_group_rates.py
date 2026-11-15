# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 2.3 · Rates with intervals
#
# Day 2 · Session 3 (Comparing groups) · 25 min.
#
# You compare what Awn does across four pairs of groups: how often it refers, how often it refers
# a student who did not struggle, and how often it misses one who did. Every rate and every
# difference gets a 95% interval, and one gap is checked inside colleges before anyone explains it.
#
# **Reference state.** `data/analysis_extract.csv`. Nothing from another lab.
#
# **Tasks**
# - [ ] 1 · Build the four outcome counts by group (5')
# - [ ] 2 · Compute the three rates with Wilson intervals (8')
# - [ ] 3 · Compute the differences with their intervals (5')
# - [ ] 4 · Check the gender gap inside each college (5')
# - [ ] 5 · Write the result in one sentence per gap (2')
# - [ ] ✱ Stretch · Compute the rates for one intersection of two groups and say what the interval allows you to claim

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

extract = U.load("analysis_extract.csv")
extract["referred"] = extract["awn_referred"] == "yes"
extract["struggled"] = extract["term_outcome"] == "struggled"
GROUPS = ["gender", "nationality_group", "disability_status", "first_generation"]
print(len(extract), "students ·", int(extract["referred"].sum()), "referred ·", int(extract["struggled"].sum()), "struggled")

# %% [markdown]
# ## 1 · Four counts per group (5')
#
# | | struggled | did not struggle |
# |---|---|---|
# | **referred** | caught | false referral |
# | **not referred** | missed | correctly left alone |
#
# ✏️ **Exercise** · Write `counts(df, group)`: one row per value of the group, with the columns
# `n`, `caught`, `false_referral`, `missed`, `left_alone`.

# %%
def counts(df: pd.DataFrame, group: str) -> pd.DataFrame:
    # BEGIN SOLUTION
    g = df.groupby(group)
    return pd.DataFrame({
        "n": g.size(),
        "caught": g.apply(lambda d: int((d["referred"] & d["struggled"]).sum()), include_groups=False),
        "false_referral": g.apply(lambda d: int((d["referred"] & ~d["struggled"]).sum()), include_groups=False),
        "missed": g.apply(lambda d: int((~d["referred"] & d["struggled"]).sum()), include_groups=False),
        "left_alone": g.apply(lambda d: int((~d["referred"] & ~d["struggled"]).sum()), include_groups=False),
    })
    # END SOLUTION

# %%
try:
    table = {g: counts(extract, g) for g in GROUPS}
except NotImplementedError:
    table = {g: pd.DataFrame(v).T for g, v in U.reference("lab23_counts").items()}
for g in GROUPS:
    print(table[g], "\n")
U.check(all(int(t[["caught", "false_referral", "missed", "left_alone"]].sum().sum()) == 18000 for t in table.values()),
        "the four counts add up to 18,000 in every breakdown")
U.check(int(table["disability_status"].loc["registered", "n"]) == 429, "429 students with a registered disability")

# %% [markdown]
# ## 2 · Three rates, each with an interval (8')
#
# - **referral rate** = referred / all
# - **false-referral rate** = false referrals / students who did not struggle
# - **missed rate** = missed / students who struggled
#
# ✏️ **Exercise** · Write `rates(c)`: from one row of counts, return each rate with its 95% Wilson
# interval, as `{"referral": (rate, low, high), "false_referral": (...), "missed": (...)}`.
# `U.wilson(k, n)` returns `(low, high)`.

# %%
def rates(c) -> dict[str, tuple[float, float, float]]:
    # BEGIN SOLUTION
    parts = {
        "referral": (c["caught"] + c["false_referral"], c["n"]),
        "false_referral": (c["false_referral"], c["false_referral"] + c["left_alone"]),
        "missed": (c["missed"], c["missed"] + c["caught"]),
    }
    return {name: (float(k) / float(n), *U.wilson(int(k), int(n))) for name, (k, n) in parts.items()}
    # END SOLUTION

# %%
def rate_table(table: dict) -> pd.DataFrame:
    rows = []
    for g, t in table.items():
        for value, c in t.iterrows():
            r = rates(c)
            rows.append({"group": g, "value": value, "n": int(c["n"]),
                         **{k: f"{v[0]:.1%} ({v[1]:.1%} to {v[2]:.1%})" for k, v in r.items()}})
    return pd.DataFrame(rows)

try:
    rt = rate_table(table)
    probe = rates(table["disability_status"].loc["registered"])
except NotImplementedError:
    rt = pd.DataFrame(U.reference("lab23_rates"))
    probe = {k: tuple(v) for k, v in U.reference("lab23_probe").items()}
print(rt.to_string(index=False))
U.check(0.33 < probe["false_referral"][0] < 0.36, "about 34% of students with a registered disability who did not struggle were referred")
U.check(probe["missed"][2] - probe["missed"][1] > 0.15, "their missed rate rests on 61 students: the interval is wide, and the table says so")

# %% [markdown]
# **Look at** the widths. The rates of 16,063 Saudi students are known to about a point. The
# missed rate of students with a registered disability rests on 61 struggling students and spans
# more than 15 points. A rate without its interval hides which of the two you are reading.

# %% [markdown]
# ## 3 · Differences, with intervals (5')
#
# ✏️ **Exercise** · Write `gap(table, group, a, b, rate)`: the difference of one rate between value
# `a` and value `b` of a group, with its 95% interval, using `U.diff_ci(k1, n1, k2, n2)`.

# %%
def numerator_denominator(c, rate: str) -> tuple[int, int]:
    return {"referral": (int(c["caught"] + c["false_referral"]), int(c["n"])),
            "false_referral": (int(c["false_referral"]), int(c["false_referral"] + c["left_alone"])),
            "missed": (int(c["missed"]), int(c["missed"] + c["caught"]))}[rate]

def gap(table: dict, group: str, a: str, b: str, rate: str) -> tuple[float, float, float]:
    # BEGIN SOLUTION
    k1, n1 = numerator_denominator(table[group].loc[a], rate)
    k2, n2 = numerator_denominator(table[group].loc[b], rate)
    return U.diff_ci(k1, n1, k2, n2)
    # END SOLUTION

# %%
COMPARISONS = [("gender", "F", "M", "referral"), ("disability_status", "registered", "none", "false_referral"),
               ("nationality_group", "non-Saudi", "Saudi", "missed"), ("first_generation", "yes", "no", "missed"),
               ("first_generation", "yes", "no", "false_referral")]
try:
    gaps = [{"group": g, "compare": f"{a} minus {b}", "rate": r, "difference": d, "low": lo, "high": hi}
            for g, a, b, r in COMPARISONS for d, lo, hi in [gap(table, g, a, b, r)]]
except NotImplementedError:
    gaps = U.reference("lab23_gaps")
for x in gaps:
    x["excludes_zero"] = bool(x["low"] > 0 or x["high"] < 0)
    print(f"{x['group']:18s} {x['compare']:22s} {x['rate']:15s} {x['difference']:+.1%}  ({x['low']:+.1%} to {x['high']:+.1%})"
          f"  {'clear' if x['excludes_zero'] else 'could be zero'}")
by = {(x["group"], x["rate"]): x for x in gaps}
U.check(by[("disability_status", "false_referral")]["low"] > 0.2, "false referrals: at least 20 points higher for students with a registered disability")
U.check(by[("nationality_group", "missed")]["low"] > 0.1, "missed students: at least 10 points higher for non-Saudi students")
U.check(not by[("first_generation", "missed")]["excludes_zero"], "first-generation students: no clear gap, and that is a finding too")

# %% [markdown]
# ## 4 · Does the gender gap survive inside colleges? (5')
#
# Women are referred more often than men overall, and the interval excludes zero. Before anyone
# explains that, check the obvious third variable: colleges differ in difficulty and in their
# share of women.
#
# ✏️ **Exercise** · Write `within(df, stratum, group, a, b)`: for each value of the stratum, the
# difference in referral rate between `a` and `b` with its interval.

# %%
def within(df: pd.DataFrame, stratum: str, group: str, a: str, b: str) -> pd.DataFrame:
    # BEGIN SOLUTION
    rows = []
    for value, d in df.groupby(stratum):
        da, db = d[d[group] == a], d[d[group] == b]
        diff, lo, hi = U.diff_ci(int(da["referred"].sum()), len(da), int(db["referred"].sum()), len(db))
        rows.append({stratum: value, "share_" + a: len(da) / len(d), "referral_rate": d["referred"].mean(),
                     "difference": diff, "low": lo, "high": hi})
    return pd.DataFrame(rows)
    # END SOLUTION

# %%
try:
    inside = within(extract, "college", "gender", "F", "M")
except NotImplementedError:
    inside = pd.DataFrame(U.reference("lab23_within"))
print(inside.round(3).to_string(index=False))
overall = by[("gender", "referral")]
print(f"\noverall: {overall['difference']:+.1%} ({overall['low']:+.1%} to {overall['high']:+.1%})")
U.check(overall["excludes_zero"], "overall, women are referred more often")
U.check(bool(((inside["low"] < 0) & (inside["high"] > 0)).all()), "inside every college the interval includes zero")
U.check(inside.sort_values("referral_rate").iloc[-1]["college"] == "Health Sciences", "the college with the highest referral rate also has the highest share of women")

# %% [markdown]
# **Look at** the two columns `share_F` and `referral_rate`. The overall gap is made by where
# women study, not by how the rule treats them. An analyst who reports the overall number alone
# has reported something true and misleading.

# %% [markdown]
# ## 5 · One sentence per gap (2')
#
# ✏️ **Exercise** · Write the three sentences: the gap, its size with the interval, and what is not
# yet known. No causes yet; those are Lab 2.4.

# %%
def sentences() -> list[str]:
    # BEGIN SOLUTION
    return [
        "Students with a registered disability who did not struggle were referred far more often than other students: 34% against 5%, a difference of 30 points (95% interval 25 to 35); the cause is not yet established.",
        "Awn missed 62% of struggling non-Saudi students against 43% of struggling Saudi students, a difference of 19 points (12 to 25); the cause is not yet established.",
        "Women were referred more often than men overall (12.3% against 10.5%), but inside each college the difference is small and its interval includes zero: the gap reflects where women study.",
    ]
    # END SOLUTION

# %%
try:
    lines = sentences()
except NotImplementedError:
    lines = U.reference("lab23_sentences")
for line in lines:
    print("-", line)
U.check(len(lines) == 3 and all("interval" in l or "(" in l for l in lines), "three sentences, each with its uncertainty")
out = Path("artifacts"); out.mkdir(exist_ok=True)
pd.DataFrame(gaps).to_csv(out / "lab23_gaps.csv", index=False)

# %% [markdown]
# ## ✱ Stretch · An intersection
#
# Compute the missed rate for non-Saudi women in Health Sciences. How many struggling students is
# it based on? What does the interval allow you to say, and would the unit's release policy let
# you publish the count?

# %% [markdown]
# ## Check yourself
#
# 1. Why three rates and not one "accuracy"?
# 2. The first-generation gap "could be zero". Do you report it?
# 3. Fairlearn's `MetricFrame` computes rates by group in one call. What would it not have told you?
#
# <details><summary>Answers</summary>
#
# 1. The two errors hurt differently: a false referral labels a student who was fine, a miss
#    leaves a struggling student alone. One number averages them away, and the two gaps found here
#    are in different errors.
# 2. Yes: "no clear difference, interval from x to y". Leaving out the comparisons that found
#    nothing makes the two that found something look selected.
# 3. Which comparisons to make, that the gender gap vanishes inside colleges, and why a gap
#    exists. A library computes; it does not choose the strata or the question.
# </details>
#
# **Carry forward.** The gaps table is the capstone's group comparison. Lab 2.4 starts from a
# supplied copy of it, `data/reference/lab23_gaps.json`.
