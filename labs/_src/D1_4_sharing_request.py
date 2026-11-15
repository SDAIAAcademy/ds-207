# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 1.4 · The Observatory's request
#
# Day 1 · Session 4 (Sharing requests) · 25 min.
#
# Masarat Labour Market Observatory, a government body, asks Al-Qimam University for student
# records. The request came to the analyst's inbox. You name the parties and the route, assess the
# request against the three tests of the Data Sharing Policy, choose the form of release, draft
# the conditions under the policy's eight control headings and fill the decision record. The
# analyst prepares the decision; the data management office and the data protection officer make it.
#
# **Reference state.** `data/partner_request.json`, `data/control_headings.json`,
# `data/students.csv`. Nothing from another lab.
#
# **Tasks**
# - [ ] 1 · Read the request and name the parties and the route (4')
# - [ ] 2 · Assess it against the three tests (6')
# - [ ] 3 · Choose the form of release (5')
# - [ ] 4 · Draft the conditions under the eight control headings (7')
# - [ ] 5 · Fill the decision record and name who signs (3')
# - [ ] ✱ Stretch · The partner adds a consultant outside the Kingdom: revise the decision

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

request = U.json("partner_request.json")
HEADINGS = U.json("control_headings.json")
students = U.load("students.csv")
print(json.dumps(request, indent=1, ensure_ascii=False))

# %% [markdown]
# ## 1 · Parties and route (4')
#
# The Data Sharing Policy names the roles: the **data requester**, the **data sharing entity**, and
# the **data source entity** that is responsible for a field (the University is the source of
# marks and programmes; it is not the source of identity numbers or nationality). A request goes
# to the sharing entity's data management office, not to an analyst. A request for analytical
# purposes goes first to the National Data Bank.
#
# ✏️ **Exercise** · Fill the four facts.

# %%
def parties() -> dict[str, str]:
    # BEGIN SOLUTION
    return {
        "requester": "Masarat Labour Market Observatory (government entity)",
        "sharing_entity": "Al-Qimam University",
        "route": "the University's data management office, with the data protection officer because the data is personal",
        "between_government_entities": "yes: the policy's controls template applies, not a data sharing agreement",
    }
    # END SOLUTION

# %%
try:
    who = parties()
except NotImplementedError:
    who = U.reference("lab14_parties")
U.check("data management office" in who["route"].lower(), "the request is routed to the data management office")
U.check(who["between_government_entities"].lower().startswith("yes"), "two government entities: controls template")
U.table([who]).T

# %% [markdown]
# ## 2 · The three tests (6')
#
# The office assesses a request on three things: (a) a **legitimate purpose** with a legal basis or
# a justified operational need; (b) the **minimum data** for that purpose; (c) the **consent of the
# data source entity** where the sharing entity is not the source. The General Rules for Secondary
# Use of Data repeat the first two for a request like this one, which reuses data for a purpose
# other than the one it was collected for, and the PDPL allows disclosure to a public entity for a
# public-interest purpose (Article 15).
#
# ✏️ **Exercise** · Return `"met"`, `"not met"` or `"met with conditions"` for each test, with the
# evidence from the request.

# %%
TESTS = ["legitimate purpose", "minimum data", "source entity consent"]

def assess(request: dict) -> dict[str, dict]:
    # BEGIN SOLUTION
    return {
        "legitimate purpose": {"status": "met", "evidence": "Labour-market planning is inside the Observatory's mandate and serves the public interest."},
        "minimum data": {"status": "not met", "evidence": "All 18,000 current students, with names, phones, birth dates, disability type and the referral flag: a study of graduates' employment needs none of these."},
        "source entity consent": {"status": "met with conditions", "evidence": "The University is the source of programme and marks. Identity number and nationality come from another source entity: share only what is needed to link, and say so."},
    }
    # END SOLUTION

# %%
try:
    tests = assess(request)
except NotImplementedError:
    tests = U.reference("lab14_tests")
U.check(set(tests) == set(TESTS), "all three tests assessed")
U.check(tests["legitimate purpose"]["status"].startswith("met"), "the purpose is legitimate: this is not a refusal")
U.check(tests["minimum data"]["status"] == "not met", "the request asks for far more than the purpose needs")
U.table([{"test": t, **tests[t]} for t in TESTS])

# %% [markdown]
# ## 3 · The form of release (5')
#
# Three forms, from least to most revealing:
#
# | Form | What leaves | Can the Observatory link to employment records? |
# |---|---|---|
# | aggregate | counts and averages by programme | no |
# | pseudonymised | one row per student under a code only the University can reverse | no |
# | record level, minimised | one row per student with the identity number and the few fields the purpose needs | yes |
#
# The purpose is linkage, so the honest answer is not "aggregates only". It is the narrowest
# record-level release that still links.
#
# ✏️ **Exercise** · Return the form, the population and the fields to share.

# %%
def release_form(request: dict) -> dict:
    # BEGIN SOLUTION
    return {
        "form": "record level, minimised",
        "population": "final-year students only",
        "fields": ["national_id", "college", "programme", "level_year", "term_gpa"],
        "coarsened": {"term_gpa": "a band of half a grade point"},
        "reason": "Linkage needs the identity number. Employment follows graduation, so only final-year students. No contact details, no birth date, no disability type, no referral flag.",
    }
    # END SOLUTION

# %%
try:
    form = release_form(request)
except NotImplementedError:
    form = U.reference("lab14_form")
