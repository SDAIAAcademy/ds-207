# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 1.2 · Cut the extract
#
# Day 1 · Session 2 (Purpose, minimisation and secondary use) · 25 min.
#
# Request R1 is inside the collection purpose, so the work may start. It starts with a cut: the
# registry has 30 columns and the purpose needs a handful. You decide each field, look inside the
# free-text notes with pattern rules, build the extract under a project pseudonym and write the
# log that says why each field stayed or went.
#
# **Reference state.** `data/students.csv` (18,000 synthetic students, 30 columns). Nothing from
# another lab.
#
# **Tasks**
# - [ ] 1 · Read the purpose and the 30 columns of the registry (3')
# - [ ] 2 · Decide keep, coarsen or drop for each field, with a reason (8')
# - [ ] 3 · Scan the advisor notes for identifiers with rules (5')
# - [ ] 4 · Build the extract with a project pseudonym (6')
# - [ ] 5 · Write the minimisation log (3')
# - [ ] ✱ Stretch · Decide the fields again for a second purpose, the partner's study, and say what makes it a secondary use

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
import re

students = U.load("students.csv")

# %% [markdown]
# ## 1 · The purpose and the columns (3')
#
# The purpose, as agreed with the director of the unit:

# %%
PURPOSE = ("Evaluate whether Awn's referrals in term 1 of 2026-27 reached the students who ended the term "
           "struggling, by college and level, to decide whether to extend the rule.")
print(PURPOSE, "\n")
print(len(students), "rows,", len(students.columns), "columns")
students.iloc[0].to_frame("first row")

# %% [markdown]
# ## 2 · Field by field (8')
#
# For each column choose one of three: **keep** (the purpose needs it as it is), **coarsen** (it
# needs a rougher form: a band, a flag, a pseudonym), **drop** (it does not need it). The test is
# the sentence above, not "it might be useful".
#
# ✏️ **Exercise** · Return a decision and a short reason for every column.

# %%
def decide() -> dict[str, tuple[str, str]]:
    # BEGIN SOLUTION
    drop_identity = "identifies the student; the question is about groups of students"
    d = {c: ("drop", "the purpose does not need it") for c in students.columns}
    for c in ["national_id", "full_name", "email", "phone", "home_address", "bank_iban"]:
        d[c] = ("drop", drop_identity)
    d["student_id"] = ("coarsen", "a project pseudonym keeps one row per student without the registry number")
    d["college"] = ("keep", "the result is reported by college")
    d["level_year"] = ("keep", "the result is reported by level")
    d["admission_route"] = ("keep", "bridging-year entrants have no midterm mark; needed to read the rule's result")
    d["attendance_rate"] = ("keep", "an input of the rule")
    d["midterm_gpa"] = ("keep", "an input of the rule")
    d["awn_referred"] = ("keep", "what is being evaluated")
    d["term_outcome"] = ("keep", "the outcome the referral is compared with")
    d["term_gpa"] = ("drop", "term_outcome already says struggled or not")
    d["disability_type"] = ("drop", "health data; the purpose does not need it")
    d["counselling_visits"] = ("drop", "health-related; the purpose does not need it")
    d["advisor_note"] = ("drop", "free text: cannot be checked field by field")
    return d
    # END SOLUTION

# %%
MUST_DROP = {"national_id", "full_name", "email", "phone", "home_address", "bank_iban", "date_of_birth",
             "disability_type", "counselling_visits", "advisor_note"}
MUST_STAY = {"college", "level_year", "attendance_rate", "midterm_gpa", "awn_referred", "term_outcome"}
try:
    decision = decide()
except NotImplementedError:
    decision = {k: tuple(v) for k, v in U.reference("lab12_decision").items()}
U.check(set(decision) == set(students.columns), "every column has a decision")
U.check(all(decision[c][0] == "drop" for c in MUST_DROP), "identifiers, contact details, health data and free text are dropped")
U.check(all(decision[c][0] in ("keep", "coarsen") for c in MUST_STAY), "the rule's inputs, its output and the outcome stay")
U.check(decision["student_id"][0] != "keep", "the registry number does not travel into the extract")
U.check(all(len(reason) > 8 for _, reason in decision.values()), "every decision has a reason")
log = U.table([{"field": c, "decision": decision[c][0], "reason": decision[c][1]} for c in students.columns])
print(log["decision"].value_counts().to_dict())

# %% [markdown]
# **Look at** `gender`, `nationality` and `disability_status`. This purpose does not need them, so
# they go. Comparing the rule's errors across groups is a different question, with its own
# approval: you meet it on Day 2, already approved and logged.

# %% [markdown]
# ## 3 · What hides in free text (5')
#
# `advisor_note` is one column. Inside it are other people's data. Pattern rules find the
# identifiers that have a shape. (A library such as Presidio packages many such rules; two
# regular expressions are enough to see the point.)
#
# ✏️ **Exercise** · Write `find_identifiers(note)`: return the list of kinds found, `"phone"` for a
# Saudi mobile number (05 and eight more digits) and `"national_id"` for a ten-digit number that
# starts with 1 or 2.

