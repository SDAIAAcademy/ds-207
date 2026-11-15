---
course: "Responsible Data Practice and Conduct in Analytical Work"
code: "DS-207"
version: "2027.1.0"
deck: "day3"
day: 3
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/ds-207/slides/day3.html"
---

# Responsible Data Practice and Conduct in Analytical Work

## Day 3: Professional conduct

Document the work so others can check it, and hold the three conversations

#### [day3#title] Professional conduct

*SDAIA Academy · Responsible Data Practice and Conduct in Analytical Work*

Day 3: Document the work so others can check it, and hold the three conversations

Data Science Track · 3 teaching days + capstone day · 4 sessions · 4 labs · DS-207

#### [day3#agenda] Professional conduct

*Today*

- **Session 1 · Datasheets and analysis logs**: A reviewer must be able to trace a number to data, decisions and approvals
- **Session 2 · Scoping with a sponsor**: A vague request becomes a decision, a population, a measure and a criterion
- **Session 3 · Pushing back without obstructing**: Name the harm and the rule, offer an alternative, escalate when needed
- **Session 4 · Explaining limits**: Say what the result does not show and what it must not be used for

#### [day3#review-day2] What is the right next step?

*Review of Day 2*

**Question:** A rule misses struggling non-Saudi students more often than Saudi students: 62% against 43%, and the interval of the difference excludes zero. What does the analyst do next?

- A. Propose a lower threshold for non-Saudi students
- B. Report that the rule discriminates by nationality
- C. Name two candidate causes and run the check on which they disagree
- D. Leave the breakdown by nationality out of the report

### Session 1: Datasheets and analysis logs

#### [day3#s1] Datasheets and analysis logs

*Session 1*

- Fill a datasheet that states what the data is, how it was collected and what it must not be used for
- Keep an analysis log in which every decision has a reason, a date and an approver
- Tie a release to a version so a result can be traced and rerun

#### [day3#trace-a-number] "Where does the 55% come from?" must have an answer without you in the room

*The test of documentation*

1. **The number** 55% of struggling students referred
2. **The release** version, date, file fingerprints
3. **The data** a datasheet: what it is, what is wrong with it
4. **The decisions** a log: reason, date, approver

> **The reader.** A reviewer in six months, the data protection officer in an audit, your successor, and you.

#### [day3#datasheet-sections] A datasheet answers what a careful user would ask before using the data

*The datasheet*

| Section | The question |
| --- | --- |
| Motivation | Why was it made, for whom, for which decision? |
| Composition | What is one row? What is personal, sensitive, missing, and for whom? |
| Collection | Where does each field come from? What is recorded badly? |
| Preprocessing | What was dropped, coarsened, pseudonymised? |
| Uses | What is the approved use? What must it not be used for? |
| Distribution | Who may see it? What level? May it leave? |
| Maintenance | Who owns it? Kept until when? How is an error reported? |

#### [day3#state-the-weakness] A datasheet that states the data's weakness protects the analysis

*Honesty in the datasheet*

- **Collection, as written in the lab.** "Known to be recorded badly: attendance is about 17 points too low for the 300 students with a remote accommodation, because remote sessions leave no card reading."
- **Composition, as written in the lab.** "The midterm mark is missing for 1,244 students, all bridging-year entrants."

- A reader who finds the weakness alone stops trusting everything
- A reader who is told can weigh the results that depend on it

#### [day3#analysis-log] Every decision has a reason, a date and an approver

*The analysis log*

| Id | Decision | Approver |
| --- | --- | --- |
| L001 | Evaluate Awn on a pseudonymised extract of 13 fields | Registrar (data owner) |
| L002 | Add four group fields for the comparison | Data protection officer |
| L003 | Release two one-way tables, not the cross table | Registrar; suppression checked by the director |
| L004 | Do not release the Saudi-only table by college | Registrar |
| L005 | Report bridging-year entrants and remote accommodation separately | Director of the unit |

> **Six fields per entry.** Id, date, decision, reason, approver, where the evidence is.

#### [day3#approver-is-a-person] An approver is a named person with the authority to approve that thing

*Accountability*

- **The data owner.** Approves extracts and releases of the data he is responsible for. Here: the registrar.
- **The data protection officer.** Decides on sensitive fields, new purposes, disclosures and transfers.
- **The owner of the decision.** Approves how results are reported and used. Here: the director of the unit.

> **What goes wrong.** "Approved by the team." A team cannot be asked a question in an audit, and cannot be shown to have had the authority.

