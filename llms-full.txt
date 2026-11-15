---
course: "Responsible Data Practice and Conduct in Analytical Work"
code: "DS-207"
version: "2027.1.0"
scope: "course"
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/ds-207/"
---

# Responsible Data Practice and Conduct in Analytical Work

Handle an analytical request lawfully and fairly: test it against the PDPL, classify and share with conditions, release tables that single nobody out, compare groups honestly, document the work and hold the conversation that rescopes an unsafe request

Participants handle an analytical engagement for a fictional university's student-success unit. They test requests against the Personal Data Protection Law (PDPL), classify the data and decide what may be shared with a government partner, suppress small cells in aggregate outputs, compare outcome and error rates across student groups, keep an analysis log and a datasheet, and handle three stakeholder conversations: scoping, pushing back on an unsafe request and explaining limits. Deeper de-identification and fairness audits are in DS-309.

- **Audience:** Practitioners. Graduates and early-career analysts who have completed the FN courses or passed the placement test, and analysts moving into data science.
- **Prerequisites:** FN-106 Responsible Data and AI Practice in the Kingdom; Computes rates and a confidence interval for a proportion by group in SQL or a dataframe; Has written a short analytical report for a non-specialist reader
- **Case study:** Al-Qimam University, Student Success Unit: Al-Qimam University is a fictional public university with six colleges. Its Student Success Unit runs Awn, a rule that refers students to academic support from attendance and midterm marks, and its analyst is asked to evaluate the rule, publish tables, answer a government partner and serve three sponsors. All 18,000 student records are synthetic, generated with a fixed seed, and planted with the problems the labs find: identifiers in free-text notes, small cells that a subtraction recovers, attendance that is under-recorded for one group, marks that are missing for another, a gap that vanishes inside colleges, and a sharing request that asks for too much.

## Outcomes

- LO1 (Awareness): Explain the PDPL principles and the classification and sharing rules an analysis engages, from lawful basis to data subjects' rights and transfer, given five analysis requests from the case
- LO2 (Applied): Classify the datasets and outputs of an analysis and decide what may be shared, with whom and in what form, given the student records, a partner's sharing request and the classification policy
- LO3 (Applied): Apply aggregation and small-cell suppression to results tables and check that no student can be singled out, given draft tables by college, nationality and disability status
- LO4 (Applied): Analyse referral and error rates across student groups and report differences with their uncertainty and possible causes, given a support-referral rule and its results by group
- LO5 (Applied): Prepare a datasheet and an analysis log that let a reviewer trace each result to its data, decisions and approvals, given the case analysis and a template
- LO6 (Performance): Lead a stakeholder conversation that rescopes an unsafe or unclear request into a lawful, answerable question, and record the agreement, given a role-played sponsor asking for an individual-level risk list

## Day 1: Lawful analysis

Test the request, cut the data, classify it and decide what a partner may have

#### [day1#title] Lawful analysis

*SDAIA Academy · Responsible Data Practice and Conduct in Analytical Work*

Day 1: Test the request, cut the data, classify it and decide what a partner may have

Data Science Track · 3 teaching days + capstone day · 4 sessions · 4 labs · DS-207

#### [day1#agenda] Lawful analysis

*Today*

- **Session 1 · What the law asks of an analyst**: Name the rules a request engages, and know when to ask before touching data
- **Session 2 · Purpose, minimisation and secondary use**: The purpose decides the fields; a new purpose is a new decision
- **Session 3 · Classifying data and outputs**: Tables, charts and lists get a level, and the level sets the controls
- **Session 4 · Sharing requests**: Judge a partner's request, then answer with a form of release and conditions

#### [day1#the-case] One unit, one rule, one analyst and a week of requests

*The case*

- **Al-Qimam University**: a fictional public university, six colleges, 18,000 students
- **The Student Success Unit** runs **Awn**, a rule that refers students to academic support
- **You are Ohoud Al-Lihyani**, the unit's analyst
- Every record is synthetic, made with a fixed seed

| Who | Role |
| --- | --- |
| Jassim Al-Nuaimi | Director of the unit |
| Dr. Ibtisam Al-Khayyat | Vice-rector, a sponsor |
| Dr. Nabil Al-Faraj | Dean of engineering |
| Rami Al-Tuwaijri | Registrar, data owner |
| Shatha Al-Omair | Data protection officer |
| Hazza Al-Marri | Liaison of a government partner |

#### [day1#awn-rule] Awn refers a student on two signals

*The rule under study*

1. **Attendance** recorded rate below 75%
2. **or midterm mark** below 2.5 out of 5
3. **Referral** an advisor contacts the student

- **18,000** students this term
- **2,040** referred by Awn
- **2,191** ended the term struggling

#### [day1#setup-check] Prove your setup in two minutes

*Before the first lab*

- **Google Colab.** Open `00_setup_check.ipynb` from the course page and run every cell. The first cell clones the course repository.
- **Your laptop.** Clone the repository, then in `labs/` run `uv run jupyter lab` and open the same notebook.

> **What you need.** Python and pandas. No lab calls a model, needs a key or downloads anything beyond the repository.

#### [day1#from-fn106] The pre-work gave you the instruments; this course is about using them at a desk

*Where you start*

- **You know.** The PDPL's vocabulary, the four classification levels, the eight sharing principles, what a pseudonym does and does not hide.
- **You practise here.** Testing a request, cutting an extract, classifying outputs, releasing tables, comparing groups, documenting, saying no with an alternative.
- **Later, in DS-309.** Measured re-identification risk, differential privacy, synthetic data, fairness audits of models, model cards.

### Session 1: What the law asks of an analyst

#### [day1#s1] What the law asks of an analyst

*Session 1*

- Name the PDPL rules an analysis request engages, from lawful basis to transfer
- Distinguish analysis inside the collection purpose from a new purpose, a disclosure and a transfer
- Decide which requests go to the data protection officer before any data is touched

#### [day1#analysis-is-processing] Every step of an analysis is "processing" in the law

*The first idea*

- The PDPL's definition lists **collecting, storing, linking, using, disclosing, sharing, publishing and destroying**
- A query, a join, a chart and an email attachment are each on that list
- The **University is the controller**: it sets the purpose. You act for it
- So the question is never "is this analysis?" but **"which rules does this step engage?"**

- **At Al-Qimam.** Pulling 30 columns "to have a look" is collecting and storing. Joining the counselling register is linking. Sending a table to a dean is disclosing inside the controller; sending it to the Observatory is disclosing outside it.

#### [day1#four-kinds] Four kinds of request, four gates

*Sort the request first*

| The request is | The gate | In the case |
| --- | --- | --- |
| Inside the collection purpose | The purpose students were told | Does Awn reach struggling students? |
| A new internal purpose | Only the cases Article 10 lists | A dean wants names with counselling visits |
| A disclosure to another entity | Only the cases Article 15 lists | The Observatory wants records |
| A transfer outside the Kingdom | Article 29 and the transfer regulation | An upload to a notebook service abroad |

