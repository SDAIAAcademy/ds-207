# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 1.3 · Classify and control
#
# Day 1 · Session 3 (Classifying data and outputs) · 25 min.
#
# An analysis produces data: extracts, tables, lists. Each one needs a classification level before
# it is stored, sent or pasted anywhere. You classify four datasets and three outputs of the Awn
# evaluation with the impact questions of the Data Classification Policy, apply the highest-level
# rule to a joined file, name the controls and decide what may be entered into an AI tool.
#
# **Reference state.** `data/datasets.json` and `data/students.csv`. Nothing from another lab.
#
# **Tasks**
# - [ ] 1 · Run the impact questions on the four datasets (7')
# - [ ] 2 · Classify the three outputs (6')
# - [ ] 3 · Apply the highest-level rule to a joined file (3')
# - [ ] 4 · Name the controls for each item (6')
# - [ ] 5 · Decide what may be entered into an AI tool (3')
# - [ ] ✱ Stretch · Set a declassification trigger for the referral table and say who approves it

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

pack = U.json("datasets.json")
ITEMS, LEVELS, CONTROLS = pack["items"], pack["levels"], pack["controls"]
for it in ITEMS:
    print(f"{it['id']} · {it['name']} ({it['kind']})\n     {it['description']}")

# %% [markdown]
# ## 1 · The four datasets (7')
#
# The policy's route to a level, shortened to what a university analyst meets:
#
# 1. **Impact.** If this were disclosed to someone who should not have it, what is the worst
#    realistic harm: to the national interest, to the entity's activities, to individuals, to the
#    environment? High means Top Secret, medium means Secret, none means Public.
# 2. **Low impact** (the privacy of an individual is the usual case) needs two more questions:
#    would disclosure conflict with a law, such as the PDPL? Then Restricted. If not, do the
#    benefits of openness outweigh the harm? Then Public, otherwise Restricted.
# 3. Data that nobody has classified yet is treated as Restricted.
#
# ✏️ **Exercise** · Write `classify(item_id)` for D1 to D4: return the level and the impact reason.

# %%
def classify_datasets() -> dict[str, tuple[str, str]]:
    # BEGIN SOLUTION
    return {
        "D1": ("Restricted", "low impact on individuals' privacy; disclosure would break the PDPL"),
        "D2": ("Restricted", "health data of individuals; disclosure would break the PDPL"),
        "D3": ("Public", "already published; disclosure harms nobody"),
        "D4": ("Restricted", "pseudonymised rows are still personal data; disclosure would break the PDPL"),
    }
    # END SOLUTION

# %%
try:
    datasets = {k: tuple(v) for k, v in classify_datasets().items()}
except NotImplementedError:
    datasets = {k: tuple(v) for k, v in U.reference("lab13_datasets").items()}
U.check(all(lv in LEVELS for lv, _ in datasets.values()), "each level is one of the four")
U.check(datasets["D3"][0] == "Public", "the published timetable is Public")
U.check(datasets["D4"][0] == "Restricted", "a pseudonym does not make the extract Public")
U.check(datasets["D1"][0] == datasets["D2"][0] == "Restricted", "personal data of students is Restricted, not Secret: the impact is on individuals")
U.table([{"item": k, "level": v[0], "reason": v[1]} for k, v in datasets.items()])

# %% [markdown]
# **Look at** D1 and D2. Both are Restricted, and they are not handled alike: the level sets the
# floor, and health data adds its own rule about who may see it (task 4).

# %% [markdown]
# ## 2 · The three outputs (6')
#
# An output is new data. It does not inherit the level of its source: a table can be Public when
# its source is Restricted, and a draft can be Restricted when its final form will be Public.
# Look at the two tables before you classify them.

# %%
students = U.load("students.csv")
students["nationality_group"] = students["nationality"].where(students["nationality"] == "Saudi", "non-Saudi")
o1 = students.groupby("college").agg(students=("student_id", "size"), referred=("awn_referred", lambda s: (s == "yes").sum()))
o1["referral_rate"] = (o1["referred"] / o1["students"]).round(3)
reg = students[students["disability_status"] == "registered"]
o2 = pd.crosstab(reg["college"], reg["nationality_group"])
print("O1\n", o1, "\n\nO2\n", o2)

# %% [markdown]
# ✏️ **Exercise** · Classify O1, O2 and O3 **as they are today**: O1 has been computed and not yet
# approved for release, O2 is a draft, O3 goes to advisors.

# %%
def classify_outputs() -> dict[str, tuple[str, str]]:
    # BEGIN SOLUTION
    return {
        "O1": ("Public", "large counts, nobody singled out, a benefit in publishing; released once the data owner approves"),
        "O2": ("Restricted", "a cell of 1 points at one student's health data"),
        "O3": ("Restricted", "named students, for the advisors who act on the list"),
    }
    # END SOLUTION

# %%
try:
    outputs = {k: tuple(v) for k, v in classify_outputs().items()}
except NotImplementedError:
    outputs = {k: tuple(v) for k, v in U.reference("lab13_outputs").items()}
U.check(outputs["O2"][0] == "Restricted", "a table with a cell of 1 is not Public")
U.check(outputs["O3"][0] == "Restricted", "a named worklist is personal data")
U.check(outputs["O1"][0] in ("Public", "Restricted"), "O1 is Public after approval; Restricted until then is also a defensible answer")
smallest = int(o2.values.min())
print("smallest cell of O2:", smallest)
U.check(smallest == 1, "the draft has a cell of exactly one student")

