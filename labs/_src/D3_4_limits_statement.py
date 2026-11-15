# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 3.4 · Three sentences and the capstone case
#
# Day 3 · Session 4 (Explaining limits) · 25 min.
#
# The evaluation of Awn has one headline number. You state what the analysis cannot show, write
# the three-sentence limits statement that travels with the number, test it against four ways a
# reader could misread it, and then choose the engagement for your capstone pack.
#
# **Reference state.** `data/limits_result.json`, `data/analysis_extract.csv` and the three
# folders under `capstone/`. Nothing from another lab.
#
# **Tasks**
# - [ ] 1 · Read the result and its interval (3')
# - [ ] 2 · List what the analysis cannot show (5')
# - [ ] 3 · Write the three-sentence limits statement (7')
# - [ ] 4 · Test it against four misreadings (5')
# - [ ] 5 · Choose the capstone engagement and open its files (5')
# - [ ] ✱ Stretch · Rewrite the statement for a student newspaper, without a number that could mislead

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
import re

RESULT = U.json("limits_result.json")
extract = U.load("analysis_extract.csv")

# %% [markdown]
# ## 1 · The result (3')

# %%
struggled = extract[extract["term_outcome"] == "struggled"]
caught = int((struggled["awn_referred"] == "yes").sum())
low, high = U.wilson(caught, len(struggled))
print(RESULT["claim"])
print(f"95% interval: {low:.1%} to {high:.1%}")
U.check(caught == 1209 and len(struggled) == 2191, "1,209 of 2,191 struggling students were referred")

# %% [markdown]
# **Look at** the interval: about two points either way. Uncertainty from sampling is small here.
# The limits that matter are of another kind: what the number does not measure at all.

# %% [markdown]
# ## 2 · What the analysis cannot show (5')
#
# Eight statements. Some are real limits of this analysis; some sound like limits and are not.
#
# ✏️ **Exercise** · Return the letters of the real limits.

# %%
STATEMENTS = {
    "a": "It did not test whether support helps: every referred student was contacted, so there is no comparison group.",
    "b": "It covers one term of one year.",
    "c": "Attendance is under-recorded for students with a remote accommodation, so most of their referrals are false.",
    "d": "Midterm marks are missing for bridging-year entrants, so most of their struggling students are missed.",
    "e": "With 18,000 students the sample is too small to estimate the overall rate.",
    "f": "'Struggled' is a term average below 2.5; students who withdraw during the term can be labelled 'ok'.",
    "g": "The rates are unreliable because the extract is pseudonymised.",
    "h": "It describes groups; it says nothing reliable about the risk of any one student.",
}
for k, v in STATEMENTS.items():
    print(k, "·", v)

def real_limits() -> list[str]:
    # BEGIN SOLUTION
    return ["a", "b", "c", "d", "f", "h"]
    # END SOLUTION

# %%
try:
    limits = real_limits()
except NotImplementedError:
    limits = U.reference("lab34_limits")
U.check("e" not in limits, "18,000 students estimate the overall rate to about two points: size is not the limit")
U.check("g" not in limits, "a pseudonym changes who can be identified, not any rate")
U.check(set(limits) == {"a", "b", "c", "d", "f", "h"}, "six real limits")

# %% [markdown]
# ## 3 · Three sentences (7')
#
# The statement travels with the number, in the report, on the slide, in the email. Three
# sentences, one job each:
#
# 1. **What it shows**, with the number and its uncertainty.
# 2. **What it does not show**, and for whom it is known to be worse.
# 3. **What it must not be used for.**
#
# ✏️ **Exercise** · Write the statement for a reader who is not a specialist. No more than 90 words.

# %%
def limits_statement() -> str:
    # BEGIN SOLUTION
    return (
        "In term 1, Awn referred 55% of the students who ended the term struggling (between 53% and 57%), so it missed 45% of them. "
        "The analysis did not test whether the support that follows a referral helps, and the rule is known to be less reliable for two groups: "
        "it wrongly refers many students with a remote-attendance accommodation and misses most struggling bridging-year entrants. "
        "The result describes groups of students and must not be used to judge, rank or list any individual student."
    )
    # END SOLUTION

# %%
try:
    statement = limits_statement()
except NotImplementedError:
    statement = U.reference("lab34_statement")["text"]
sentences = [s for s in re.split(r"(?<=[.!?])\s+", statement.strip()) if s]
print(statement, "\n")
print(len(sentences), "sentences,", len(statement.split()), "words")
U.check(len(sentences) == 3, "exactly three sentences")
U.check(len(statement.split()) <= 90, "no more than 90 words")
U.check("%" in sentences[0], "the first sentence carries the number")
U.check("must not" in sentences[2].lower(), "the third sentence says what the result must not be used for")