#### [day3#versioned-release] A release is a version, a date, fingerprints and one line of warning

*Decision records and versioned releases*

```json
{"version": "2026.11.1",
 "table": "Referral rate by college",
 "files": {"analysis_extract.csv":
           "2d9ebc9f490e9f0d"},
 "log_entries": ["L001", "L002", "L003"],
 "approved_by": "the registrar",
 "must_not_be_used_for":
   "ranking colleges or judging advisors"}
```

- A **fingerprint** (a hash of the file) changes if one byte changes: a version number is a claim, a fingerprint is a check
- A **decision record** keeps the options that were rejected, and why
- Templates live in **Git** beside the code, as Markdown or Quarto documents

#### [day3#records-the-law-asks] Some of this record is required

*Not only good practice*

- The University keeps a **record of processing**: the purpose, the categories of people, who the data is disclosed to, transfers, the retention period
- For statistics without consent, the purpose is stated **in that record**
- Sharing requests and their documents are kept for **five years**
- Disposal of data is **logged**

- **Your log feeds theirs.** The data protection officer keeps the record of processing. An analysis log with purposes, approvals and end dates is what lets her keep it true.

#### [day3#five-audit-questions] Five questions your documents must answer alone

*The peer audit*

1. Which file and which version produced the referral table released in November?
2. Who approved the use of disability status in the group comparison, and on what condition?
3. Why are bridging-year entrants reported separately?
4. What must the group comparison not be used for?
5. How many cells were suppressed in the release, and who checked the suppression?

> **The rule of the swap.** Your peer reads only your documents. No asking, no notebook.

#### [day3#check-documentation] Which log entry would survive an audit?

*Checkpoint*

**Question:** The analyst decided to merge two small nationality groups in a published table. Which entry lets a reviewer trace that decision?

- A. "2026-11-09. Merged groups X and Y in table T1: both had cells under 10. Approved by the registrar (data owner). Evidence: suppression log."
- B. "Merged some categories in T1 for privacy reasons. Approved."
- C. A comment in the notebook cell that does the merge
- D. "2026-11-09. Merged X and Y in T1. Decided by the analyst."

#### [day3#lab-3-1] Datasheet and log

Lab 3.1 · 25 min

Fill a datasheet and log three decisions with their approver, then let a peer audit them.