> **Method.** Name the kind before you argue about the data. The kind tells you which article to open.

#### [day1#lawful-basis] A university's analysis rarely rests on consent

*Lawful basis*

- Consent is the default, and Article 6 lists cases that need none
- **An agreement the student is party to**, or another law: enrolment, teaching, assessment, support
- **Legitimate interest** of the controller: never for sensitive data
- **Advertising** sent to a person needs prior consent, whatever else is true

> **What goes wrong.** "They agreed to the terms at registration" used as a basis for anything. The basis covers the purposes in the notice. A new purpose needs its own gate.

#### [day1#statistics-without-consent] Statistics without consent are allowed, on four duties

*The analyst's own article*

- **The law allows it when.** the data does not specifically identify the person, or the evidence of identity is destroyed before the data is disclosed (not for sensitive data), or another law or an agreement requires it.

1. State the purpose in the **record of processing**
2. Collect only the **minimum** the purpose needs
3. **Pseudonymise** wherever the purpose can still be met
4. Make sure the work has **no negative impact** on the people in the data

#### [day1#sensitive-data] Health data sits in three ordinary-looking columns

*Sensitive data*

| Column | Why it is health data |
| --- | --- |
| `disability_type` | A health condition, stated |
| `counselling_visits` | A health service received |
| `advisor_note` | Free text: surgery, treatment, a hearing aid |

- The PDPL's sensitive kinds include **health data**, ethnic origin, beliefs, criminal and biometric data
- Health data: access for the **fewest staff** who need it to provide the service
- Legitimate interest never covers it
- A **registered or none** flag is still health data

#### [day1#rights-and-retention] A student can ask what you hold, and the extract has an end date

*Rights and retention*

- **Rights:** to be informed, to access, to get a copy, to correct, to have data destroyed when no longer needed
- The University answers within **30 days**
- **Retention:** destroy personal data when the purpose is met; data that no longer identifies anyone may be kept

- **What this means at your desk.** Know where every copy of an extract is. Give each extract a destruction date in the log. Keep the pseudonym key in the unit, so a student's rows can be found for an access request and nowhere else.

#### [day1#disclosure-transfer-breach] Three words that are not synonyms: disclosure, transfer, breach

*When data leaves*

- **Disclosure.** Someone outside the controller gets access. Allowed only in listed cases, such as a public entity asking for a public-interest purpose.
- **Transfer.** The data is processed outside the Kingdom. Needs an adequate level of protection or approved safeguards, and the minimum data.
- **Breach.** Access nobody allowed: a lost laptop, a file sent to the wrong list. The University notifies the authority within 72 hours where harm is expected.

> **Your part in a breach.** Tell the data protection officer at once. The 72 hours run from when the University knows, and you are the University.

#### [day1#ask-the-dpo] The analyst prepares the decision; the data protection officer owns the hard ones

*Who decides*

- She monitors how the law is applied and supervises impact assessments
- She receives data subjects' requests and reports breaches
- She keeps the **record of processing** up to date

- **Rule of thumb.** Inside the collection purpose: proceed, minimise, record. Anything else (a new purpose, sensitive data, a disclosure, a transfer, advertising): to her **before** any data is touched, with your note attached.

#### [day1#check-kind-of-request] Which gate does this request pass through?

*Checkpoint*

**Question:** The alumni office asks the analyst for the grade averages of last year's graduates, to invite the top tenth to a paid executive programme run with a private partner. Which rule decides the answer?

- A. Purpose limitation is satisfied, because the data stays inside the University
- B. The sensitive-data rule, because grades are sensitive data
- C. Purpose limitation and marketing consent: a new purpose that is advertising
- D. The disclosure rule, because the alumni office is another entity

#### [day1#lab-1-1] Five requests, which rules

Lab 1.1 · 25 min

Map five requests to the PDPL principles they engage, and write the note that says so for one of them.

