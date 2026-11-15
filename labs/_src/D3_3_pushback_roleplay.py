# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 3.3 · The risk list
#
# Day 3 · Session 3 (Pushing back without obstructing) · 25 min.
#
# The vice-rector asks for a named list of every student likely to fail, with a risk score, for
# herself and the deans. You prepare two lawful alternatives with real numbers, then role-play the
# conversation three times in threes, so everyone plays the analyst. The observer scores the
# analyst on five behaviours. You end with the written record: what was agreed, what was refused
# and why, and what goes to the data protection officer. No AI assistant in this lab.
#
# **Reference state.** `data/risk_list_request.json` and `data/analysis_extract.csv`. Nothing from
# another lab.
#
# **Tasks**
# - [ ] 1 · Read the request and prepare two alternatives (5')
# - [ ] 2 · Round 1: analyst, sponsor, observer (5')
# - [ ] 3 · Round 2: rotate the roles (5')
# - [ ] 4 · Round 3: rotate the roles (5')
# - [ ] 5 · Record the agreement and the escalation (5')
# - [ ] ✱ Stretch · The sponsor insists: write the three-line escalation to the data protection officer

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

pack = U.json("risk_list_request.json")
REQUEST, ALTERNATIVES, RUBRIC = pack["request"], pack["alternatives"], pack["observer_rubric"]
extract = U.load("analysis_extract.csv")

# %% [markdown]
# ## 1 · The request, and what you can offer instead (5')

# %%
print(f"{REQUEST['sponsor']}:\n   \"{REQUEST['request']}\"\n")
print("What she has to decide:", REQUEST["what_she_wants_to_decide"], "\n")
print("Why the list is unsafe:")
for w in REQUEST["why_it_is_unsafe"]:
    print("  -", w)
print()
for a in ALTERNATIVES:
    print(f"{a['id']} · {a['title']}: {a['what']}")

# %% [markdown]
# A good alternative passes two tests: it **serves the sponsor's decision**, and **no named list
# leaves the advisors** who act on it.
#
# ✏️ **Exercise** · Return the ids of the two alternatives that pass both tests.

# %%
def choose() -> list[str]:
    # BEGIN SOLUTION
    return [a["id"] for a in ALTERNATIVES if a["serves_decision"] and not a["names_leave_advising"]]
    # END SOLUTION

# %%
try:
    chosen = choose()
except NotImplementedError:
    chosen = U.reference("lab33_chosen")
print("offer:", chosen)
U.check(sorted(chosen) == ["A1", "A2"], "counts for the vice-rector, worklists stay with advisors")

# %% [markdown]
# An alternative you can show beats one you can describe. Build A1 now: referred and struggling
# students by college, checked against the release threshold. This is the table that
# places twelve advisors.
#
# ✏️ **Exercise** · Write `advisor_table(extract)`: one row per college, with the columns
# `students`, `referred`, `struggled` and `missed` (struggled and not referred).

# %%
def advisor_table(extract: pd.DataFrame) -> pd.DataFrame:
    # BEGIN SOLUTION
    d = extract.assign(referred=extract["awn_referred"] == "yes", struggled=extract["term_outcome"] == "struggled")
    d["missed"] = d["struggled"] & ~d["referred"]
    return d.groupby("college").agg(students=("pid", "size"), referred=("referred", "sum"),
                                    struggled=("struggled", "sum"), missed=("missed", "sum")).astype(int)
    # END SOLUTION

# %%
try:
    a1 = advisor_table(extract)
except NotImplementedError:
    a1 = pd.DataFrame(U.reference("lab33_a1")).T
a1["advisors_of_12"] = (12 * a1["struggled"] / a1["struggled"].sum()).round(1)
print(a1)
U.check(int(a1["students"].sum()) == 18000 and int(a1.drop(columns="advisors_of_12").values.min()) >= U.THRESHOLD, "every cell is 10 or more: the table can go to the vice-rector")
U.check(a1["advisors_of_12"].idxmax() == "Health Sciences", "the table answers her question: Health Sciences needs the most advisors")

# %% [markdown]
# ## 2 · Round 1 (5')
#
# Name yourselves P1, P2, P3. Three minutes of conversation, two of feedback from the observer.
#
# - **The sponsor** opens with the request and uses the three pressures, one at a time. She gives
#   way only when she hears something that serves her decision.
# - **The analyst** has the table above and the two alternatives.
# - **The observer** scores five behaviours: 0 not seen, 1 partly, 2 clearly.

# %%
print("SPONSOR · pressures to use, one at a time:")
for p in REQUEST["pressures"]:
    print("  -", p)