# %% [markdown]
# ## 4 · Four misreadings (5')
#
# A limits statement works if it blocks the ways a hurried reader will misread the number.
# ✏️ **Exercise** · For each misreading, return the number of the sentence (1, 2 or 3) that blocks it.

# %%
for m in RESULT["misreadings"]:
    print(m["id"], "·", m["text"])

def blocked_by() -> dict[str, int]:
    # BEGIN SOLUTION
    return {"M1": 2, "M2": 1, "M3": 2, "M4": 3}
    # END SOLUTION

# %%
NEEDS = {"M1": ["help", "support"], "M2": ["missed"], "M3": ["remote", "bridging", "group"], "M4": ["must not"]}
try:
    blocks = blocked_by()
except NotImplementedError:
    blocks = U.reference("lab34_blocks")
for mid, n in blocks.items():
    ok = any(word in sentences[n - 1].lower() for word in NEEDS[mid])
    print(f"{mid}: sentence {n} {'blocks it' if ok else 'does NOT block it'}")
    U.check(ok, f"{mid} is blocked by the sentence you named")
out = Path("artifacts"); out.mkdir(exist_ok=True)
(out / "lab34_limits_statement.md").write_text(RESULT["claim"] + "\n\n" + statement + "\n", encoding="utf-8")

# %% [markdown]
# **Look at** misreading M2, "a student Awn did not refer is safe". The usual headline, "Awn
# referred 55%", invites it. The same fact stated as "it missed 45%" blocks it. Choosing which
# side of a number to print is part of explaining limits.

# %% [markdown]
# ## 5 · Choose your capstone engagement (5')
#
# Three engagements in other units of the University. Each has 4,000 synthetic records, a rule, a
# sponsor's request and a partner's request. Read the three briefs, then set `CHOICE`.

# %%
CAP = Path("capstone")
ENGAGEMENTS = sorted(p.name for p in CAP.iterdir() if (p / "brief.md").exists())
for name in ENGAGEMENTS:
    brief = (CAP / name / "brief.md").read_text(encoding="utf-8")
    print(brief.split("\n")[0].lstrip("# "), "·", f"capstone/{name}/")
    print("   ", re.search(r"\*\*The sponsor's request\.\*\* (.*)", brief).group(1), "\n")

# %%
CHOICE = "housing"   # ✏️ scholarships, housing or careers

records = pd.read_csv(CAP / CHOICE / "records.csv", dtype=str, keep_default_na=False)
partner = json.loads((CAP / CHOICE / "partner_request.json").read_text(encoding="utf-8"))
flag, outcome = records.columns[-2], records.columns[-1]
print(len(records), "records ·", len(records.columns), "columns · flag:", flag, "· outcome:", outcome)
print("partner:", partner["requester"], "·", partner["requester_kind"])
print("asks for:", partner["requested_fields"])
print("\nfirst look, flag rate by group:")
for g in ["gender", "nationality_group", "disability_status"]:
    print("  ", (records[flag] == "yes").groupby(records[g]).mean().round(3).to_dict())
U.check(CHOICE in ENGAGEMENTS and len(records) == 4000, "the engagement's files are open")
U.check({"01_sharing_decision.md", "03_group_comparison.md", "04_datasheet.md", "05_analysis_log.md", "06_scope_note.md"}
        <= {p.name for p in (CAP / "pack_template").iterdir()}, "the pack template is there")

# %% [markdown]
# Before you leave today, write three lines in your notes: which engagement, which of the
# partner's requested fields you already expect to refuse, and which group you will look at
# first. `capstone/README.md` lists what the pack contains and how it is scored.

# %% [markdown]
# ## ✱ Stretch · For the student newspaper
#
# Rewrite the statement for students. Which number do you keep? Which word do you replace for
# "struggling"? What do students most need to know about what a referral is not?

# %% [markdown]
# ## Check yourself
#
# 1. What is the difference between uncertainty and a limit?
# 2. Why does the statement name the two groups?
# 3. A manager wants the number without the three sentences "to keep the slide clean". What do you do?
#
# <details><summary>Answers</summary>
#
# 1. Uncertainty is how far the number could move if you measured again: the interval covers it.
#    A limit is what the number does not measure however often you measure: whether support
#    helps, whether the label is right, whether the record is right.
# 2. Because the rule's errors for them have a known size and cause. Leaving them out would let
#    a reader assume the 55% holds for everyone.
# 3. Shorten, do not remove: "missed 45%; unreliable for two groups; not for judging individuals"
#    fits under any number. A number that travels without its limits will be used beyond them.
# </details>
#
# **Carry forward.** The limits statement closes the capstone's group comparison. You build the pack for the
# engagement you chose before the capstone day, and defend it there.
