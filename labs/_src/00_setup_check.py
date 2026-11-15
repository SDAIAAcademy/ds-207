# %% [markdown]
# # Setup check
#
# Run every cell before Day 1. It proves that Python and pandas work and that the course data is
# where the labs expect it. No lab of this course calls a model, needs a key or downloads
# anything beyond the repository.

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
        os.chdir("..")
sys.path.insert(0, os.getcwd())

# %%
problems = []
print("Python", sys.version.split()[0])
if sys.version_info < (3, 11):
    problems.append("Python 3.11 or later is needed")
try:
    import pandas as pd
    print("pandas", pd.__version__)
except ImportError:
    problems.append("pandas is missing: locally run the notebooks with uv from labs/; in Colab it is already there")

# %%
try:
    import qimam as U
    students = U.load("students.csv")
    print("students.csv:", len(students), "rows,", len(students.columns), "columns")
    if (len(students), len(students.columns)) != (18000, 30):
        problems.append("students.csv is not the course file: run prepare_data.py in labs/")
    low, high = U.wilson(1209, 2191)
    print(f"Wilson interval of 1209 / 2191: {low:.3f} to {high:.3f}")
except Exception as error:  # the message is what the participant needs
    problems.append(f"the course data could not be read: {error}")

# %%
print("\nReady for Day 1." if not problems else "\nFix before Day 1:\n- " + "\n- ".join(problems))
assert not problems, problems