print("\nOBSERVER · score each 0, 1 or 2:")
for r in RUBRIC:
    print(f"  [ ] {r['id']:12s} {r['text']}")

def total(scores: dict[str, int]) -> int:
    assert set(scores) == {r["id"] for r in RUBRIC} and all(v in (0, 1, 2) for v in scores.values())
    return sum(scores.values())

round1 = {"listen": 2, "harm": 1, "rule": 2, "alternative": 2, "record": 1}   # the observer replaces these
print("\nscore of round 1:", total(round1), "of 10")

# %% [markdown]
# ## 3 · Round 2 (5')
#
# Rotate: P2 is the analyst, P3 the sponsor, P1 the observer. The sponsor may add a pressure of
# her own.

# %%
round2 = {"listen": 2, "harm": 2, "rule": 1, "alternative": 2, "record": 2}   # the observer replaces these
print("score of round 2:", total(round2), "of 10")

# %% [markdown]
# ## 4 · Round 3 (5')
#
# Rotate: P3 is the analyst, P1 the sponsor, P2 the observer.

# %%
round3 = {"listen": 1, "harm": 2, "rule": 2, "alternative": 2, "record": 2}   # the observer replaces these
print("score of round 3:", total(round3), "of 10")

# %% [markdown]
# ## 5 · The record (5')
#
# What is not written down was not agreed. ✏️ **Exercise** · Return the record of your own round as
# analyst: what will be delivered and when, what will not and why (the harm in plain words and the
# rule), who confirms, and what goes to the data protection officer.

# %%
def agreement() -> dict[str, str]:
    # BEGIN SOLUTION
    return {
        "asked_for": "A named list of every student likely to fail, with a risk score, for the vice-rector and the deans.",
        "will_deliver": "By Sunday: referred, struggling and missed students by college, with the share of referred students contacted by an advisor within two weeks. No cell under 10.",
        "will_not_deliver": "Names or scores of individual students outside the advisors who contact them.",
        "why": "A list of predicted failure that reaches deans can follow a student into grading and discipline, and the rule is known to be wrong for two groups. Students were told their data is used for advice and support; a list for deans is a new purpose.",
        "who_decides_more": "If named data is still needed, the data protection officer decides: the request goes to Shatha Al-Omair with this record.",
        "confirmed_by": "Dr. Ibtisam Al-Khayyat, by reply to this note.",
    }
    # END SOLUTION

# %%
try:
    record = agreement()
except NotImplementedError:
    record = U.reference("lab33_record")
low = {k: v.lower() for k, v in record.items()}
U.check(all(len(v) > 20 for v in record.values()) and len(record) == 6, "six fields, each a full sentence")
U.check("name" in low["will_not_deliver"], "the record says plainly that names are not delivered")
U.check("student" in low["why"] and ("purpose" in low["why"] or "notice" in low["why"] or "told" in low["why"]), "the reason names the harm to students and the rule")
U.check("data protection officer" in low["who_decides_more"], "the escalation route is written down")
U.check(any(ch.isdigit() for ch in record["will_deliver"]) or "sunday" in low["will_deliver"], "the delivery has a date or a number")
out = Path("artifacts"); out.mkdir(exist_ok=True)
(out / "lab33_agreement.json").write_text(json.dumps(record, indent=1, ensure_ascii=False), encoding="utf-8")
U.table([{"field": k.replace("_", " "), "record": v} for k, v in record.items()])

# %% [markdown]
# ## ✱ Stretch · The escalation
#
# The sponsor says: "Send me the list. That is an instruction." Write three lines to the data
# protection officer: what was asked and by whom, what you offered, and the decision you need
# from her. Copy the sponsor. Why copy her?

# %% [markdown]
# ## Check yourself
#
# 1. The vice-rector is senior and is allowed to see student data. Why is that not the end of it?
# 2. Why offer the alternative before explaining the rule?
# 3. Is escalating to the data protection officer going behind the sponsor's back?
#
# <details><summary>Answers</summary>
#
# 1. Access follows the purpose and the need to know, not rank. She does not advise students, and
#    her decision (where to put advisors) does not need names.
# 2. She came with a problem. Someone who hears first how her problem gets solved by Sunday can
#    listen to the reason; someone who hears a rule first hears a refusal.
# 3. Not when it is said aloud and she is copied. The decision is not the analyst's and not the
#    sponsor's; saying whose it is protects both.
# </details>
#
# **Carry forward.** The agreement is the model for the last section of the capstone's scope
# note, and this conversation is the role-play inside the capstone defence.