[D3_1_datasheet_log.ipynb](https://sdaiaacademy.github.io/ds-207/labs/D3_1_datasheet_log.ipynb)

- [ ] Fill the datasheet from the data and the notice (8 min)
- [ ] Log three decisions with reason, date and approver (6 min)
- [ ] Tag the release with its file fingerprints (4 min)
- [ ] Swap with a peer and answer five audit questions (5 min)
- [ ] Fix what the peer could not answer (2 min)
- [ ] ✱ Stretch: Add a decision record for the choice of threshold, with the options that were rejected

### Session 2: Scoping with a sponsor

#### [day3#s2] Scoping with a sponsor

*Session 2*

- Ask the questions that turn a request into a decision, a population, a measure and a time frame
- Agree success criteria and what is out of scope before any analysis starts
- Record the agreement in a scope note the sponsor confirms

#### [day3#vague-request] A request is usually one sentence, and the sentence is not the question

*How requests arrive*

**Director:** Is Awn working? The vice-rector will ask me next month.

**Analyst, too fast (weak example):** I will send you the referral numbers by Thursday.

**Analyst (good example):** What will you decide once you know?

- "Working" could mean reaching struggling students, helping them, or costing less
- Each meaning needs different data, and one of them cannot be answered at all
- Starting the analysis before asking is the most expensive way to find that out

#### [day3#four-questions] Four questions turn a request into something answerable

*The conversation*

- **The decision.** "What will you decide once you know?"
- **The population.** "Which students, which term?"
- **The measure.** "What would you count, and compared with what?"
- **The time.** "When is the decision taken?"

> **Order matters.** The decision first. It tells you which answer would change what the sponsor does, and it is the purpose the law asks you for.

#### [day3#success-criteria] Agree what a useful answer looks like before you produce one

*Success criteria*

- "If the answer were X, what would you do? And if it were Y?"
- The **form**: one page, a table, a number with its definition
- The **precision** that matters: to the point, or "more than half"?
- What would make the sponsor **not believe** the answer

- **In brief B2.** "One page the director can take to the council: the two rates, the groups for which they differ clearly, and the cause where it could be established."

#### [day3#out-of-scope] Write down what you will not do, while everyone still agrees

*Out of scope*

| The sponsor's opening sentence | What was really needed | Out of scope |
| --- | --- | --- |
| "I need the data on why engineering students are failing." | Whether to add tutorial sections to two first-year courses | Naming students or instructors |
| "Is Awn working?" | Extend the rule, or change its thresholds first | Whether support helps: no comparison group |
| "A nice number for the annual report." | One figure with its definition, beside last year's | Breakdowns with small counts |

> **Requests grow.** The line "no lists of students" is the one you will point to in three weeks.

#### [day3#scope-note] The scope note: nine fields, one sentence each, confirmed by the sponsor

*The record*

- **Decision**
- **Question**
- **Population**

- **Measure**
- **Success criterion**
- **Out of scope**

- **Data**
- **Deadline**
- **Confirmed by**

> **Send it within the hour.** Five lines, the question first, and one sentence you ask the sponsor to confirm by reply. An unconfirmed note is your opinion of what was agreed.

#### [day3#how-to-ask] Three habits make the six minutes work

*Technique*

- **Ask, then wait.** One question at a time. The pause after it is where the real answer comes.
- **Say it back.** "So the decision is whether to add tutorials, and you need it in three weeks." Sponsors correct a summary more easily than they answer a question.
- **Propose the question.** Leave with a sentence that ends in a question mark and that data can answer. Read it aloud before you go.

#### [day3#roleplay-scoping] Six minutes a round: four to talk, two for feedback. Rotate the roles each round

*Role-play · three rounds*

##### One round

- Round 1 · brief B1
- Round 2 · brief B2
- Round 3 · brief B3

#### [day3#check-scoping] Which is the best first question?

*Checkpoint*

**Question:** A dean says: "Get me the data on why our students are failing." What does the analyst ask first?

- A. "Which fields do you want in the extract?"
- B. "Would you prefer a regression or a simple breakdown?"
- C. "Do you mean first-year students or all students?"
- D. "What do you have to decide, and by when?"

#### [day3#lab-3-2] Scope in six minutes

Lab 3.2 · 25 min

Turn a vague request into a question in a timed role-play, in threes, and write the scope note.

[D3_2_scoping_roleplay.ipynb](https://sdaiaacademy.github.io/ds-207/labs/D3_2_scoping_roleplay.ipynb)

- [ ] Read the brief and your role card (3 min)
- [ ] Round 1: analyst, sponsor, observer (6 min)
- [ ] Round 2: rotate the roles (6 min)
- [ ] Round 3: rotate the roles (6 min)
- [ ] Write your scope note (4 min)
- [ ] ✱ Stretch: Send the scope note as a five-line message and ask the sponsor to confirm one sentence

### Session 3: Pushing back without obstructing

#### [day3#s3] Pushing back without obstructing

*Session 3*

- Refuse an unsafe request by naming the harm and the rule, not by citing policy at the sponsor
- Offer a lawful alternative that serves the sponsor's decision
- Recognise when to escalate to the data protection officer and record the agreement

#### [day3#the-risk-list] "A list of every student likely to fail, with names and a score, by Sunday"

*The request*

- **Why it is unsafe.** A named list of predicted failure is a new purpose and reaches people who do not advise the student. The score is wrong for known groups. A label that travels to deans can follow a student into grading and discipline.
- **What she has to decide.** Where to put twelve new advisors, and whether the colleges act on referrals. Neither decision needs a name.

> **The sponsor is not the villain.** Dr. Ibtisam Al-Khayyat wants struggling students helped. The request is the wrong tool for a good aim.

#### [day3#anatomy-of-a-no] A refusal that works has five parts, and the alternative comes early

*The structure*

1. **1 · Listen** what must she decide?
2. **2 · Alternative** what serves that decision
3. **3 · Harm** to students, in plain words
4. **4 · Rule** and who decides
5. **5 · Record** what was agreed

> **Why this order.** She came with a problem. Someone who hears first how it gets solved by Sunday can listen to the reason. Someone who hears a rule first hears a refusal.

#### [day3#alternative-with-numbers] An alternative you can show beats one you can describe

*The alternative, built*

| College | Referred | Struggled | Missed | Advisors of 12 |
| --- | --- | --- | --- | --- |
| Health Sciences | 479 | 488 | 165 | 2.7 |
| Science | 390 | 438 | 192 | 2.4 |
| Arts and Humanities | 317 | 363 | 181 | 2.0 |
| Engineering | 332 | 354 | 172 | 1.9 |
| Business | 306 | 310 | 153 | 1.7 |
| Computing | 216 | 238 | 119 | 1.3 |

- Answers "where do twelve advisors go?"
- Every cell is 10 or more
- Named worklists stay with each student's advisor, as today

#### [day3#pressures] Three pressures, and a reply to each that is not a rule

*What you will hear*

| She says | A reply that keeps the conversation |
| --- | --- |
| "The council meets on Monday." | "You will have the table for the council on Sunday. It answers where the advisors go." |
| "Another university does this already." | "Ours would wrongly list most students who attend remotely with an accommodation. I would not want your name on that list." |
| "I am the vice-rector. I am allowed to see student data." | "You are. The question is what this decision needs, and it does not need names. If you need them, the data protection officer decides, and I will take it to her today." |

#### [day3#escalate] Escalating is saying aloud whose decision it is

*Escalation*

- **When:** the sponsor still wants named or sensitive data, a new purpose, a disclosure or a transfer
- **To whom:** the data protection officer, who monitors how the law is applied and supervises impact assessments
- **How:** three lines: what was asked and by whom, what you offered, the decision you need

- **Copy the sponsor.** Escalation said aloud and copied is a service: the decision was never the analyst's, and never the sponsor's alone. Escalation behind someone's back is a complaint.

#### [day3#obstruction] Obstructing is as much a failure as complying

*The other failure*

- **Comply.** Send the list. The harm happens, with your name in the log.
- **Obstruct.** "We cannot, it is the law." No alternative, no route. The sponsor asks someone else, who sends a worse list.
- **Push back.** The decision is served by Sunday, the names stay with advisors, the record says who agreed, and the open question has an owner.

> **The record.** Asked for, will deliver, will not deliver, why, who decides more, confirmed by. What is not written down was not agreed.

#### [day3#roleplay-pushback] Five minutes a round: three to talk, two for the observer's five scores

*Role-play · three rounds*

##### One round

- Listen
- Alternative
- Harm
- Rule and who decides
- Record

#### [day3#check-pushback] Which reply pushes back without obstructing?

*Checkpoint*

**Question:** A dean asks for the names of students who used the counselling service, "so lecturers can go easy on them". Which reply is best?

- A. "I cannot. Counselling data is health data."
- B. "You want lecturers to support students under strain. I can give counts by department, and the service can contact lecturers for students who agree. Names would break what students were told."
- C. "I will send the list marked confidential, for department heads only."
- D. "That is a question for the data protection officer, not for me."

#### [day3#lab-3-3] The risk list

Lab 3.3 · 25 min

Role-play a request for a risk list and agree a lawful alternative.

[D3_3_pushback_roleplay.ipynb](https://sdaiaacademy.github.io/ds-207/labs/D3_3_pushback_roleplay.ipynb)

- [ ] Read the request and prepare two alternatives (5 min)
- [ ] Round 1: analyst, sponsor, observer (5 min)
- [ ] Round 2: rotate the roles (5 min)
- [ ] Round 3: rotate the roles (5 min)
- [ ] Record the agreement and the escalation (5 min)
- [ ] ✱ Stretch: The sponsor insists: write the three-line escalation to the data protection officer

### Session 4: Explaining limits

#### [day3#s4] Explaining limits

*Session 4*

- State what an analysis cannot show, separately from how uncertain it is
- Write a limits statement a non-specialist cannot misread
- Choose the capstone engagement and list what its pack must contain

#### [day3#uncertainty-and-limits] An interval tells you how sure; a limit tells you what was never measured

*Two different things*

- **Uncertainty.** How far the number could move if you measured again. Awn referred 55% of struggling students, between 53% and 57%. Small, with 2,191 students.
- **Limits.** What the number does not measure however often you measure: whether support helps, whether the label is right, whether the record is right, whether next term will be like this one.

> **What goes wrong.** A tight interval read as "the analysis is solid". Precision about the wrong thing is still the wrong thing.

#### [day3#six-limits] Six real limits, and two that only sound like limits

*The Awn evaluation*

- No test of whether support helps: no comparison group
- One term of one year
- Attendance under-recorded for remote accommodation
- Marks missing for bridging-year entrants
- "Struggled" is one definition; withdrawals can count as "ok"
- It describes groups, not any one student's risk

- **Not limits.** "The sample is too small": 18,000 students give the overall rate to about two points. "The data is pseudonymised": a pseudonym changes who can be identified, not any rate.

#### [day3#three-sentences] Three sentences that travel with the number

*The limits statement*

1. **What it shows.** "In term 1, Awn referred 55% of the students who ended the term struggling (between 53% and 57%), so it missed 45% of them."
2. **What it does not show, and for whom it is worse.** "The analysis did not test whether the support that follows a referral helps, and the rule is known to be less reliable for two groups: it wrongly refers many students with a remote-attendance accommodation and misses most struggling bridging-year entrants."
3. **What it must not be used for.** "The result describes groups of students and must not be used to judge, rank or list any individual student."

#### [day3#misreadings] A statement works if it blocks the ways a hurried reader will misread the number

*Testing the statement*

| The misreading | Blocked by |
| --- | --- |
| "Awn causes students to pass." | Sentence 2: support was not tested |
| "A student Awn did not refer is safe." | Sentence 1: it missed 45% |
| "The rule works equally well for every group." | Sentence 2: the two groups, named |
| "The list of referred students can decide who repeats a course." | Sentence 3: must not be used for |

> **Which side of the number.** "Referred 55%" invites the second misreading. "Missed 45%" blocks it. Same fact.

#### [day3#human-oversight] A referral is a prompt for a person, and the statement keeps it that way

*Who acts on the result*

- Awn's output goes to an **advisor**, who talks to the student and decides
- People tend to favour a system's output over other evidence: the guide's **automation bias**
- "Must not be used to judge, rank or list" is the line that protects the advisor's judgement

- **In every release.** The unit's policy asks for a version, a date, an approver and a line that says what the table must not be used for. The line is not decoration: it is the record that you said it.

#### [day3#capstone-kickoff] Three engagements; choose one and build its responsible-practice pack

*Capstone kickoff*

| Engagement | The rule | The partner | The sponsor asks |
| --- | --- | --- | --- |
| Scholarship Office | Flags awards for review | A charity that co-funds awards | "Which students do not deserve their award?" |
| Student Housing | Gives priority for rooms | The city's municipality | "Prove the priority rule is fair." |
| Career Centre | Shortlists for internships | A private employers' council | "Send me the names of those not shortlisted." |

> **Each folder.** 4,000 synthetic records, the rule, the sponsor's brief and the partner's request, in `labs/capstone/`.

#### [day3#the-pack] Six documents in five scored parts, each one a lab you have done

*What you hand in*

| Part of the pack | The lab that taught it | Weight |
| --- | --- | --- |
| Sharing decision with conditions and classification | 1.1, 1.3, 1.4 | 25 |
| Release tables, suppression log, differencing check | 2.1 | 20 |
| Group comparison: rates, intervals, two bias types, the check | 2.3, 2.4 | 20 |
| Datasheet and analysis log | 1.2, 3.1 | 20 |
| Scope note, with what the analysis must not be used for | 3.2, 3.3, 3.4 | 15 |

> **The defence.** Eight minutes: six on the pack, with a two-minute role-play inside, and two in which the assessor changes one fact of the partner's request.

#### [day3#check-limits] Which sentence belongs under the number?

*Checkpoint*

**Question:** A slide for the University council will say "Awn referred 55% of struggling students". There is room for one more line. Which one?

- A. "95% confidence interval: 53% to 57%."
- B. "Computed on a pseudonymised extract of 18,000 students."
- C. "It missed 45%, is unreliable for two groups, and must not be used to judge individual students."
- D. "Results should be interpreted with caution."

#### [day3#lab-3-4] Three sentences and the capstone case

Lab 3.4 · 25 min

Write a three-sentence limits statement and choose the capstone case.

[D3_4_limits_statement.ipynb](https://sdaiaacademy.github.io/ds-207/labs/D3_4_limits_statement.ipynb)

- [ ] Read the result and its interval (3 min)
- [ ] List what the analysis cannot show (5 min)
- [ ] Write the three-sentence limits statement (7 min)
- [ ] Test it against four misreadings (5 min)
- [ ] Choose the capstone engagement and open its files (5 min)
- [ ] ✱ Stretch: Rewrite the statement for a student newspaper, without a number that could mislead

#### [day3#wrap-up] Three things to keep

*Day 3*

- **Write it so a stranger can check it.** A datasheet that states the weakness, a log with a named approver, a release with a fingerprint.
- **The decision first.** Ask what the sponsor has to decide. The same sentence is the scope and the lawful purpose.
- **No, with an alternative.** Serve the decision, name the harm, say who decides, write it down. Then say what the number does not show.

#### [day3#next] The capstone: your pack, defended

*Next*

Six documents for one engagement, in a public repository, and eight minutes in front of an assessor who will change one fact.

- Before the day: build the pack from the template
- Rehearse the two-minute role-play with a peer as your sponsor
