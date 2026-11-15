---
course: "Responsible Data Practice and Conduct in Analytical Work"
code: "DS-207"
version: "2027.1.0"
deck: "day1"
day: 1
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/ds-207/slides/day1.html"
---

# Responsible Data Practice and Conduct in Analytical Work

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
