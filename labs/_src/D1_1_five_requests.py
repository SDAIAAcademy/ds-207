# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 1.1 · Five requests, which rules
#
# Day 1 · Session 1 (What the law asks of an analyst) · 25 min.
#
# Five requests reached Ohoud Al-Lihyani, the analyst of the Student Success Unit, in one week.
# You decide what kind of processing each one is, which rules of the Personal Data Protection Law
# (PDPL) and the national data policies it engages, and which of them must go to the data
# protection officer before any data is touched. You end with the note for one request.
#
# **Reference state.** `data/requests.json` and `data/privacy_notice.md`. Nothing from another lab.
#
# **Tasks**
# - [ ] 1 · Read the five requests and the privacy notice (4')
# - [ ] 2 · Name the kind of processing each request is (5')
# - [ ] 3 · Mark the rules each request engages (8')
# - [ ] 4 · Flag the requests that go to the data protection officer (3')
# - [ ] 5 · Write the note for one request (5')
# - [ ] ✱ Stretch · Add a sixth request: a student asks for a copy of her data used in the analysis

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

# %% [markdown]
# ## 1 · The requests and the notice (4')
#
# The privacy notice is what students were told when their data was collected. It fixes the
# purposes. Read it first, then the five requests.

# %%
print(U.text("privacy_notice.md"))
pack = U.json("requests.json")
REQUESTS, RULES, KINDS = pack["requests"], pack["rules"], pack["kinds"]
for r in REQUESTS:
    print(f"\n{r['id']} · {r['from']}\n   \"{r['text']}\"\n   wants: {r['data_wanted']}")

# %% [markdown]
# ## 2 · What kind of processing is it? (5')
#
# Four kinds, each with its own gate in the law:
#
# | Kind | The gate |
# |---|---|
# | within the collection purpose | The purpose students were told (PDPL Article 10, first sentence) |
# | new internal purpose | A purpose other than the one collected for: only in the cases Article 10 lists |
# | disclosure to another entity | Only in the cases Article 15 lists |
# | transfer outside the Kingdom | Article 29 and the transfer regulation |
#
# ✏️ **Exercise** · Return the kind of each request.

# %%
print(KINDS)

def kinds() -> dict[str, str]:
    # BEGIN SOLUTION
    return {
        "R1": "within the collection purpose",
        "R2": "new internal purpose",
        "R3": "disclosure to another entity",
        "R4": "new internal purpose",
        "R5": "transfer outside the Kingdom",
    }
    # END SOLUTION

# %%
try:
    kind = kinds()
except NotImplementedError:
    kind = U.reference("lab11_kinds")
U.check(set(kind) == {"R1", "R2", "R3", "R4", "R5"} and set(kind.values()) <= set(KINDS), "every request has one of the four kinds")
U.check(kind["R1"] == "within the collection purpose", "R1 is academic support, the purpose in the notice")
U.check(kind["R5"] == "transfer outside the Kingdom", "an upload to a service abroad is a transfer")
U.table([{"request": k, "kind": v} for k, v in kind.items()])

# %% [markdown]
# ## 3 · Which rules does each request engage? (8')
#
# The nine rules an analyst meets most often:
#
# | Rule | Where | The question it asks |
# |---|---|---|
# | lawful basis | PDPL Articles 5, 6 | On what ground is this processing allowed at all? |
# | purpose limitation | Articles 10, 11 | Is this the purpose the data was collected for? |
# | minimisation | Article 11 | Does the purpose need every field and every row asked for? |
# | sensitive data | Articles 1, 23 | Does it touch health data or another sensitive kind? |
# | disclosure | Articles 15, 16 | Does someone outside the University get access? |
# | transfer | Article 29 | Does the data leave the Kingdom? |
# | marketing consent | Articles 25, 26 | Is it advertising sent to a person? |
# | classification | Data Classification Policy | What level is the data, and where may that level go? |
# | records of processing | Article 31 | Is this processing in the University's record? |
#
# ✏️ **Exercise** · Return the rules each request engages. Name the ones that decide the answer,
# not all nine every time. The check accepts your answer for a request when it contains the
# deciding rules; the course outcome asks for at least four of five.

# %%
def rules() -> dict[str, list[str]]:
    # BEGIN SOLUTION
    return {
        "R1": ["lawful basis", "purpose limitation", "minimisation", "records of processing"],
        "R2": ["purpose limitation", "minimisation", "sensitive data"],
        "R3": ["lawful basis", "purpose limitation", "minimisation", "disclosure", "classification", "records of processing"],
        "R4": ["lawful basis", "purpose limitation", "marketing consent"],
        "R5": ["minimisation", "sensitive data", "transfer", "classification"],
    }
    # END SOLUTION

