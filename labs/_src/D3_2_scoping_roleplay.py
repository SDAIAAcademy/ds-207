# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 3.2 · Scope in six minutes
#
# Day 3 · Session 2 (Scoping with a sponsor) · 25 min.
#
# A role-play in threes: analyst, sponsor, observer. Three rounds of six minutes, three briefs, so
# everyone plays the analyst once. The analyst has six minutes to turn one vague sentence into a
# question that can be answered. Then each of you writes the scope note for the brief you handled
# as analyst. No AI assistant in this lab: the skill is the conversation.
#
# **Reference state.** `data/sponsor_briefs.json`. Nothing from another lab.
#
# **Tasks**
# - [ ] 1 · Read the brief and your role card (3')
# - [ ] 2 · Round 1: analyst, sponsor, observer (6')
# - [ ] 3 · Round 2: rotate the roles (6')
# - [ ] 4 · Round 3: rotate the roles (6')
# - [ ] 5 · Write your scope note (4')
# - [ ] ✱ Stretch · Send the scope note as a five-line message and ask the sponsor to confirm one sentence

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

pack = U.json("sponsor_briefs.json")
BRIEFS = {b["id"]: b for b in pack["briefs"]}
SCOPE_FIELDS = pack["scope_fields"]

# %% [markdown]
# ## 1 · Roles and cards (3')
#
# Name yourselves P1, P2 and P3. The table says who plays what in each round.

# %%
ROUNDS = U.table([
    {"round": 1, "brief": "B1", "analyst": "P1", "sponsor": "P2", "observer": "P3"},
    {"round": 2, "brief": "B2", "analyst": "P2", "sponsor": "P3", "observer": "P1"},
    {"round": 3, "brief": "B3", "analyst": "P3", "sponsor": "P1", "observer": "P2"},
])
ROUNDS

# %% [markdown]
# **The analyst** sees only the request. Run `analyst_card` for your round.
#
# **The sponsor** runs `sponsor_card` for the round **on their own screen** and does not show it.
# The card holds what the sponsor really needs. Rules for the sponsor: answer truthfully and
# briefly; volunteer nothing; if the analyst proposes work, say "fine" unless it misses your
# decision.
#
# **The observer** runs `observer_sheet` and ticks what the analyst asked about.

# %%
def analyst_card(brief_id: str) -> None:
    b = BRIEFS[brief_id]
    print(f"ANALYST · {brief_id}\n{b['sponsor']} says:\n   \"{b['request']}\"\n\nYou have six minutes. Leave with a question you can answer.")

def sponsor_card(brief_id: str) -> None:
    b = BRIEFS[brief_id]
    print(f"SPONSOR · {brief_id} · do not show this screen\nYou are {b['sponsor']}. Open with:\n   \"{b['request']}\"\n\nWhat you know, and say only when asked:")
    for k, v in b["hidden"].items():
        print(f"   {k.replace('_', ' '):13s} {v}")

ASKED = ["decision", "population", "measure", "deadline", "out_of_scope"]

def observer_sheet(brief_id: str) -> dict[str, bool]:
    print(f"OBSERVER · {brief_id} · tick what the analyst found out, and note the best question you heard")
    for item in ASKED:
        print(f"   [ ] {item.replace('_', ' ')}")
    return {item: False for item in ASKED}

analyst_card("B1")

# %% [markdown]
# ## 2 · Round 1 (6')
#
# Four minutes of conversation, two of feedback: the observer says what was found out and what
# was not, then the sponsor reveals the card. The trainer runs the timer on the slide.

# %%
sheet_round1 = observer_sheet("B1")

# %% [markdown]
# ## 3 · Round 2 (6')
#
# Rotate. The new analyst runs `analyst_card("B2")`, the new sponsor `sponsor_card("B2")`.

# %%
sheet_round2 = observer_sheet("B2")

# %% [markdown]
# ## 4 · Round 3 (6')
#
# Rotate again: brief B3.

# %%
sheet_round3 = observer_sheet("B3")

