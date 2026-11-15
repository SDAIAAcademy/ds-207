# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 2.1 · Suppress, then attack
#
# Day 2 · Session 1 (Aggregate release and small cells) · 25 min.
#
# The unit wants to publish three tables. The release policy says no count of 1 to 9 students
# leaves the unit. You count the cells under the threshold, suppress them with a log, then attack
# your own table: first with its totals, then with a table the unit published last month. A
# release is ready when both attacks fail.
#
# **Reference state.** `data/students.csv`, `data/release_policy.md` and
# `data/release_2026_10_disability_by_college.csv` (last month's published table). Nothing from
# another lab.
#
# **Tasks**
# - [ ] 1 · Count the cells under the threshold in three draft tables (4')
# - [ ] 2 · Suppress them and log each cell with its reason (6')
# - [ ] 3 · Recover a suppressed cell from the totals (4')
# - [ ] 4 · Add complementary suppression and test again (6')
# - [ ] 5 · Difference the table against an earlier release (5')
# - [ ] ✱ Stretch · Round the counts to a base of 5 in place of suppression and compare what a reader loses

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

print(U.text("release_policy.md"))
T = U.THRESHOLD
students = U.load("students.csv")
students["nationality_group"] = students["nationality"].where(students["nationality"] == "Saudi", "non-Saudi")
registered = students[students["disability_status"] == "registered"]
referred = students[students["awn_referred"] == "yes"]

# %% [markdown]
# ## 1 · Three draft tables (4')
#
# - **T1** students by college and nationality
# - **T2** referred students by college and disability status
# - **T3** students with a registered disability by college and nationality group
#
# ✏️ **Exercise** · Write `small_cells(table)`: the number of cells with a count from 1 to 9.

# %%
T1 = pd.crosstab(students["college"], students["nationality"])
T2 = pd.crosstab(referred["college"], referred["disability_status"])
T3 = pd.crosstab(registered["college"], registered["nationality_group"])
TABLES = {"T1": T1, "T2": T2, "T3": T3}

def small_cells(table: pd.DataFrame) -> int:
    # BEGIN SOLUTION
    return int(((table > 0) & (table < T)).sum().sum())
    # END SOLUTION

# %%
try:
    small = {name: small_cells(t) for name, t in TABLES.items()}
except NotImplementedError:
    small = U.reference("lab21_small")
print("cells with a count of 1 to 9:", small)
print(T3)
U.check(small["T2"] == 0, "T2 needs no suppression: not every table does")
U.check(small["T3"] == 5, "T3 has five cells under the threshold")
U.check(small["T1"] > 0, "T1 has small cells too")

# %% [markdown]
# ## 2 · Primary suppression, with a log (6')
#
# ✏️ **Exercise** · Write `primary(table)`: a table of True and False of the same shape, True where
# the cell must be suppressed. Then the cell below prints the table as a reader would see it and
# writes one log line per suppressed cell.

# %%
def primary(table: pd.DataFrame) -> pd.DataFrame:
    # BEGIN SOLUTION
    return (table > 0) & (table < T)
    # END SOLUTION

def shown(table: pd.DataFrame, mask: pd.DataFrame, totals: bool = True) -> pd.DataFrame:
    """The table as released: suppressed cells show 'c'; row and column totals stay exact."""
    out = table.astype(object).where(~mask, "c")
    if totals:
        out["Total"] = table.sum(axis=1)
        out.loc["Total"] = list(table.sum(axis=0)) + [int(table.values.sum())]
    return out

def log_lines(name: str, table: pd.DataFrame, mask: pd.DataFrame, kind: str, reason: str) -> list[dict]:
    return [{"table": name, "row": r, "column": c, "kind": kind, "reason": reason}
            for r in table.index for c in table.columns if mask.loc[r, c]]

# %%
try:
    mask3 = primary(T3)
except NotImplementedError:
    mask3 = (T3 > 0) & (T3 < T)
log = log_lines("T3", T3, mask3, "primary", f"count of 1 to {T - 1}")
print(shown(T3, mask3))
U.check(int(mask3.sum().sum()) == 5 and len(log) == 5, "five cells suppressed, five log lines")
U.check(bool(mask3.loc["Computing", "non-Saudi"]), "the cell of one student is suppressed")

# %% [markdown]
# ## 3 · Attack one: the totals (4')
#
# The table above still prints its totals. ✏️ **Exercise** · Write `recoverable(table, mask)`: for
# every row and every column that has **exactly one** suppressed cell, recover that cell by
# subtracting the shown cells from the total. Return a list of `(row, column, value)`.

# %%
def recoverable(table: pd.DataFrame, mask: pd.DataFrame) -> list[tuple]:
    # BEGIN SOLUTION
    found = set()
    for r in table.index:
        if mask.loc[r].sum() == 1:
            c = mask.loc[r].idxmax()
            found.add((r, c, int(table.loc[r].sum() - table.loc[r][~mask.loc[r]].sum())))
    for c in table.columns:
        if mask[c].sum() == 1:
            r = mask[c].idxmax()
            found.add((r, c, int(table[c].sum() - table[c][~mask[c]].sum())))
    return sorted(found)
    # END SOLUTION

# %%
try:
    leaked = recoverable(T3, mask3)
except NotImplementedError:
    leaked = [tuple(x) for x in U.reference("lab21_leaked")]
for row in leaked:
    print("recovered:", row)
U.check(len(leaked) == 5, "all five suppressed cells come back from the row totals")
U.check(("Computing", "non-Saudi", 1) in leaked, "including the single student in Computing")

# %% [markdown]
# **Look at** what happened: the suppression changed how the table looks and nothing about what it
# reveals. A suppressed cell beside an exact total is a subtraction exercise.

