# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 2.2 · Four entry points
#
# Day 2 · Session 2 (Where bias enters) · 25 min.
#
# Before comparing any rates, you walk the path of Awn's data from the event in a teaching room to
# the report on the director's desk, and mark where a systematic error could enter. Then you stop
# arguing and measure two of the points with data: the attendance record against an audit of
# instructors' roll calls, and the midterm marks that are missing.
#
# **Reference state.** `data/awn_pipeline.json`, `data/analysis_extract.csv` (the pseudonymised
# extract with the group fields the data protection officer approved) and
# `data/roll_call_audit.csv`. Nothing from another lab.
#
# **Tasks**
# - [ ] 1 · Trace Awn's data from the event to the referral (5')
# - [ ] 2 · Mark four points where bias can enter (8')
# - [ ] 3 · Measure the attendance record against the roll-call audit (6')
# - [ ] 4 · Measure missing midterm marks by group (4')
# - [ ] 5 · Rank which entry point to check first (2')
# - [ ] ✱ Stretch · Find a fifth entry point after the referral: who takes up the support that is offered

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

PIPELINE = U.json("awn_pipeline.json")
extract = U.load("analysis_extract.csv")
audit = U.load("roll_call_audit.csv")
extract["attendance_rate"] = extract["attendance_rate"].astype(float)

# %% [markdown]
# ## 1 · The path of the data (5')
#
# Six stages. Read each one and ask: for whom could this step go wrong more often than for others?

# %%
for s in PIPELINE:
    print(f"{s['id']} · {s['stage']}\n     {s['what_happens']}\n")
print("group fields in the extract:", [c for c in extract.columns if c in
      ("gender", "nationality_group", "disability_status", "first_generation", "remote_accommodation", "admission_route")])

# %% [markdown]
# ## 2 · Mark four points (8')
#
# ✏️ **Exercise** · For at least four stages, write what could go wrong and for which students.
# Use the key `"how"` for the mechanism and `"who"` for the group. A good entry is specific enough
# to be measured: "attendance may be biased" is not; "remote sessions leave no card reading, so
# students with a remote accommodation look absent" is.

# %%
def entry_points() -> dict[str, dict]:
    # BEGIN SOLUTION
    return {
        "S1": {"how": "Remote sessions leave no card reading, so recorded attendance is lower than true attendance.",
               "who": "students with an approved remote accommodation, most of them with a registered disability"},
        "S2": {"how": "Marks kept in the bridging programme's system never reach the registry, so the rule sees no midterm mark and cannot fire on it.",
               "who": "bridging-year entrants in their first two years, many of them non-Saudi students"},
        "S3": {"how": "Limits set on two colleges in 2023 may not fit colleges with different attendance habits or grading.",
               "who": "students of the four colleges that were not in the 2023 records"},
        "S4": {"how": "A student who withdraws after two easy courses keeps a good average and is labelled 'ok'.",
               "who": "students who withdraw during the term"},
        "S5": {"how": "Support that works turns a correct referral into an apparent false alarm.",
               "who": "referred students in colleges where advisors act quickly"},
        "S6": {"how": "One rate for the whole University hides a rule that works well for most and badly for a small group.",
               "who": "any small group: 429 students have a registered disability"},
    }
    # END SOLUTION

# %%
try:
    points = entry_points()
except NotImplementedError:
    points = U.reference("lab22_points")
U.check(len(points) >= 4 and set(points) <= {s["id"] for s in PIPELINE}, "at least four of the six stages are marked")
U.check(all(len(p["how"]) > 25 and len(p["who"]) > 5 for p in points.values()), "each entry says how and for whom")
U.check({"S1", "S2"} <= set(points), "the two stages you are about to measure are among them")
U.table([{"stage": k, **v} for k, v in points.items()])

# %% [markdown]
# ## 3 · Measure S1: the attendance record (6')
#
# For an audit, instructors kept a roll call for 1,600 students: all 300 with a remote
# accommodation and 1,300 others drawn at random. The roll call counts remote attendance.
#
# ✏️ **Exercise** · Write `recording_gap(extract, audit)`: join the audit to the extract on `pid`,
# compute `roll_call_rate - attendance_rate` per student, and return the mean gap for
# `remote_accommodation` "yes" and "no".

# %%
def recording_gap(extract: pd.DataFrame, audit: pd.DataFrame) -> dict[str, float]:
    # BEGIN SOLUTION
    j = audit.merge(extract[["pid", "attendance_rate", "remote_accommodation"]], on="pid")
    j["gap"] = j["roll_call_rate"].astype(float) - j["attendance_rate"]
    return {k: round(float(v), 3) for k, v in j.groupby("remote_accommodation")["gap"].mean().items()}
    # END SOLUTION