# %%
DECIDING = {"R1": {"purpose limitation", "minimisation"}, "R2": {"sensitive data", "purpose limitation"},
            "R3": {"disclosure", "minimisation"}, "R4": {"marketing consent"}, "R5": {"transfer", "classification"}}
try:
    engaged = rules()
except NotImplementedError:
    engaged = U.reference("lab11_rules")
right = [r for r in DECIDING if DECIDING[r] <= set(engaged.get(r, []))]
print("requests with the deciding rules named:", right)
U.check(all(set(v) <= set(RULES) for v in engaged.values()), "only rules from the list")
U.check(len(right) >= 4, "at least four of five requests carry their deciding rules")
U.table([{"request": r, "rules engaged": ", ".join(engaged[r])} for r in engaged])

# %% [markdown]
# **Look at** R1 and R3 side by side. Both are evaluations, both use the same records. What
# separates them is who sees the data and for which purpose, not the method.

# %% [markdown]
# ## 4 · Who goes to the data protection officer first? (3')
#
# Shatha Al-Omair, the data protection officer, monitors how the University applies the law and
# supervises impact assessments. The analyst's rule of thumb: anything that is not plainly inside
# the collection purpose goes to her before data is touched.
#
# ✏️ **Exercise** · Return the requests that go to her.

# %%
def to_dpo() -> list[str]:
    # BEGIN SOLUTION
    return ["R2", "R3", "R4", "R5"]
    # END SOLUTION

# %%
try:
    dpo = to_dpo()
except NotImplementedError:
    dpo = U.reference("lab11_dpo")
U.check("R1" not in dpo, "R1 proceeds inside the unit, with a minimised extract and a record")
U.check({"R2", "R3", "R4", "R5"} <= set(dpo), "a new purpose, a disclosure, advertising and a transfer all go to her")

# %% [markdown]
# ## 5 · The note for one request (5')
#
# The note is what you send back. Four lines: what was asked, the kind of processing, the rules
# engaged, and what happens next.
#
# ✏️ **Exercise** · Write the note for R2 (the dean's request). Name the purpose problem and the
# health data, and offer what the dean can have instead.

# %%
def note_r2() -> str:
    # BEGIN SOLUTION
    return (
        "Asked: names of referred engineering students with counselling visits and disability type, for department heads.\n"
        "Kind: a new internal purpose. The notice tells students that health and counselling data is seen only by the staff who provide those services.\n"
        "Rules engaged: purpose limitation, minimisation, sensitive data (health data, PDPL Articles 1, 10, 11 and 23).\n"
        "Next: I cannot send names, counselling or disability data. I can send the number of referred students per department and "
        "the share contacted by their advisor within two weeks. If you need more, the data protection officer decides: I have copied her."
    )
    # END SOLUTION

# %%
try:
    note = note_r2()
except NotImplementedError:
    note = U.reference("lab11_note")["text"]
print(note)
low = note.lower()
U.check("purpose" in low and ("health" in low or "sensitive" in low), "the note names the purpose problem and the health data")
U.check("data protection officer" in low, "the note says who decides")
U.check(len([l for l in note.splitlines() if l.strip()]) <= 6, "the note is short enough to be read")

# %% [markdown]
# ## ✱ Stretch · A sixth request
#
# A student writes: "I heard my data was used in a study of Awn. Send me a copy of what you
# hold about me." Which right is this, who answers it, and by when? What does the pseudonymised
# extract mean for the answer?

# %% [markdown]
# ## Check yourself
#
# 1. Why is R1 not a new purpose, although no student was told about "an evaluation of Awn"?
# 2. The Observatory is a government body with a public-interest purpose. Why is R3 still not a yes?
# 3. Which single fact makes R5 a transfer?
#
# <details><summary>Answers</summary>
#
# 1. The notice names academic advice and support as a purpose. Checking that the support
#    service works is part of running it. The fields still have to be cut to what that needs.
# 2. Article 15 makes the disclosure possible, not automatic: the data must be the minimum the
#    purpose needs, the Data Sharing Policy sets the route and the controls, and the University
#    records it.
# 3. The data would be stored and processed on servers outside the Kingdom. Who owns the
#    service does not matter.
# </details>
#
# **Carry forward.** The kinds and rules table is the first part of the capstone's sharing
# decision. Lab 1.2 takes R1 and cuts its extract.
