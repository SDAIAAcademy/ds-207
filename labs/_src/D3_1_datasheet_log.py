# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 3.1 · Datasheet and log
#
# Day 3 · Session 1 (Datasheets and analysis logs) · 25 min.
#
# Two days of decisions are in your head. A reviewer who was not in the room has to be able to
# trace each published number to its data, its decisions and its approvals. You fill a datasheet
# for the analysis extract, add three decisions to the analysis log with their approver, tag the
# release with the fingerprints of its files, and let a peer try five audit questions on your
# documents alone.
#
# **Reference state.** `data/analysis_extract.csv`, `data/datasheet_template.md`,
# `data/analysis_log_seed.json` (the first two log entries), `data/audit_questions.json`. Nothing
# from another lab.
#
# **Tasks**
# - [ ] 1 · Fill the datasheet from the data and the notice (8')
# - [ ] 2 · Log three decisions with reason, date and approver (6')
# - [ ] 3 · Tag the release with its file fingerprints (4')
# - [ ] 4 · Swap with a peer and answer five audit questions (5')
# - [ ] 5 · Fix what the peer could not answer (2')
# - [ ] ✱ Stretch · Add a decision record for the choice of threshold, with the options that were rejected

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
import hashlib
import json

extract = U.load("analysis_extract.csv")
SEED_LOG = U.json("analysis_log_seed.json")
QUESTIONS = U.json("audit_questions.json")
SECTIONS = ["motivation", "composition", "collection", "preprocessing", "uses", "distribution", "maintenance"]
print(U.text("datasheet_template.md"))

# %% [markdown]
# ## 1 · The datasheet (8')
#
# A datasheet answers, for a dataset, the questions a careful user would ask before using it.
# Seven sections. Facts first: the cell below gives you the numbers.

# %%
facts = {"rows": len(extract), "columns": list(extract.columns),
         "no_midterm_mark": int((extract["midterm_gpa"] == "").sum()),
         "remote_accommodation": int((extract["remote_accommodation"] == "yes").sum()),
         "registered_disability": int((extract["disability_status"] == "registered").sum())}
print(json.dumps(facts, indent=1))

# %% [markdown]
# ✏️ **Exercise** · Return the seven sections. Write for a reader who has never seen the data:
# what one row is, what is missing and for whom, what is known to be recorded badly, and what the
# data must not be used for.

# %%
def datasheet() -> dict[str, str]:
    # BEGIN SOLUTION
    return {
        "motivation": "Made by the Student Success Unit of Al-Qimam University to evaluate Awn, the support-referral rule, in term 1 of 2026-27, for the director's decision whether to extend the rule.",
        "composition": "One row per enrolled student: 18,000 rows, 13 fields. A project pseudonym, college, level, admission route, gender, nationality group, disability status, first-generation flag, remote accommodation, recorded attendance, midterm mark, referral, term outcome. Personal data throughout; disability status and remote accommodation are health data. The midterm mark is missing for 1,244 students, all bridging-year entrants.",
        "collection": "Attendance comes from card readings at teaching-room doors; midterm marks and the term outcome from the registry; group fields from the registry and the accommodation register. Known to be recorded badly: attendance is about 17 points too low for the 300 students with a remote accommodation, because remote sessions leave no card reading.",
        "preprocessing": "Extracted from the 30-column registry. Names, identity numbers, contact details, addresses, bank accounts, disability type, counselling visits and free-text notes were not extracted. Student numbers were replaced by a keyed project pseudonym; nationality was coarsened to two groups. The raw registry stays with the registrar.",
        "uses": "Approved use: evaluating Awn's referrals and comparing its error rates across groups, reported in aggregate. It must not be used to decide anything about an individual student, to build lists of students, or for any purpose outside the unit without a new decision.",
        "distribution": "Classified Restricted. Access for the unit's analysts on a need-to-know basis. It does not leave the University and is not entered into any AI tool.",
        "maintenance": "Owner: Rami Al-Tuwaijri, registrar. Kept until 30 June 2027, then destroyed with a log entry. Errors are reported to the unit's analyst, who records the correction in the analysis log.",
    }
    # END SOLUTION

# %%
try:
    sheet = datasheet()