refused = [f for f in request["requested_fields"] if f not in form["fields"]]
rows = int((students["level_year"] == "4").sum()) if "final" in form["population"] else len(students)
print("form:", form["form"], "·", form["population"], "·", rows, "rows of", len(students))
print("share:", form["fields"], "\nrefuse:", refused)
U.check({"full_name", "phone", "date_of_birth", "disability_type", "awn_referred"} <= set(refused), "no names, contacts, birth dates, health data or referral flag")
U.check("national_id" in form["fields"], "the identity number stays, because the purpose is linkage")
U.check(rows < len(students) / 3, "final-year students only: under a third of the rows asked for")

# %% [markdown]
# **Look at** the two numbers: 11 fields for 18,000 students asked for, 5 fields for 3,612
# students offered. The purpose is served in full.

# %% [markdown]
# ## 4 · The conditions (7')
#
# The policy lists eight headings under which the two parties fix the controls. ✏️ **Exercise** ·
# Write one condition under each heading. Use the request's own weak points: the email, the
# contractors, the consulting firm, "kept for future studies".

# %%
print(HEADINGS)

def conditions() -> dict[str, str]:
    # BEGIN SOLUTION
    return {
        "legal basis": "Shared under the Observatory's mandate for labour-market planning, a public-interest purpose; used for the linkage study and nothing else.",
        "authorisation": "Access for named Observatory analysts only, on a need-to-know basis; no contractors unless named and approved in writing.",
        "data type": "Five fields for final-year students: identity number, college, programme, level, grade band. A new field is a new request.",
        "pre-processing": "The Observatory replaces the identity number with its own study code immediately after linkage and destroys the identity numbers.",
        "sharing means": "Through the Government Service Bus or another channel approved by the data management office; never by email attachment.",
        "usage and protection": "Marked Restricted and protected as Restricted; no onward sharing with the consulting firm or anyone else; results published only as tables with no count under 10.",
        "duration and termination": "Kept for 12 months from delivery, then destroyed with a written confirmation; access revoked if a condition is broken.",
        "liability": "Each party answers for its own breach of these conditions; a data leak is reported to the University within 24 hours of discovery.",
    }
    # END SOLUTION

# %%
try:
    conds = conditions()
except NotImplementedError:
    conds = U.reference("lab14_conditions")
U.check(set(conds) == set(HEADINGS), "one condition under each of the eight headings")
text = " ".join(conds.values()).lower()
U.check("email" in text, "the channel is fixed, and it is not an email attachment")
U.check("onward" in text or "consult" in text, "the consulting firm does not get the data")
U.check("destroy" in text, "retention ends in destruction, not 'future studies'")
U.check("restricted" in text, "the classification level travels with the data")
U.table([{"heading": h, "condition": conds[h]} for h in HEADINGS])

# %% [markdown]
# ## 5 · The decision record (3')
#
# ✏️ **Exercise** · Fill the record. Who signs depends on the level of the data: the policy names
# the director of the data management office for Restricted data. The office assesses a request
# within 10 business days.

# %%
def decision_record() -> dict:
    # BEGIN SOLUTION
    return {
        "decision": "approve with conditions",
        "classification": "Restricted",
        "signatory": "director of the data management office",
        "consulted": "Shatha Al-Omair, data protection officer; Rami Al-Tuwaijri, registrar (data owner)",
        "assessment_within_business_days": 10,
        "recorded_in": "the University's record of processing activities and the office's log of sharing requests",
        "prepared_by": "Ohoud Al-Lihyani, analyst",
    }
    # END SOLUTION

# %%
try:
    record = decision_record()
except NotImplementedError:
    record = U.reference("lab14_record")
U.check(record["decision"] == "approve with conditions", "neither a yes to everything nor a refusal")
U.check("data management office" in record["signatory"], "Restricted data: the director of the data management office signs")
U.check(record["assessment_within_business_days"] == 10, "ten business days to assess")
U.check("analyst" in record["prepared_by"].lower(), "the analyst prepares; she does not decide")
out = Path("artifacts"); out.mkdir(exist_ok=True)
(out / "lab14_sharing_decision.json").write_text(json.dumps({"tests": tests, "form": form, "conditions": conds, "record": record}, indent=1, ensure_ascii=False), encoding="utf-8")
U.table([record]).T

# %% [markdown]
# ## ✱ Stretch · One fact changes
#
# Hazza Al-Marri writes back: the dashboards are built by a consulting firm whose analysts work
# outside the Kingdom, and they need the linked file. Which rule now applies that did not before?
# Revise two conditions. This is the move the assessor asks for in the capstone defence.

# %% [markdown]
# ## Check yourself
#
# 1. Why "approve with conditions" and not "refuse until the request is rewritten"?
# 2. Why may the University not simply send aggregates?
# 3. What would change if the requester were a private company?
#
# <details><summary>Answers</summary>
#
# 1. The purpose is legitimate and the law allows the disclosure. The office's job is to make the
#    sharing safe, and the policy expects sharing when the tests are met.
# 2. It may, if aggregates served the purpose. Linkage to employment records needs one row per
#    person, so aggregates would answer a different question.
# 3. A data sharing agreement in place of the controls template, the secondary-use rules' licence
#    for private applicants, a purpose that is not profit-seeking, and a closer look at the PDPL's
#    disclosure cases: "a public entity for the public interest" would no longer apply.
# </details>
#
# **Carry forward.** `artifacts/lab14_sharing_decision.json` is the model for the capstone's
# sharing decision. The three engagements each have their own partner request.