# %% [markdown]
# ## 5 · The scope note (4')
#
# The scope note is the written agreement: nine fields, each one a sentence. It is what you send
# the sponsor afterwards, and what you point to when the request grows.
#
# ✏️ **Exercise** · Set `MY_BRIEF` to the brief you handled as analyst and return its scope note.
# `question` ends with a question mark and can be answered with data; `success_criterion` says
# what a useful answer looks like to the sponsor; `out_of_scope` names at least one thing.

# %%
MY_BRIEF = "B2"

def scope_note() -> dict[str, str]:
    # BEGIN SOLUTION
    return {
        "decision": "Whether to extend Awn to all colleges next term as it is, or to change its inputs first.",
        "question": "Of the students who ended term 1 struggling, what share did Awn refer, and what share of its referrals went to students who did not struggle, overall and by group?",
        "population": "All 18,000 students enrolled in term 1 of 2026-27.",
        "measure": "Missed rate and false-referral rate with 95% intervals, by college, level, gender, nationality group and disability status.",
        "success_criterion": "One page the director can take to the council: the two rates, the groups for which they differ clearly, and the cause where it could be established.",
        "out_of_scope": "Whether the support that follows a referral helps students: there is no comparison group. No lists of students.",
        "data": "The pseudonymised analysis extract (13 fields) and the roll-call audit; group fields as approved in log entry L002.",
        "deadline": "A draft in 2 weeks, the page in 4 weeks, before the council meets.",
        "confirmed_by": "Jassim Al-Nuaimi, director of the Student Success Unit, by reply to the note.",
    }
    # END SOLUTION

# %%
try:
    note = scope_note()
except NotImplementedError:
    note = U.reference("lab32_note")
U.check(MY_BRIEF in BRIEFS, "the brief is one of the three")
U.check(list(note) == SCOPE_FIELDS and all(len(v) > 15 for v in note.values()), "nine fields, each a full sentence")
U.check(note["question"].strip().endswith("?"), "the question is a question")
U.check(note["decision"].lower().startswith("whether") or "decide" in note["decision"].lower(), "the decision is stated as a choice the sponsor has to make")
U.check(any(ch.isdigit() for ch in note["deadline"]), "the deadline has a number in it")
U.check("no " in note["out_of_scope"].lower() or "not " in note["out_of_scope"].lower() or "whether" in note["out_of_scope"].lower(), "something is named as out of scope")
out = Path("artifacts"); out.mkdir(exist_ok=True)
(out / "lab32_scope_note.md").write_text("# Scope note\n\n" + "\n".join(f"- **{k.replace('_', ' ').capitalize()}:** {v}" for k, v in note.items()) + "\n", encoding="utf-8")
U.table([{"field": k, "agreed": v} for k, v in note.items()])

# %% [markdown]
# **Look at** your note beside the sponsor's first sentence. How much of the note was in the
# request? How much did you have to ask for?

# %% [markdown]
# ## ✱ Stretch · The confirmation message
#
# Write the message you would send the sponsor within the hour: five lines, the question first,
# and one sentence you ask the sponsor to confirm by reply. Which sentence do you choose?

# %% [markdown]
# ## Check yourself
#
# 1. Why ask for the decision before the data?
# 2. The sponsor says "just give me everything you have". What is the next question?
# 3. Why write down what is out of scope?
#
# <details><summary>Answers</summary>
#
# 1. The decision tells you which answer would change what the sponsor does. Without it you
#    cannot tell a useful result from an interesting one, and you cannot say what data the
#    purpose needs.
# 2. "What will you decide with it, and by when?" Everything is not a purpose, and a purpose is
#    what the law and your own time both need.
# 3. Requests grow. The line that says "no lists of students" or "not whether support helps" is
#    the one you will point to in three weeks.
# </details>
#
# **Carry forward.** The scope note is a file of the capstone pack and 15 points of its rubric.
# In the capstone the request you rescope is also an unsafe one: that is the next lab.