except NotImplementedError:
    sheet = U.reference("lab31_datasheet")
U.check(list(sheet) == SECTIONS and all(len(v) > 60 for v in sheet.values()), "seven sections, each more than a line")
U.check("18,000" in sheet["composition"] and "missing" in sheet["composition"].lower(), "composition says how many rows and what is missing")
U.check("must not" in sheet["uses"].lower(), "uses says what the data must not be used for")
U.check("restricted" in sheet["distribution"].lower(), "distribution states the classification level")
U.check(any(ch.isdigit() for ch in sheet["maintenance"]), "maintenance gives an end date")

# %% [markdown]
# ## 2 · Three decisions for the log (6')
#
# The log already holds two entries, L001 (the minimised extract) and L002 (the group fields).
# ✏️ **Exercise** · Add three decisions made on Day 2. Each needs an id, a date, the decision, the
# reason, the approver (a person with a role, not "the team") and where the evidence is.

# %%
for e in SEED_LOG:
    print(e["id"], e["date"], "·", e["decision"][:90], "·", e["approver"])

def new_entries() -> list[dict]:
    # BEGIN SOLUTION
    return [
        {"id": "L003", "date": "2026-11-09", "decision": "Release disability counts as two one-way tables (by college, by nationality group) and not as the cross table; 5 primary and 5 complementary cells would have been suppressed.",
         "reason": "Complementary suppression hid 10 of 12 cells; the one-way tables have no cell under 10.",
         "approver": "Rami Al-Tuwaijri, registrar (data owner); suppression checked by Jassim Al-Nuaimi, director of the unit", "evidence": "suppression log, Lab 2.1"},
        {"id": "L004", "date": "2026-11-09", "decision": "Do not release the Saudi-only disability table by college.",
         "reason": "Differencing against the release of 2026-10 reveals counts of 1 to 9, including one student in Computing.",
         "approver": "Rami Al-Tuwaijri, registrar (data owner)", "evidence": "suppression log, Lab 2.1"},
        {"id": "L005", "date": "2026-11-10", "decision": "Report bridging-year entrants and students with a remote accommodation separately in the evaluation of Awn.",
         "reason": "Their midterm marks are missing and their attendance is under-recorded, so the rule's errors for them have a known cause that the overall rates would hide.",
         "approver": "Jassim Al-Nuaimi, director of the Student Success Unit", "evidence": "bias findings, Lab 2.4"},
    ]
    # END SOLUTION

# %%
FIELDS = ["id", "date", "decision", "reason", "approver", "evidence"]
try:
    added = new_entries()
except NotImplementedError:
    added = U.reference("lab31_entries")
log = SEED_LOG + added
U.check(len(added) == 3 and all(all(e.get(f) for f in FIELDS) for e in added), "three entries, every field filled")
U.check(all("," in e["approver"] or "(" in e["approver"] for e in added), "each approver is a person with a role")
U.check([e["date"] for e in log] == sorted(e["date"] for e in log), "the log is in date order")
U.check(len({e["id"] for e in log}) == len(log), "ids are unique")
U.table(log)[["id", "date", "approver"]]

# %% [markdown]
# ## 3 · Tag the release (4')
#
# A result is traceable when the files that produced it can be recognised later. A fingerprint
# (a SHA-256 hash) changes if one byte of a file changes.
#
# ✏️ **Exercise** · Write `fingerprint(path)`: the first 16 hexadecimal characters of the file's
# SHA-256 hash. The cell below builds the release record.

# %%
def fingerprint(path: Path) -> str:
    # BEGIN SOLUTION
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:16]
    # END SOLUTION

# %%
referral_table = extract.groupby("college").agg(students=("pid", "size"), referred=("awn_referred", lambda s: int((s == "yes").sum())))
out = Path("artifacts"); out.mkdir(exist_ok=True)
referral_table.to_csv(out / "referral_by_college_v2026.11.1.csv")
try:
    prints = {"analysis_extract.csv": fingerprint(U.DATA / "analysis_extract.csv"),
              "referral_by_college_v2026.11.1.csv": fingerprint(out / "referral_by_college_v2026.11.1.csv")}