# %% [markdown]
# ## 4 · Complementary suppression (6')
#
# The unit's rule 2: where one suppressed cell could be recovered from a total, a second cell is
# suppressed. ✏️ **Exercise** · Write `complementary(table, mask)`: repeat until nothing changes:
# in every row and every column that has exactly one suppressed cell, or whose suppressed cells
# add up to less than the threshold, also suppress the smallest cell that is still shown.

# %%
def complementary(table: pd.DataFrame, mask: pd.DataFrame) -> pd.DataFrame:
    # BEGIN SOLUTION
    mask = mask.copy()
    changed = True
    while changed:
        changed = False
        for axis in (0, 1):
            t, m = (table, mask) if axis == 0 else (table.T, mask.T)
            for line in t.index:
                hidden = m.loc[line]
                if hidden.sum() == 0 or hidden.all():
                    continue
                if hidden.sum() == 1 or t.loc[line][hidden].sum() < T:
                    candidates = t.loc[line][~hidden]
                    positive = candidates[candidates > 0]
                    pick = (positive if len(positive) else candidates).idxmin()
                    if axis == 0:
                        mask.loc[line, pick] = True
                    else:
                        mask.loc[pick, line] = True
                    changed = True
                    m = mask if axis == 0 else mask.T
    return mask
    # END SOLUTION

# %%
try:
    full3 = complementary(T3, mask3)
    full1 = complementary(T1, primary(T1))
    after = {"T3_suppressed": int(full3.sum().sum()), "T3_recoverable": len(recoverable(T3, full3)),
             "T1_primary": int(primary(T1).sum().sum()), "T1_suppressed": int(full1.sum().sum()),
             "T1_recoverable": len(recoverable(T1, full1))}
except NotImplementedError:
    after = U.reference("lab21_after")
    full3 = pd.DataFrame(U.reference("lab21_mask3")).astype(bool)
print(after)
print(shown(T3, full3))
log += log_lines("T3", T3, full3 & ~mask3, "complementary", "protects a suppressed cell from subtraction")
U.check(after["T3_recoverable"] == 0 and after["T1_recoverable"] == 0, "no cell comes back from a total any more")
U.check(after["T3_suppressed"] == 10, "T3 now hides 10 of its 12 cells")

# %% [markdown]
# **Look at** the price. Ten of twelve cells are gone, including Saudi counts of 50 to 92 that
# nobody needed to hide. When complementary suppression eats the table, the table is the wrong
# design. Two one-way tables say almost as much and need no suppression:

# %%
by_college = T3.sum(axis=1).rename("registered disability")
by_group = T3.sum(axis=0).rename("registered disability")
print(by_college.to_frame().T, "\n\n", by_group.to_frame().T)
U.check(int(by_college.min()) >= T and int(by_group.min()) >= T, "every cell of the two one-way tables is 10 or more")

# %% [markdown]
# ## 5 · Attack two: differencing (5')
#
# Last month the unit published registered-disability counts by college for **all** students.
# This month a dean asks for the same table for **Saudi** students only. Each table passes the
# threshold on its own.
#
# ✏️ **Exercise** · Write `difference(new, old)`: subtract the new table from the old one, college
# by college, and return the differences that are 1 to 9.

# %%
old = U.load("release_2026_10_disability_by_college.csv").set_index("college")["registered_disability_all_students"].astype(int)
new = T3["Saudi"]
print(pd.DataFrame({"published last month, all": old, "asked for now, Saudi only": new}))
U.check(int(old.min()) >= T and int(new.min()) >= T, "each table alone passes the threshold")

def difference(new: pd.Series, old: pd.Series) -> dict[str, int]:
    # BEGIN SOLUTION
    d = (old - new).astype(int)
    return {k: int(v) for k, v in d.items() if 0 < v < T}
    # END SOLUTION

# %%
try:
    revealed = difference(new, old)
except NotImplementedError:
    revealed = U.reference("lab21_difference")
print("revealed by subtraction:", revealed)
U.check(revealed.get("Computing") == 1, "the difference is the one non-Saudi student with a registered disability in Computing")
U.check(len(revealed) == 5, "five colleges' small counts come out of two harmless-looking tables")
decision = "Do not release the Saudi-only table by college. Offer the University-level split by nationality group."
log.append({"table": "Saudi-only disability by college", "row": "all", "column": "all", "kind": "not released",
            "reason": "differencing against the release of 2026-10 reveals counts of 1 to 9"})
out = Path("artifacts"); out.mkdir(exist_ok=True)
pd.DataFrame(log).to_csv(out / "lab21_suppression_log.csv", index=False)
print(decision, "\nlog lines:", len(log))

# %% [markdown]
# ## ✱ Stretch · Rounding
#
# Round every count of T3 to the nearest multiple of 5 and publish no exact totals. What can a
# reader still learn? What can an attacker no longer compute? What does a reader lose compared
# with the two one-way tables?

# %% [markdown]
# ## Check yourself
#
# 1. Why is a zero not suppressed by the unit's rule, and when would a zero be a problem?
# 2. A cell of 54 was suppressed in task 4. Was that a mistake?
# 3. What must the unit keep to make the differencing check possible next month?
#
# <details><summary>Answers</summary>
#
# 1. A zero says nobody is in the cell, which points at no one. It becomes a disclosure when it
#    tells you something about everyone else: if a group of 12 has 0 students who were not
#    referred, all 12 were referred.
# 2. No. It was suppressed to protect its neighbour of 1 from subtraction. It is also the reason
#    to redesign the table.
# 3. A register of every table released: its population, its breakdown, its date and its version.
#    You cannot difference against a release nobody remembers.
# </details>
#
# **Carry forward.** `artifacts/lab21_suppression_log.csv` is the model for the capstone's
# suppression log: one line per cell, with the kind and the reason.