[D1_1_five_requests.ipynb](https://sdaiaacademy.github.io/ds-207/labs/D1_1_five_requests.ipynb)

- [ ] Read the five requests and the privacy notice (4 min)
- [ ] Name the kind of processing each request is (5 min)
- [ ] Mark the rules each request engages (8 min)
- [ ] Flag the requests that go to the data protection officer (3 min)
- [ ] Write the note for one request (5 min)
- [ ] ✱ Stretch: Add a sixth request: a student asks for a copy of her data used in the analysis

### Session 2: Purpose, minimisation and secondary use

#### [day1#s2] Purpose, minimisation and secondary use

*Session 2*

- Write a purpose precise enough to decide each field against
- Cut an extract to the fields the purpose needs, keeping, coarsening or dropping each with a reason
- Recognise a secondary use and name what the law and the national rules require before it starts

#### [day1#purpose-sentence] A purpose is precise enough when it can reject a column

*Purpose*

- **Too loose to decide anything.** "Understand student success." Every one of the 30 columns might help with that.
- **Precise enough to cut with.** "Evaluate whether Awn's referrals in term 1 reached the students who ended the term struggling, by college and level, to decide whether to extend the rule."

- It names the **decision**, the **population**, the **measure** and the **breakdown**
- The law: collect for purposes directly related to the controller's own, and process only for those

#### [day1#keep-coarsen-drop] Every field gets one of three verdicts

*Minimisation*

- **Keep.** The purpose needs it as it is: the rule's inputs, its output, the outcome, the breakdown.
- **Coarsen.** The purpose needs a rougher form: a band for a date, a flag for a grade, a pseudonym for a student number.
- **Drop.** The purpose does not need it. "It might be useful" is not a need.

> **The legal test.** Content limited to the minimum necessary for the purpose, and nothing that identifies a person once the purpose is achieved.

#### [day1#thirty-to-eight] The Awn evaluation needs 8 of the registry's 30 columns

*From the lab's run*

| Item | Value |
| --- | --- |
| Dropped | 22 |
| Kept | 7 |
| Coarsened | 1 |

- **Kept:** college, level, admission route, attendance, midterm mark, referral, outcome
- **Coarsened:** the student number, into a project pseudonym
- **Dropped:** names, identity numbers, contacts, addresses, bank accounts, health fields, notes, and the exact term grade

#### [day1#free-text] Pattern rules find the identifiers that have a shape, and miss the rest

*Personal data detection*

| In 2,400 advisor notes | Notes | Found by a pattern? |
| --- | --- | --- |
| A mobile number | 180 | Yes |
| An identity number | 70 | Yes |
| A health remark | 210 | No |
| Another student's name | 80 | No |

```python
re.search(r"\b05\d{8}\b", note)     # phone
re.search(r"\b[12]\d{9}\b", note)   # identity
```

> **So.** A free-text column is dropped whole, not cleaned. Detection tools (regular expressions, Presidio) lower the risk; they do not certify a text.

#### [day1#pseudonym-is-personal] "Anonymised" has a legal meaning, and your extract does not meet it

*A word used loosely*

- **Pseudonymised.** Identifiers replaced by a code. Someone holds the key, and each row is still one student. **Still personal data.** Every rule still applies.
- **Anonymised.** Re-identification is **impossible**, the controller has assessed that, and keeps assessing it as methods change. Only then is it no longer personal data.

> **At your desk.** Say "pseudonymised extract". Use a keyed hash with a key for this project only, so two extracts cannot be joined.

#### [day1#secondary-use] A new purpose for old data is a new decision

*Secondary use*

- **Secondary use:** using data for a purpose other than the one it was collected for
- The PDPL allows it only in listed cases: consent, a public entity acting in the public interest, data that no longer identifies anyone, and a few more
- The **General Rules for Secondary Use of Data** govern requests between entities for the public interest or for research

- **What the Rules ask of an applicant.** A legitimate purpose that is not profit-seeking. Only the minimum data for it. A request to the entity that is the source of the data, or proof of its approval. A rejection must give its reasons.

#### [day1#minimisation-log] The cut is a decision, so it leaves a log

*Recording why*

| Field | Decision | Reason |
| --- | --- | --- |
| `student_id` | coarsen | A project pseudonym keeps one row per student without the registry number |
| `admission_route` | keep | Bridging-year entrants have no midterm mark; needed to read the rule's result |
| `term_gpa` | drop | The outcome flag already says struggled or not |
| `advisor_note` | drop | Free text: cannot be checked field by field |

> **Who reads it.** The data owner who approves the extract, the reviewer who audits it, and you, six months later.

#### [day1#check-minimise] Which extract fits the purpose?

*Checkpoint*

**Question:** Purpose: "report the share of first-year students who end the term struggling, by college". Which extract is the minimum that serves it?

- A. A pseudonym, the college, the level and the outcome flag, for first-year students
- B. The same, plus the student number and email in case a college wants to follow up
- C. The college, the level, the exact term grade and the date of birth
- D. The college, the level and the outcome flag for all 18,000 students, filtered later

#### [day1#lab-1-2] Cut the extract

Lab 1.2 · 25 min

Cut an extract to the fields the purpose needs, recording why, and find the identifiers hiding in free text.

[D1_2_cut_extract.ipynb](https://sdaiaacademy.github.io/ds-207/labs/D1_2_cut_extract.ipynb)

- [ ] Read the purpose and the 30 columns of the registry (3 min)
- [ ] Decide keep, coarsen or drop for each field, with a reason (8 min)
- [ ] Scan the advisor notes for identifiers with rules (5 min)
- [ ] Build the extract with a project pseudonym (6 min)
- [ ] Write the minimisation log (3 min)
- [ ] ✱ Stretch: Decide the fields again for a second purpose, the partner's study, and say what makes it a secondary use

### Session 3: Classifying data and outputs

#### [day1#s3] Classifying data and outputs

*Session 3*

- Classify a dataset or an output with the impact questions of the Data Classification Policy
- Apply the highest-level rule to combined data and say when an aggregate can be Public
- Name the control each level requires, including what may be entered into an AI tool

#### [day1#outputs-are-data] A table, a chart and a list are data, and each needs a level

*The idea of this session*

- The policy covers all data a public entity **receives, produces or manages**, in any form
- An output does **not inherit** the level of its source
- Classify **when you create it**: until someone does, it is treated as Restricted

- **In the Awn evaluation.** One Restricted registry produces a Restricted extract, a Restricted worklist, a Restricted draft table and, after approval, a Public table of referral rates by college.

#### [day1#four-levels-recap] The level follows the impact of disclosure

*Recap from the pre-work*

| Level | Impact | What it looks like at a university |
| --- | --- | --- |
| Top Secret | High | Not in a student-success unit |
| Secret | Medium | Not in a student-success unit |
| Restricted | Low | Student records, the extract, a named worklist, a draft with small cells |
| Public | None | The timetable, a released table of rates by college |

> **Why not Secret?** The policy rates the disclosure of an individual's personal information as a low impact. Low impact leads to Restricted or Public.

#### [day1#low-impact-route] Low impact needs two more questions

*Restricted or Public?*

1. **Impact is low** harm to individuals is limited and short-term
2. **Would disclosure conflict with a law?** Yes: Restricted
3. **Do the benefits of openness outweigh the harm?** Yes: Public. No: Restricted

- **The extract.** Rows about single students. Disclosure would break the PDPL. Restricted at the first question.
- **Rates by college.** Nobody is identified, no law is broken, publishing helps students and the public. Public.

#### [day1#highest-level] A joined file takes the highest level of its parts

*Combined data*

1. **Timetable** Public
2. **joined to the registry** Restricted
3. **Attendance by time of day, per student** Restricted

- The policy's fourth principle: the **highest level of protection** for an integrated dataset
- The reverse also happens: an **aggregate** of Restricted rows can be Public
- So the level is set for each output, by what that output would reveal

#### [day1#controls-by-level] The level tells you how to mark, open, store, send and end the data

*Controls*

| Control | Restricted item | Public item |
| --- | --- | --- |
| Protective marking | Marked on the file and in the email | None needed |
| Access | Need to know, least privilege | Open |
| Storage | Not left unattended; encrypted | Anywhere |
| Sharing | An agreed secure channel | Any channel |
| Retention and disposal | On the schedule, disposal logged | On the schedule |
| Before release | Second-person check, owner's approval | Done |

#### [day1#ai-tools] Only Public data goes into a generative AI tool

*What may go into AI tools*

**Analyst:** Here are 200 rows of the extract. Summarise the patterns by college.

**Hosted assistant (weak example):** Happy to help. I have stored your file...

- Government employees enter **nothing classified Restricted or higher**, and nothing unclassified
- A pseudonymised extract is Restricted: **no**
- A released table of rates: **yes**
- Asking for **code** without pasting data: yes

#### [day1#who-classifies] You propose a level; the data owner classifies; a reviewer checks

*Roles and time*

1. **Analyst** proposes a level and controls for each output
2. **Data owner** (the registrar) classifies
3. **Reviewer** in the data management office checks within a month

> **Levels change.** Set the trigger when you classify: "Restricted until the release is approved", "Public from the publication date". Record it in the register.

#### [day1#check-classify-output] What level is this output today?

*Checkpoint*

**Question:** You compute a table of registered-disability counts by college and nationality group from the pseudonymised extract. Two cells are under 10 and one is 1. Nobody has reviewed it. What is its level now?

- A. Public, because it is an aggregate with no names
- B. Restricted, because every output of a Restricted source stays Restricted
- C. Secret, because it contains health data
- D. Restricted, because a cell of 1 can single out a student, until it is suppressed and checked

#### [day1#lab-1-3] Classify and control

Lab 1.3 · 25 min

Classify four datasets and three outputs and name each control.

[D1_3_classify_control.ipynb](https://sdaiaacademy.github.io/ds-207/labs/D1_3_classify_control.ipynb)

- [ ] Run the impact questions on the four datasets (7 min)
- [ ] Classify the three outputs (6 min)
- [ ] Apply the highest-level rule to a joined file (3 min)
- [ ] Name the controls for each item (6 min)
- [ ] Decide what may be entered into an AI tool (3 min)
- [ ] ✱ Stretch: Set a declassification trigger for the referral table and say who approves it

### Session 4: Sharing requests

#### [day1#s4] Sharing requests

*Session 4*

- Assess a sharing request against the tests of the Data Sharing Policy and the rules for secondary use
- Choose the form of release: record level, pseudonymised or aggregate
- Draft approval conditions under the policy's control headings and name who signs

#### [day1#sharing-is-expected] The policy expects you to share, and tells you how

*The starting point*

- Its first principle is a **data sharing culture**: entities share what they produce
- The other seven principles are the conditions: legitimate purpose, authorised access, transparency, accountability, security, ethical use, one source of truth
- For personal data the **PDPL's disclosure cases** apply on top

- **The analyst's part.** You will be the person who knows what the data contains. You prepare the assessment and the conditions. The data management office decides, with the data protection officer.

#### [day1#parties-and-route] A request has three roles and one front door

*Parties and route*

| Role | In the case |
| --- | --- |
| Data requester | Masarat Labour Market Observatory |
| Data sharing entity | Al-Qimam University |
| Data source entity | The University for marks; another entity for identity numbers |

- The front door is the **data management office**, never an analyst's inbox
- Requests for analytical purposes go to the **National Data Bank** first
- Between government entities: the **controls template**. With a private entity: a **data sharing agreement**

#### [day1#three-tests] Three tests decide whether sharing can go ahead

*The assessment*

- **1 · Legitimate purpose.** A legal basis or a justified operational need. For the Observatory: its mandate, a public-interest purpose. **Met.**
- **2 · Minimum data.** Only what the purpose needs. It asked for 11 fields of all 18,000 students. **Not met.**
- **3 · The source's consent.** Needed for fields the University is not the source of. **Met with conditions.**

> **Time.** The office assesses within 10 business days and gives its reasons in writing. A rejected request may be corrected and sent again.

#### [day1#form-of-release] Choose the least revealing form that still serves the purpose

*In what form*

| Form | What leaves | Serves a linkage study? |
| --- | --- | --- |
| Aggregate | Counts and averages by programme | No |
| Pseudonymised | Rows under a code only the University can reverse | No |
| Record level, minimised | Rows with the identity number and the few fields needed | Yes |

- **11 × 18,000** fields and students asked for
- **5 × 3,612** offered: final-year students, five fields

#### [day1#eight-headings] Eight headings turn "yes, but" into something signable

*The conditions*

1. **Legal basis:** the purpose, and no other use
2. **Authorisation:** named people, need to know
3. **Data type:** the fields, the format, the detail
4. **Pre-processing:** masking, aggregation before or after

5. **Sharing means:** the channel; retention and destruction
6. **Usage and protection:** the level, limits, onward use
7. **Duration and termination:** end date, what happens then
8. **Liability:** who answers for what

> **Read the request for its weak points.** "By email", "and its contractors", "a consulting firm", "kept for future studies": each one becomes a condition.

#### [day1#who-signs] The level of the data decides who signs

*The decision record*

| Level of the shared data | Who signs for the sharing entity |
| --- | --- |
| Secret, Top Secret | The head of the entity or a delegate |
| Restricted | The director of the data management office |
| Public | No assessment or agreement needed |

- The record names the decision, the level, the signatory and who was consulted
- It goes into the **record of processing** and the office's log of requests
- Sharing records are kept for **five years** after the request ends

#### [day1#a-fact-changes] Change one fact and the decision changes with it

*Decisions move*

| If the request changed to | What now applies |
| --- | --- |
| A private company as requester | A data sharing agreement, a licence under the secondary-use rules, no profit-seeking purpose, and a different PDPL disclosure case |
| Analysts outside the Kingdom | The transfer rules: adequate protection or approved safeguards |
| Disability status added | Sensitive data: the narrowest reading of every test |
| Aggregates only | Small-cell rules, and perhaps a Public table |

> **In the capstone.** The assessor changes one fact of your partner's request and you revise the decision aloud.

#### [day1#check-sharing] What is the right first answer to this request?

*Checkpoint*

**Question:** A government health authority emails the analyst: "For a wellbeing study, send names and counselling visit counts of all students." What comes first?

- A. Send it: a public entity asked, for the public interest
- B. Forward it to the data management office and the data protection officer, with your assessment
- C. Refuse: counselling data is health data and is never shared
- D. Send pseudonymised rows instead, which removes the names

#### [day1#lab-1-4] The Observatory's request

Lab 1.4 · 25 min

Assess a partner's sharing request and draft the approval conditions.

[D1_4_sharing_request.ipynb](https://sdaiaacademy.github.io/ds-207/labs/D1_4_sharing_request.ipynb)

- [ ] Read the request and name the parties and the route (4 min)
- [ ] Assess it against the three tests (6 min)
- [ ] Choose the form of release (5 min)
- [ ] Draft the conditions under the eight control headings (7 min)
- [ ] Fill the decision record and name who signs (3 min)
- [ ] ✱ Stretch: The partner adds a consultant outside the Kingdom: revise the decision

#### [day1#wrap-up] Three things to keep

*Day 1*

- **Name the kind first.** Inside the purpose, a new purpose, a disclosure, a transfer. The kind tells you which rule to open and who decides.
- **The purpose cuts the data.** Keep, coarsen or drop, with a reason in a log. Thirty columns became eight.
- **Outputs get a level and requests get conditions.** Classify what you produce. Answer a partner with a form of release and eight conditions.

#### [day1#next] Day 2: fair and safe outputs

*Tomorrow*

A table that looks harmless and points at one student. A rule that looks neutral and is wrong more often for two groups.

- Bring: your setup, working
- Recall: a confidence interval for a proportion

## Day 2: Fair and safe outputs

Release tables that single nobody out, and compare groups with honest uncertainty

#### [day2#title] Fair and safe outputs

*SDAIA Academy · Responsible Data Practice and Conduct in Analytical Work*

Day 2: Release tables that single nobody out, and compare groups with honest uncertainty

Data Science Track · 3 teaching days + capstone day · 4 sessions · 4 labs · DS-207

#### [day2#agenda] Fair and safe outputs

*Today*

- **Session 1 · Aggregate release and small cells**: An aggregate table can still point at one student
- **Session 2 · Where bias enters**: Bias enters in recording, coverage, labels and use, before any metric
- **Session 3 · Comparing groups**: Referral and error rates by group, each with its interval
- **Session 4 · Naming the bias**: Two candidate bias types for a gap, and the check that separates them

#### [day2#review-day1] Which statement about the pseudonymised extract is right?

*Review of Day 1*

**Question:** The analysis extract has 13 columns per student under a project pseudonym, with no names or identity numbers. A colleague wants to paste 500 rows into a hosted AI assistant to get plotting code.

- A. Fine: without names the rows are anonymous
- B. Not allowed: the extract is personal data classified Restricted; describe the columns and ask for code
- C. Fine if the assistant's history is switched off
- D. Not allowed: student data is classified Secret

#### [day2#approved-extract] The group comparison is a separate decision, already approved and logged

*Where today starts*

- Yesterday's extract dropped gender, nationality and disability status: its purpose did not need them
- Checking the rule's errors by group **does** need them
- Disability status is health data, so the data protection officer decided

- **Log entry L002, approved by Shatha Al-Omair.** Gender, nationality group, disability status and remote accommodation are added to the extract for the group comparison. It runs only on the pseudonymised extract inside the unit and is reported in aggregate.

### Session 1: Aggregate release and small cells

#### [day2#s1] Aggregate release and small cells

*Session 1*

- Explain how a small cell, a total or a second release singles out a student
- Apply a threshold rule with complementary suppression and log each suppressed cell
- Test a release for recovery by subtraction and by differencing before it leaves

#### [day2#aggregates-disclose] An aggregate table can point at one student in three ways

*The idea of this session*

- **A small cell.** A count of 1 in "Computing, non-Saudi, registered disability" is a person, to anyone who knows that college.
- **A total.** Hide the 1 and print the row total: the reader subtracts and has it back.
- **A second table.** Two tables that each look safe differ by exactly the students one of them leaves out.

> **Singling out** means a reader can tell that a cell is one particular person, and so learns what the table says about that person.

#### [day2#threshold-rule] A threshold rule: no count from 1 to 9 leaves the unit

*The rule*

- The unit's release policy sets **10**. It is the University's own choice
- **No national instrument sets a number.** The national guideline requires that aggregated data cannot be used to identify a person
- Practice elsewhere: 3 as an absolute floor, 5 or 10 as common minimums

- **Choosing a threshold.** Higher when the attribute is sensitive (health), when the population is small and people know each other (a college), and when more tables on the same population will follow.

#### [day2#draft-table] The draft: students with a registered disability, by college and nationality group

*From the lab's run*

| College | Saudi | non-Saudi | Total |
| --- | --- | --- | --- |
| Arts and Humanities | 65 | 8 | 73 |
| Business | 92 | 8 | 100 |
| Computing | 54 | 1 | 55 |
| Engineering | 81 | 12 | 93 |
| Health Sciences | 51 | 3 | 54 |
| Science | 50 | 4 | 54 |

**5** cells from 1 to 9

> **One student.** The cell of 1 states a health fact about a person a whole college can name.

#### [day2#subtraction-attack] Suppress the small cells, keep the totals, and all five come back

*Attack one*

| College | Saudi | non-Saudi | Total |
| --- | --- | --- | --- |
| Arts and Humanities | 65 | c | 73 |
| Business | 92 | c | 100 |
| Computing | 54 | c | 55 |
| Engineering | 81 | 12 | 93 |
| Health Sciences | 51 | c | 54 |
| Science | 50 | c | 54 |

```python
55 - 54   # Computing, non-Saudi: 1
54 - 51   # Health Sciences: 3
```

> **What changed.** How the table looks. Not what it reveals.

#### [day2#complementary] Complementary suppression protects the cell and can eat the table

*The repair, and its price*

- Where one hidden cell can be subtracted back, hide a **second** cell in the same row and column
- Repeat until no row or column has exactly one hidden cell
- In the draft: **10 of 12 cells** end up hidden, including counts of 50 to 92 nobody needed to hide

- **Redesign beats repair.** Two one-way tables: by college (54 to 100) and by nationality group (393 and 36). Every cell is 10 or more, no suppression, and almost the same message.

#### [day2#differencing] Two safe tables can differ by one student

*Attack two*

| Registered disability | Published last month, all | Asked for now, Saudi only | Difference |
| --- | --- | --- | --- |
| Arts and Humanities | 73 | 65 | 8 |
| Business | 100 | 92 | 8 |
| Computing | 55 | 54 | 1 |
| Health Sciences | 54 | 51 | 3 |
| Science | 54 | 50 | 4 |

- Each table passes the threshold alone: every count is 50 or more
- The difference is the group the second table left out
- **The check:** before a release, compare it with every earlier table on the same population

#### [day2#other-methods] Suppression is one of four tools

*Beyond suppression*

| Method | What it does | What the reader loses |
| --- | --- | --- |
| Coarsen the categories | Merge colleges, or nationalities into two groups | Detail; usually the cheapest loss |
| Suppress | Hide small cells and their complements | Cells, sometimes most of them |
| Round or band | Counts to a base of 5; "fewer than 10" | Exactness of every cell |
| Perturb | Small random changes to counts | Trust that a number is the number |

> **Later.** Noise with a mathematical guarantee (differential privacy) and measured re-identification risk are in DS-309.

#### [day2#zeros-and-hundreds] A cell of zero or of everyone can disclose too

*Not only small counts*

- **Everyone in a group.** "All 14 students of programme X were referred." No small cell, and you now know the referral status of each of the 14.
- **Nobody in a group.** "0 of 14 were not referred" is the same sentence. A zero that tells you about everyone else is not harmless.

- Check **rates of 0% and 100%** in small groups as well as counts
- The unit's rule covers counts of 1 to 9; this case needs your judgement and a line in the log

#### [day2#suppression-log] Every suppressed cell has a line in the log, and every release a line in the register

*The evidence*

| Table | Row | Column | Kind | Reason |
| --- | --- | --- | --- | --- |
| T3 | Computing | non-Saudi | primary | count of 1 to 9 |
| T3 | Computing | Saudi | complementary | protects a suppressed cell from subtraction |
| Saudi-only by college | all | all | not released | differencing against the release of 2026-10 reveals counts of 1 to 9 |

> **Second person.** The unit's policy: a table with a suppressed cell is checked by someone who did not make it, before it is proposed as Public.

#### [day2#check-small-cells] Is this table ready for release?

*Checkpoint*

**Question:** A table of referred students by college and level has one cell of 4. The analyst replaces it with "c" and keeps the row and column totals. The threshold is 10. What is the state of the table?

- A. Ready: the only small cell is suppressed
- B. Not ready: all totals must be removed from every table
- C. Ready, provided the cell is shown as "fewer than 10"
- D. Not ready: the 4 is recovered from its row total until a second cell in that row and column is suppressed

#### [day2#lab-2-1] Suppress, then attack

Lab 2.1 · 25 min

Apply a threshold rule and test for singling out by differencing.

[D2_1_small_cells.ipynb](https://sdaiaacademy.github.io/ds-207/labs/D2_1_small_cells.ipynb)

- [ ] Count the cells under the threshold in three draft tables (4 min)
- [ ] Suppress them and log each cell with its reason (6 min)
- [ ] Recover a suppressed cell from the totals (4 min)
- [ ] Add complementary suppression and test again (6 min)
- [ ] Difference the table against an earlier release (5 min)
- [ ] ✱ Stretch: Round the counts to a base of 5 in place of suppression and compare what a reader loses

### Session 2: Where bias enters

#### [day2#s2] Where bias enters

*Session 2*

- Trace a rule's data from the event to the decision and mark where bias can enter
- Distinguish a recording problem, a coverage problem, a label problem and a use problem
- Measure one entry point with data instead of arguing about it

#### [day2#bias-is-systematic] Bias is a systematic error that falls on some groups more than others

*A working definition*

- It needs **no intent**: a process that records or covers people unequally is enough
- It is **not noise**: more data of the same kind does not remove it
- It enters **before** any metric is computed

- **The national frame.** Fairness is the first of SDAIA's AI Ethics Principles: act to eliminate bias in the data, the design and the use of a system. The AI Bias Reference Guide names more than a hundred types, with how each arises and how to mitigate it.

#### [day2#six-stages] Awn's data passes six stages, and each is an entry point

*Walk the path*

- **1 · Recording.** A card read at the door of a teaching room
- **2 · Marks.** Midterm marks entered in the registry
- **3 · Thresholds.** 75% and 2.5, set in 2023 on two colleges
- **4 · Outcome label.** "Struggled": a term average below 2.5
- **5 · Use.** An advisor contacts the referred student
- **6 · Reporting.** One rate for the whole University

> **The question at each stage.** For whom could this step go wrong more often than for others?

#### [day2#recording-gap] The card record is 17 points too low for students who attend remotely

*Entry point 1, measured*

| Item | Value |
| --- | --- |
| Remote accommodation | 16.8 points |
| Other students | -0.1 points |

- Roll call minus card record, from an audit of 1,600 students
- Of 300 students with a remote accommodation, **191** are below the 75% limit on the card record
- On the roll call, **14** are

#### [day2#coverage-gap] Over a third of non-Saudi students have no midterm mark in the registry

*Entry point 2, measured*

| Item | Value |
| --- | --- |
| Non-Saudi students | 36.2% |
| Saudi students | 3.4% |

- 1,244 students have no mark; **every one** is a bridging-year entrant
- Their marks are in the bridging programme's own system
- For them, half of the rule cannot fire

> **Where you see it is not where it comes from.** The effect appears under nationality; the cause is the admission route.

#### [day2#thresholds-and-labels] Thresholds carry their history, and labels carry a definition

*Entry points 3 and 4*

- **Thresholds from 2023, two colleges.** A limit tuned on Business and Engineering may not fit Health Sciences, where one student in five ends the term struggling. Past conditions built into today's rule: the guide's historical bias.
- **"Struggled" is a choice.** A term average below 2.5. A student who withdraws after two courses keeps a good average and counts as "ok". Change the label and every error rate changes with it.

> **What goes wrong.** Treating the outcome column as the truth. It is one more measurement, with its own blind spots.

#### [day2#use-and-feedback] What happens after the referral changes what the data says about it

*Entry points 5 and 6*

- **Support that works hides itself.** A referred student who is helped and passes counts as a referral that was "not needed"
- **Take-up differs.** Who answers an advisor's call, who can come during working hours?
- **One number for everyone** hides a rule that fails a small group

- **The loop.** If next year's thresholds are tuned on this year's outcomes, colleges with good advisors will look as if they need fewer referrals. The guide's feedback loop bias.

#### [day2#measure-not-argue] An entry point is a hypothesis until someone measures it

*Method*

- **An opinion.** "Attendance data is probably unfair to some students." Nobody can act on it, and nobody can refute it.
- **A measurement.** "For 300 students with a remote accommodation the record is 17 points below the roll call; 191 fall under the limit on paper, 14 in fact." A size, a group, a consequence.

- The audit sampled **all 300** students of the small group and 1,300 others at random: a small group needs all its members to be measured at all

#### [day2#check-entry-point] Where did the bias enter?

*Checkpoint*

**Question:** A library fines late returns. Evening students are fined twice as often. A return is logged when staff scan the book; the desk closes before evening classes end, and the drop box is scanned the next morning. Where does the gap come from?

- A. Recording: the return time is logged later than the true return for one group
- B. Outcome: evening students return books later
- C. Thresholds: the loan period is too short for evening students
- D. Reporting: the fine rate is reported for all students together

#### [day2#lab-2-2] Four entry points

Lab 2.2 · 25 min

Mark four points where bias can enter the referral data, and measure two of them.

[D2_2_bias_entry_points.ipynb](https://sdaiaacademy.github.io/ds-207/labs/D2_2_bias_entry_points.ipynb)

- [ ] Trace Awn's data from the event to the referral (5 min)
- [ ] Mark four points where bias can enter (8 min)
- [ ] Measure the attendance record against the roll-call audit (6 min)
- [ ] Measure missing midterm marks by group (4 min)
- [ ] Rank which entry point to check first (2 min)
- [ ] ✱ Stretch: Find a fifth entry point after the referral: who takes up the support that is offered

### Session 3: Comparing groups

#### [day2#s3] Comparing groups

*Session 3*

- Compute referral, false-referral and missed-student rates by group
- Report each rate and each difference with a confidence interval
- Check whether a gap survives inside colleges before explaining it

#### [day2#three-rates] One rule, four outcomes, three rates

*What to compare*

|  | Struggled | Did not struggle |
| --- | --- | --- |
| **Referred** | caught: 1,209 | false referral: 831 |
| **Not referred** | missed: 982 | left alone: 14,978 |

- **Referral rate** = referred / all = 11.3%
- **False-referral rate** = false referrals / did not struggle = 5.3%
- **Missed rate** = missed / struggled = 44.8%

> **Not "accuracy".** Awn is right for 90% of students, and misses 45% of those it exists for.

#### [day2#two-errors] The two errors hurt different students in different ways

*Why two error rates*

- **A false referral.** A student who was fine is contacted, labelled "at risk" in a system, and takes an advisor's hour from someone else. Mild once; not mild if the label travels.
- **A miss.** A student who is struggling hears from nobody. The rule existed for this student.

- A group can be worse off in **one** error and not the other, so one combined number hides it
- The ethics principles ask that metrics be chosen by the **effect of the decision** and the harm of each kind of error

#### [day2#intervals] A rate without its interval hides how many students it rests on

*Uncertainty*

| Missed rate | Struggling students | Rate (95% interval) |
| --- | --- | --- |
| Saudi | 1,971 | 42.9% (40.8 to 45.1) |
| non-Saudi | 220 | 61.8% (55.2 to 68.0) |
| Registered disability | 61 | 13.1% (6.8 to 23.8) |

- The **denominator** of a missed rate is the struggling students of the group, not the group
- Use the **Wilson interval**: it behaves for small counts and rates near 0 or 1
- For a difference, an interval on the difference itself

#### [day2#rate-table] Two groups stand out, in two different errors

*From the lab's run*

| Group | Students | Referral rate | False-referral rate | Missed rate |
| --- | --- | --- | --- | --- |
| Women | 8,218 | 12.3% | 5.5% | 43.2% |
| Men | 9,782 | 10.5% | 5.1% | 46.4% |
| Saudi | 16,063 | 11.8% | 5.4% | 42.9% |
| non-Saudi | 1,937 | 7.8% | 3.9% | 61.8% |
| No registered disability | 17,571 | 10.6% | 4.6% | 45.7% |
| Registered disability | 429 | 41.7% | 34.2% | 13.1% |

#### [day2#gaps-with-intervals] Report every comparison you made, with its interval

*Differences*

| Comparison | Rate | Difference | 95% interval | Reading |
| --- | --- | --- | --- | --- |
| Registered disability minus none | false referral | +29.7 points | +25.0 to +34.7 | clear |
| non-Saudi minus Saudi | missed | +18.9 points | +12.0 to +25.4 | clear |
| Women minus men | referral | +1.9 points | +0.9 to +2.8 | clear, see next slide |
| First generation minus not | missed | +1.1 points | -3.3 to +5.6 | could be zero |
| First generation minus not | false referral | +0.6 points | -0.2 to +1.4 | could be zero |

> **The two rows at the bottom belong in the report.** Leaving out comparisons that found nothing makes the others look selected.

#### [day2#gap-inside-colleges] The gender gap vanishes inside every college

*Before explaining a gap*

| College | Share of women | Referral rate | Women minus men (95% interval) |
| --- | --- | --- | --- |
| Health Sciences | 76% | 20.0% | -1.2 points (-5.1 to +2.5) |
| Science | 59% | 14.4% | -1.1 points (-3.9 to +1.6) |
| Arts and Humanities | 50% | 10.6% | +0.3 points (-1.9 to +2.5) |
| Business | 39% | 7.8% | -0.8 points (-2.5 to +1.0) |
| Computing | 37% | 9.0% | 0.0 points (-2.3 to +2.4) |
| Engineering | 25% | 9.2% | -0.3 points (-2.3 to +2.0) |

> **Overall: +1.9 points.** Women study more often in the colleges where everyone is referred more. The rule treats women and men in the same college alike.

#### [day2#tools-for-groups] A library computes the rates; you choose the comparisons

*Tools*

```python
g = df.groupby("nationality_group")
missed = g.apply(lambda d:
    (~d.referred & d.struggled).sum()
    / d.struggled.sum())
```

- **Grouped metrics in pandas or SQL:** a group-by and three ratios
- **A fairness library** (Fairlearn's `MetricFrame`): the same table in one call, for many metrics
- Neither chooses the groups, the strata, the intervals or the question

> **Small groups twice.** A rate on 8 students is too uncertain to interpret and too small to publish. Both rules apply.

#### [day2#check-compare] What can the analyst claim?

*Checkpoint*

**Question:** Awn missed 8 of 61 struggling students with a registered disability (13%, interval 7% to 24%) and 974 of 2,130 others (46%, interval 44% to 48%). Which sentence is supported?

- A. The rule works better for students with a registered disability
- B. Nothing can be said: 61 students are too few
- C. Fewer of this group were missed, by an uncertain margin; read the false-referral rate beside it
- D. The rule is biased in favour of students with a registered disability

#### [day2#lab-2-3] Rates with intervals

Lab 2.3 · 25 min

Compare referral and error rates by group with intervals.

[D2_3_group_rates.ipynb](https://sdaiaacademy.github.io/ds-207/labs/D2_3_group_rates.ipynb)

- [ ] Build the four outcome counts by group (5 min)
- [ ] Compute the three rates with Wilson intervals (8 min)
- [ ] Compute the differences with their intervals (5 min)
- [ ] Check the gender gap inside each college (5 min)
- [ ] Write the result in one sentence per gap (2 min)
- [ ] ✱ Stretch: Compute the rates for one intersection of two groups and say what the interval allows you to claim

### Session 4: Naming the bias

#### [day2#s4] Naming the bias

*Session 4*

- Match an observed gap to candidate bias types in the AI Bias Reference Guide
- Design the check that separates two candidate causes
- State what a fairness metric cannot settle and who decides the rest

#### [day2#gap-is-not-cause] A gap is an observation; a bias type is an explanation

*The idea of this session*

1. **1 · Observe** a gap with its interval
2. **2 · Name two candidates** that would need different fixes
3. **3 · Design a check** on which they disagree
4. **4 · Run it** and say what stays open

> **What goes wrong.** Naming the first bias type that fits and stopping. One gap usually fits several names, and each name points to a different repair.

#### [day2#the-guide] The AI Bias Reference Guide gives each type a definition, an example and a mitigation

*The national reference*

| Type | In one line (our wording) |
| --- | --- |
| Measurement bias | Recorded values are systematically too high or too low |
| Coverage bias | The data does not adequately represent part of the population |
| Aggregation bias | Groups that differ are combined; the result fits the largest |
| Historical bias | Past assumptions or conditions no longer fit the present |
| Feedback loop bias | Outputs return as inputs and magnify an early skew |
| Automation bias | People favour a system's output over other evidence |

#### [day2#gap-a-candidates] Is the record wrong, or does one limit not fit?

*Gap A · false referrals, registered disability*

- **Measurement bias.** Attendance is **recorded** too low for these students. Prediction: the record is far below the roll call, and the gap is confined to students with a remote accommodation. Fix the record.
- **Aggregation bias.** Attendance is recorded correctly and one limit of 75% does not fit this group. Prediction: record matches roll call, and the gap covers all students with a registered disability. Fix the rule.

> **The check.** Roll call against record, and the false-referral rate with and without a remote accommodation.

#### [day2#gap-a-result] The gap is confined to students whose attendance is under-recorded

*Gap A · the check's result*

| Item | Value |
| --- | --- |
| Registered, remote accommodation | 59.4% |
| Registered, no remote accommodation | 3.6% |
| No registered disability | 4.6% |

- False-referral rates, Lab 2.4
- Intervals: 52.5 to 65.9; 1.7 to 7.7; 4.2 to 4.9
- The record is 16.8 points below the roll call for the first group
- **Measurement bias.** Fix the feed of remote attendance

#### [day2#gap-b-result] Compare like with like and the gap moves to where the marks are missing

*Gap B · missed students, non-Saudi*

| Missed rate | Saudi | non-Saudi |
| --- | --- | --- |
| Mark present | 41.6% (39.4 to 43.9) | 45.9% (37.6 to 54.3) |
| Mark missing | 76.7% (65.8 to 84.9) | 86.2% (77.4 to 91.9) |

- **Candidates:** coverage bias (no marks) or aggregation bias (limits that do not fit)
- With a mark, both groups are missed at similar rates
- Without one, both are missed three times in four or more
- **Coverage bias.** Bring the bridging programme's marks into the registry

#### [day2#name-decides-fix] The name decides the fix, and a wrong name produces a harmful one

*Why the name matters*

| If you had concluded | You would have | And then |
| --- | --- | --- |
| "The limit does not fit students with a disability" | Lowered their attendance limit | Missed those who truly stop attending, and left the record wrong |
| "The rule does not fit non-Saudi students" | Set separate limits by nationality | Treated students by a protected characteristic, and still missed Saudi bridging-year entrants |
| Measurement and coverage | Repaired two data feeds | Fixed it for everyone the feeds had failed |

#### [day2#what-metrics-cannot-settle] A fairness metric cannot tell you which fairness to want

*The limit of the numbers*

- When groups differ in how often the outcome occurs, a rule **cannot** equalise every error rate and every hit rate at once
- Lowering false referrals for a group raises its misses, or the reverse
- How large a remaining gap is acceptable is not a statistical question

- **Who decides.** The director of the unit owns the rule; the data protection officer owns the impact on students. You bring the rates, the intervals, the cause you could establish and what stays open. They choose.

#### [day2#check-name-bias] Which check separates the two candidates?

*Checkpoint*

**Question:** A training centre flags trainees with fewer than three logged sessions a week. One branch is flagged three times as often. Either its sessions are logged too low (measurement), or one limit does not fit a branch with fewer, longer sessions (aggregation). Which check separates the two?

- A. Recompute the flag rates with confidence intervals
- B. Compare logged sessions with the branch's attendance sheets
- C. Lower the limit for that branch and see whether the gap closes
- D. Ask the branch's trainers whether the rule seems fair

#### [day2#lab-2-4] Two gaps, two names

Lab 2.4 · 25 min

Match two observed gaps to bias types in the national guide and run the check that separates them.

[D2_4_name_the_bias.ipynb](https://sdaiaacademy.github.io/ds-207/labs/D2_4_name_the_bias.ipynb)

- [ ] Read the two gaps and their intervals (3 min)
- [ ] Pick two candidate bias types for each gap (6 min)
- [ ] Design the check that separates them (6 min)
- [ ] Run the two checks (7 min)
- [ ] Record the conclusion and what stays open (3 min)
- [ ] ✱ Stretch: Change the rule to equalise false referrals and report what happens to missed students

#### [day2#wrap-up] Three things to keep

*Day 2*

- **Attack your own table.** Small cells, then totals, then earlier releases. When suppression eats the table, redesign it.
- **Rates by group, with intervals.** Referral, false referral, missed. Every comparison reported, each inside the strata that matter.
- **Two candidates and a check.** A gap is not a cause. The name decides the fix, so earn the name.

#### [day2#next] Day 3: professional conduct

*Tomorrow*

The work so far lives in your head and your notebook. Tomorrow it becomes something others can check, and you hold three conversations.

- You will role-play in threes: analyst, sponsor, observer
- No AI assistant in the role-plays

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

## Capstone: Capstone: the responsible-practice pack

Eight-minute defences: six to present the pack with a short role-play inside, two for the assessor's changed fact

#### [capstone#title] Capstone: the responsible-practice pack

*SDAIA Academy · Responsible Data Practice and Conduct in Analytical Work*

Capstone: Eight-minute defences: six to present the pack with a short role-play inside, two for the assessor's changed fact

Data Science Track · 3 teaching days + capstone day · 6 min talk and demo · 2 min Q&A · DS-207

#### [capstone#agenda] How the defences run

*Capstone*

- **Expectations and final prep**: the rubric, the format, one last rehearsal of the role-play
- **Defences**: eight minutes each: the pack, the role-play, one changed fact
- **Review and closing**: peer feedback, the trainer's review, what next

#### [capstone#rubric] The rubric

*How the pack is scored*

| Item | Value |
| --- | --- |
| Legal and classification decisions | 25% |
| Release tables and suppression | 20% |
| Group comparison | 20% |
| Documentation | 20% |
| Scope note | 15% |

> **Every decision has a reason and an owner.** "Refused" or "suppressed" without the rule, the harm and the approver is a guess, not a decision.

#### [capstone#format] Eight minutes for each defence

*Format*

- **1 · The pack · 4 minutes.** The engagement, the sharing decision, one release table, the largest gap between groups and its likely cause.
- **2 · The role-play · 2 minutes.** A peer plays the sponsor of your brief and presses. You rescope the request. No AI assistant, no notes on screen.
- **3 · One fact changes · 2 minutes.** The assessor changes one fact of the partner's request. You revise the sharing decision aloud.

> **Peer feedback.** After each defence, everyone writes one strength, one question and one suggestion.

#### [capstone#running-order] Who defends when

*Running order*

| # | Participant | Engagement |
| --- | --- | --- |
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |
| 4 |  |  |
| 5 |  |  |
| 6 |  |  |
| 7 |  |  |
| 8 |  |  |

#### [capstone#final-prep] Final prep · 20 minutes

*Before the first defence*

Open your repository on this screen, rehearse the role-play once, choose the table you will show.

#### [capstone#now-presenting] Pack and role-play

*Now defending*

##### One fact changes

#### [capstone#review] What the defences showed

*Trainer review*

- **Strongest patterns.** What several packs got right.
- **Common gaps.** What most packs would fix next.
- **One surprise.** Something nobody expected.

#### [capstone#what-next] Keep going

*After the course*

- **The follow-up task:** a classification and sharing table for one dataset you work with, agreed with its data owner
- **Your pack stays yours:** reuse the templates for the datasheet, the log and the scope note in your next analysis
- **Next Academy course:** DS-309, Responsible Data Science: Privacy, Fairness and Documentation, takes release and group comparison further: re-identification risk, differential privacy, synthetic data and model audits

#### [capstone#thanks] Thank you

*SDAIA Academy*

Responsible Data Practice and Conduct in Analytical Work