except NotImplementedError:
    prints = U.reference("lab31_release")["files"]
release = {"version": "2026.11.1", "date": "2026-11-11", "table": "Referral rate by college, term 1 of 2026-27",
           "files": prints, "log_entries": [e["id"] for e in log], "classification": "Public after approval",
           "approved_by": "Rami Al-Tuwaijri, registrar (data owner)", "suppressed_cells": 0,
           "must_not_be_used_for": "ranking colleges or judging advisors: referral rates follow how hard a college's programmes are"}
print(json.dumps(release, indent=1))
U.check(all(len(v) == 16 for v in prints.values()), "two fingerprints of 16 characters")
U.check(all(set(v) <= set("0123456789abcdef") for v in prints.values()), "fingerprints are lower-case hexadecimal")

# %% [markdown]
# ## 4 · Five audit questions (5')
#
# Swap documents with a peer. Each of you answers the five questions **from the other's documents
# only**: no asking, no notebook. Note every question you could not answer and why.

# %%
for i, q in enumerate(QUESTIONS, 1):
    print(f"{i}. {q}")

# %% [markdown]
# The function below is a mechanical stand-in for the peer, for when you work alone: it looks for
# the answer where a reviewer would look, and says "cannot answer" when the place is empty.

# %%
def audit(sheet: dict, log: list[dict], release: dict) -> dict[int, str]:
    def find(word):
        return next((e for e in log if word in (e["decision"] + e["reason"]).lower()), None)
    group, bridging, supp = find("disability status"), find("bridging"), find("suppress")
    return {
        1: f"{', '.join(release['files'])}, version {release['version']}" if release.get("files") and release.get("version") else "cannot answer",
        2: f"{group['approver']}: {group['reason']}" if group else "cannot answer",
        3: bridging["reason"] if bridging else "cannot answer",
        4: sheet["uses"].split("must not", 1)[1].strip() if "must not" in sheet.get("uses", "") else "cannot answer",
        5: f"{supp['decision']} Checked: {supp['approver']}" if supp and "check" in supp["approver"].lower() else "cannot answer",
    }

answers = audit(sheet, log, release)
for i, a in answers.items():
    print(f"{i}. {a[:150]}")
unanswered = [i for i, a in answers.items() if a == "cannot answer"]
U.check(not unanswered, "all five audit questions can be answered from the documents alone")

# %% [markdown]
# ## 5 · Fix what could not be answered (2')
#
# For each question your peer could not answer, add the missing sentence to the datasheet or the
# missing field to the log, and run task 4 again. Then save the pack.

# %%
lines = ["# Datasheet: analysis extract, Awn evaluation", ""]
for s in SECTIONS:
    lines += [f"## {s.capitalize()}", "", sheet[s], ""]
(out / "lab31_datasheet.md").write_text("\n".join(lines), encoding="utf-8")
(out / "lab31_analysis_log.json").write_text(json.dumps(log, indent=1, ensure_ascii=False), encoding="utf-8")
(out / "lab31_release.json").write_text(json.dumps(release, indent=1), encoding="utf-8")
print("saved:", sorted(p.name for p in out.glob("lab31_*")))

# %% [markdown]
# ## ✱ Stretch · A decision record
#
# Write a one-page record of the choice of 10 as the release threshold: the context, the options
# considered (3, 5, 10, rounding), the decision, who made it, and what would make the unit revisit
# it.

# %% [markdown]
# ## Check yourself
#
# 1. Why does the approver have to be a named person with a role?
# 2. What does the fingerprint add to a version number?
# 3. The datasheet states a weakness of the data (attendance under-recorded). Does that not
#    undermine the analysis?
#
# <details><summary>Answers</summary>
#
# 1. Accountability attaches to people. "The team approved" cannot be asked a question in an
#    audit, and cannot be shown to have had the authority.
# 2. A version number is a claim; a fingerprint is a check. If the extract is regenerated and one
#    value differs, the fingerprint differs.
# 3. It protects it. A reader who finds the weakness alone stops trusting everything; a reader
#    who is told can weigh the results that depend on it.
# </details>
#
# **Carry forward.** The three files in `artifacts/` are the model for the capstone's datasheet
# and analysis log.