# %%
try:
    gap = recording_gap(extract, audit)
except NotImplementedError:
    gap = U.reference("lab22_gap")
print("mean of roll call minus card record:", gap)
U.check(abs(gap["no"]) < 0.01, "for other students the card record matches the roll call")
U.check(gap["yes"] > 0.15, "for students with a remote accommodation the record is about 17 points too low")

# %% [markdown]
# **Look at** what 17 points does to a rule with a limit at 75%: a student who truly attends 88%
# is recorded at 71% and referred.

# %%
j = audit.merge(extract, on="pid")
j["true_rate"] = j["roll_call_rate"].astype(float)
remote = j[j["remote_accommodation"] == "yes"]
moved = {"students": len(remote), "recorded_below_limit": int((remote["attendance_rate"] < 0.75).sum()),
         "truly_below_limit": int((remote["true_rate"] < 0.75).sum())}
print(moved)
U.check(moved["recorded_below_limit"] > 5 * max(1, moved["truly_below_limit"]), "most of them are below the limit only on paper")

# %% [markdown]
# ## 4 · Measure S2: the missing marks (4')
#
# ✏️ **Exercise** · Write `missing_marks(extract)`: the share of students with no midterm mark, by
# `nationality_group`, as a number between 0 and 1.

# %%
def missing_marks(extract: pd.DataFrame) -> dict[str, float]:
    # BEGIN SOLUTION
    share = (extract["midterm_gpa"] == "").groupby(extract["nationality_group"]).mean()
    return {k: round(float(v), 3) for k, v in share.items()}
    # END SOLUTION

# %%
try:
    missing = missing_marks(extract)
except NotImplementedError:
    missing = U.reference("lab22_missing")
print("share with no midterm mark:", missing)
by_route = pd.crosstab(extract["admission_route"], extract["midterm_gpa"] == "")
print(by_route)
U.check(missing["non-Saudi"] > 0.3 and missing["Saudi"] < 0.05, "over a third of non-Saudi students have no mark; about 3% of Saudi students")
U.check(int(by_route.loc["direct", True]) == 0, "every missing mark belongs to a bridging-year entrant")

# %% [markdown]
# **Look at** the second table. The mark is missing because of the admission route, not because of
# nationality. Nationality is where you will see the effect; the route is where it comes from.

# %% [markdown]
# ## 5 · Which first? (2')
#
# ✏️ **Exercise** · Return the two stages to check first in tomorrow's group comparison, most urgent
# first, with one reason each. Weigh how many students are affected against how wrong the rule
# gets for each of them.

# %%
def first_checks() -> list[tuple[str, str]]:
    # BEGIN SOLUTION
    return [
        ("S2", "1,244 students have no mark, so half of the rule cannot fire for them: struggling students are missed"),
        ("S1", "300 students are recorded about 17 points low: most of their referrals are false, and a false referral labels a student"),
    ]
    # END SOLUTION

# %%
try:
    order = first_checks()
except NotImplementedError:
    order = [tuple(x) for x in U.reference("lab22_order")]
for stage, why in order:
    print(stage, "·", why)
U.check({s for s, _ in order} == {"S1", "S2"}, "the two measured stages come first; either order can be defended")
n_missing = int((extract["midterm_gpa"] == "").sum())
print("students with no mark:", n_missing, "· students with a remote accommodation:", int((extract["remote_accommodation"] == "yes").sum()))

# %% [markdown]
# ## ✱ Stretch · After the referral
#
# Awn's output is a referral; the benefit is support that a student takes up. Who is less likely
# to answer an advisor's call or come to an appointment during working hours? Which data would
# show it, and is the unit allowed to collect it?

# %% [markdown]
# ## Check yourself
#
# 1. Neither S1 nor S2 involves anyone intending to treat a group differently. Is it still bias?
# 2. Why measure with the roll-call audit instead of asking instructors whether the record is fair?
# 3. Stage S5 makes the rule look worse where support works. What would you need to separate
#    "false alarm" from "helped"?
#
# <details><summary>Answers</summary>
#
# 1. Yes. Bias here means a systematic error that falls on some groups more than others. It needs
#    no intent, only a process that records or covers people unequally.
# 2. A measurement gives a size (17 points), a group (300 students) and a consequence (referrals
#    below the limit on paper only). An opinion gives none of the three.
# 3. A comparison group that was referred and not contacted, or a staggered start. The unit has
#    neither, which is a limit to state on Day 3, not to hide.
# </details>
#
# **Carry forward.** Lab 2.3 compares the rule's errors by group; Lab 2.4 uses the two
# measurements of this lab as the checks that separate one bias type from another.