# %%
def find_identifiers(note: str) -> list[str]:
    # BEGIN SOLUTION
    found = []
    if re.search(r"\b05\d{8}\b", note):
        found.append("phone")
    if re.search(r"\b[12]\d{9}\b", note):
        found.append("national_id")
    return found
    # END SOLUTION

# %%
notes = students[students["advisor_note"] != ""]
try:
    hits = notes["advisor_note"].map(find_identifiers)
    counts = {"notes": len(notes), "phone": int(hits.map(lambda h: "phone" in h).sum()),
              "national_id": int(hits.map(lambda h: "national_id" in h).sum())}
except NotImplementedError:
    counts = U.reference("lab12_note_counts")
print(counts)
U.check(counts["phone"] == 180 and counts["national_id"] == 70, "180 notes carry a phone number and 70 an identity number")

# %% [markdown]
# **Look at** what the rules did not find. Run the next cell: health remarks and other students'
# names have no shape a pattern can catch. That is why the note is dropped whole, not cleaned.

# %%
for needle in ["surgery", "anxiety", "Dialysis", "Hearing aid", "copied the lab report"]:
    sample = notes[notes["advisor_note"].str.contains(needle)]["advisor_note"]
    print(f"{len(sample):4d} notes with '{needle}', for example: {sample.iloc[0]}")

# %% [markdown]
# ## 4 · Build the extract (6')
#
# ✏️ **Exercise** · Write `build_extract(students, decision)`: the kept columns, and `pid` in place of
# `student_id`, made with `U.pseudonym` (a keyed hash; the key stays in the unit). Sort by `pid` so
# the order of the registry does not survive.

# %%
def build_extract(students: pd.DataFrame, decision: dict) -> pd.DataFrame:
    # BEGIN SOLUTION
    keep = [c for c in students.columns if decision[c][0] == "keep"]
    out = students[keep].copy()
    out.insert(0, "pid", students["student_id"].map(U.pseudonym))
    return out.sort_values("pid").reset_index(drop=True)
    # END SOLUTION

# %%
try:
    extract = build_extract(students, decision)
except NotImplementedError:
    ref = U.reference("lab12_extract")
    extract = U.load("analysis_extract.csv")[ref["columns"]]
print(len(extract), "rows;", list(extract.columns))
U.check(len(extract) == 18000 and extract["pid"].is_unique, "one row per student, one pseudonym each")
U.check(not (set(extract.columns) & (MUST_DROP | {"student_id"})), "nothing that had to be dropped is in the extract")
U.check(MUST_STAY <= set(extract.columns), "the fields the purpose needs are there")
U.check(len(extract.columns) <= 10, "ten columns or fewer, down from 30")
extract.head(3)

# %% [markdown]
# ## 5 · The minimisation log (3')
#
# The log is the evidence that the cut was a decision. It is what a reviewer reads, and what you
# show the data owner. Save it beside the extract.

# %%
summary = {"purpose": PURPOSE, "columns_before": len(students.columns), "columns_after": len(extract.columns),
           "dropped": int((log["decision"] == "drop").sum()), "coarsened": int((log["decision"] == "coarsen").sum()),
           "kept": int((log["decision"] == "keep").sum())}
print(summary)
out = Path("artifacts"); out.mkdir(exist_ok=True)
log.to_csv(out / "lab12_minimisation_log.csv", index=False)
U.check(summary["columns_after"] < summary["columns_before"] / 3, "the extract has fewer than a third of the registry's columns")
log[log["decision"] != "drop"]

# %% [markdown]
# ## ✱ Stretch · A second purpose
#
# The Observatory wants to link study records to employment records. Decide the 30 fields again
# for that purpose. Which fields change sides? The data was collected to teach and support
# students: what makes the Observatory's study a secondary use, and which document sets its rules?

# %% [markdown]
# ## Check yourself
#
# 1. Why is `student_id` coarsened and not kept, when the extract never leaves the unit?
# 2. Is the extract still personal data?
# 3. Why drop `term_gpa` when it is more precise than `term_outcome`?
#
# <details><summary>Answers</summary>
#
# 1. The purpose needs one row per student, not the number that opens every other system. If the
#    extract leaks, a pseudonym made with a project key links to nothing else.
# 2. Yes. Pseudonymised data is personal data: the key exists and each row is about one student.
# 3. The question is whether referrals reached struggling students. The flag answers it; the
#    exact grade adds detail the purpose does not use.
# </details>
#
# **Carry forward.** The decision table is the model for the capstone's extract. Day 2 starts from
# `data/analysis_extract.csv`, this extract plus four group fields approved for the comparison.