# %% [markdown]
# ## 3 · The highest-level rule (3')
#
# The analyst joins the public timetable (D3) to the registry (D1) to study attendance by time of
# day. ✏️ **Exercise** · Write `combined_level(levels)`: the level of a file made from data of
# several levels. The policy's fourth principle gives the answer.

# %%
def combined_level(levels: list[str]) -> str:
    # BEGIN SOLUTION
    return min(levels, key=LEVELS.index)
    # END SOLUTION

# %%
try:
    joined = combined_level(["Public", "Restricted"])
    U.check(combined_level(["Restricted", "Secret", "Public"]) == "Secret", "the highest level of the parts wins")
except NotImplementedError:
    joined = U.reference("lab13_joined")["level"]
print("timetable joined to the registry:", joined)
U.check(joined == "Restricted", "a Public file joined to a Restricted one is Restricted")

# %% [markdown]
# ## 4 · The controls (6')
#
# The level decides how the item is marked, who may open it, how it is stored and sent, how long
# it is kept and what must happen before it is released.
#
# ✏️ **Exercise** · Choose the controls of each item from the list. A Public item needs no
# protection, but a table needs an approval before it becomes Public.

# %%
print(CONTROLS)

def controls() -> dict[str, list[str]]:
    # BEGIN SOLUTION
    restricted = ["protective marking", "need-to-know access", "encrypted storage", "retention schedule"]
    return {
        "D1": restricted,
        "D2": ["protective marking", "minimum staff access for health data", "encrypted storage", "retention schedule"],
        "D3": ["no control beyond accuracy"],
        "D4": restricted,
        "O1": ["approval by the data owner before release"],
        "O2": ["protective marking", "need-to-know access", "second-person check before release"],
        "O3": ["protective marking", "need-to-know access", "retention schedule"],
    }
    # END SOLUTION

# %%
try:
    ctrl = controls()
except NotImplementedError:
    ctrl = U.reference("lab13_controls")
levels = {**{k: v[0] for k, v in datasets.items()}, **{k: v[0] for k, v in outputs.items()}}
U.check(all(set(v) <= set(CONTROLS) for v in ctrl.values()) and set(ctrl) == set(levels), "every item has controls from the list")
U.check(all("protective marking" in ctrl[k] for k in ["D1", "D2", "D4", "O2", "O3"]), "every Restricted item is marked")
U.check("minimum staff access for health data" in ctrl["D2"], "health data is open to the fewest staff who need it")
U.check("second-person check before release" in ctrl["O2"], "a suppressed table is checked by a second person")
U.check("approval by the data owner before release" in ctrl["O1"], "the data owner approves a release")
register = U.table([{"item": k, "name": next(i["name"] for i in ITEMS if i["id"] == k), "level": levels[k],
                     "controls": "; ".join(ctrl[k])} for k in levels])
register

# %% [markdown]
# ## 5 · What may go into an AI tool (3')
#
# The Generative AI Guidelines for Government limit what an employee enters into a generative AI
# tool to data classified Public: nothing Restricted or higher, and nothing unclassified.
#
# ✏️ **Exercise** · Return the items that may be pasted into a hosted AI assistant today.

# %%
def ai_tool_ok(levels: dict[str, str]) -> list[str]:
    # BEGIN SOLUTION
    return ["D3"]   # O1 joins the list on the day its release is approved
    # END SOLUTION

# %%
try:
    ok = ai_tool_ok(levels)
except NotImplementedError:
    ok = U.reference("lab13_ai")
print("may be entered into an AI tool today:", ok)
U.check("D3" in ok and not ({"D1", "D2", "D4", "O2", "O3"} & set(ok)), "only Public data; never the registry, the extract, the draft or the worklist")
U.check(set(ok) <= {"D3", "O1"}, "O1 only once it has been approved and released")
out = Path("artifacts"); out.mkdir(exist_ok=True)
register.to_csv(out / "lab13_classification_register.csv", index=False)

# %% [markdown]
# ## ✱ Stretch · A declassification trigger
#
# O1 is Restricted until its release is approved. Write the trigger that changes its level
# (an event, a date or a period), who approves it, and what the register records on that day.

# %% [markdown]
# ## Check yourself
#
# 1. Why are student records Restricted and not Secret?
# 2. A colleague says: "the extract has no names, so it is Public." What is the reply?
# 3. Who makes the first classification, and who reviews it?
#
# <details><summary>Answers</summary>
#
# 1. The level follows the impact. Disclosing one individual's personal information is a low
#    impact in the policy's table; Secret is for serious, long-term harm to national interests or
#    to many entities.
# 2. Pseudonymised data is personal data, and each row is one student. Its disclosure would break
#    the PDPL, which is the policy's test for Restricted.
# 3. The person responsible for the data (the policy's Business Data Executive, here the
#    registrar) classifies; a reviewer in the data management office checks the level, within a
#    month of the first classification.
# </details>
#
# **Carry forward.** The register is half of the course's follow-up task (a classification and
# sharing table for one dataset at your work) and feeds the capstone's sharing decision.
