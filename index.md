---
course: "Responsible Data Practice and Conduct in Analytical Work"
code: "DS-207"
version: "2027.1.0"
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/ds-207/index.html"
---

# Responsible Data Practice and Conduct in Analytical Work

الممارسة المسؤولة للبيانات وقواعد السلوك في العمل التحليلي

Data Science Track · 3 teaching days + capstone day · 21 hours · Level 200

Handle an analytical request lawfully and fairly: test it against the PDPL, classify and share with conditions, release tables that single nobody out, compare groups honestly, document the work and hold the conversation that rescopes an unsafe request

Participants handle an analytical engagement for a fictional university's student-success unit. They test requests against the Personal Data Protection Law (PDPL), classify the data and decide what may be shared with a government partner, suppress small cells in aggregate outputs, compare outcome and error rates across student groups, keep an analysis log and a datasheet, and handle three stakeholder conversations: scoping, pushing back on an unsafe request and explaining limits. Deeper de-identification and fairness audits are in DS-309.

**Who it is for:** Practitioners. Graduates and early-career analysts who have completed the FN courses or passed the placement test, and analysts moving into data science.

**Format:** Intensive: 3 teaching days of four sessions and a capstone day, with guided pre-work and a tracked follow-up task

## The case study

**Al-Qimam University, Student Success Unit.** Al-Qimam University is a fictional public university with six colleges. Its Student Success Unit runs Awn, a rule that refers students to academic support from attendance and midterm marks, and its analyst is asked to evaluate the rule, publish tables, answer a government partner and serve three sponsors. All 18,000 student records are synthetic, generated with a fixed seed, and planted with the problems the labs find: identifiers in free-text notes, small cells that a subtraction recovers, attendance that is under-recorded for one group, marks that are missing for another, a gap that vanishes inside colleges, and a sharing request that asks for too much.

## The course

### Day 1: Lawful analysis

Slides: https://sdaiaacademy.github.io/ds-207/slides/day1.md

- **Session 1: What the law asks of an analyst**
  - Name the PDPL rules an analysis request engages, from lawful basis to transfer
  - Distinguish analysis inside the collection purpose from a new purpose, a disclosure and a transfer
  - Decide which requests go to the data protection officer before any data is touched
  - [Lab 1.1: Five requests, which rules (25 min)](https://sdaiaacademy.github.io/ds-207/labs/D1_1_five_requests.ipynb)
- **Session 2: Purpose, minimisation and secondary use**
  - Write a purpose precise enough to decide each field against
  - Cut an extract to the fields the purpose needs, keeping, coarsening or dropping each with a reason
  - Recognise a secondary use and name what the law and the national rules require before it starts
  - [Lab 1.2: Cut the extract (25 min)](https://sdaiaacademy.github.io/ds-207/labs/D1_2_cut_extract.ipynb)
- **Session 3: Classifying data and outputs**
  - Classify a dataset or an output with the impact questions of the Data Classification Policy
  - Apply the highest-level rule to combined data and say when an aggregate can be Public
  - Name the control each level requires, including what may be entered into an AI tool
  - [Lab 1.3: Classify and control (25 min)](https://sdaiaacademy.github.io/ds-207/labs/D1_3_classify_control.ipynb)
- **Session 4: Sharing requests**
  - Assess a sharing request against the tests of the Data Sharing Policy and the rules for secondary use
  - Choose the form of release: record level, pseudonymised or aggregate
  - Draft approval conditions under the policy's control headings and name who signs
  - [Lab 1.4: The Observatory's request (25 min)](https://sdaiaacademy.github.io/ds-207/labs/D1_4_sharing_request.ipynb)

### Day 2: Fair and safe outputs

Slides: https://sdaiaacademy.github.io/ds-207/slides/day2.md

- **Session 1: Aggregate release and small cells**
  - Explain how a small cell, a total or a second release singles out a student
  - Apply a threshold rule with complementary suppression and log each suppressed cell
  - Test a release for recovery by subtraction and by differencing before it leaves
  - [Lab 2.1: Suppress, then attack (25 min)](https://sdaiaacademy.github.io/ds-207/labs/D2_1_small_cells.ipynb)
- **Session 2: Where bias enters**
  - Trace a rule's data from the event to the decision and mark where bias can enter
  - Distinguish a recording problem, a coverage problem, a label problem and a use problem
  - Measure one entry point with data instead of arguing about it
  - [Lab 2.2: Four entry points (25 min)](https://sdaiaacademy.github.io/ds-207/labs/D2_2_bias_entry_points.ipynb)
- **Session 3: Comparing groups**
  - Compute referral, false-referral and missed-student rates by group
  - Report each rate and each difference with a confidence interval
  - Check whether a gap survives inside colleges before explaining it
  - [Lab 2.3: Rates with intervals (25 min)](https://sdaiaacademy.github.io/ds-207/labs/D2_3_group_rates.ipynb)
- **Session 4: Naming the bias**
  - Match an observed gap to candidate bias types in the AI Bias Reference Guide
  - Design the check that separates two candidate causes
  - State what a fairness metric cannot settle and who decides the rest
  - [Lab 2.4: Two gaps, two names (25 min)](https://sdaiaacademy.github.io/ds-207/labs/D2_4_name_the_bias.ipynb)

### Day 3: Professional conduct

Slides: https://sdaiaacademy.github.io/ds-207/slides/day3.md

- **Session 1: Datasheets and analysis logs**
  - Fill a datasheet that states what the data is, how it was collected and what it must not be used for
  - Keep an analysis log in which every decision has a reason, a date and an approver
  - Tie a release to a version so a result can be traced and rerun
  - [Lab 3.1: Datasheet and log (25 min)](https://sdaiaacademy.github.io/ds-207/labs/D3_1_datasheet_log.ipynb)
- **Session 2: Scoping with a sponsor**
  - Ask the questions that turn a request into a decision, a population, a measure and a time frame
  - Agree success criteria and what is out of scope before any analysis starts
  - Record the agreement in a scope note the sponsor confirms
  - [Lab 3.2: Scope in six minutes (25 min)](https://sdaiaacademy.github.io/ds-207/labs/D3_2_scoping_roleplay.ipynb)
- **Session 3: Pushing back without obstructing**
  - Refuse an unsafe request by naming the harm and the rule, not by citing policy at the sponsor
  - Offer a lawful alternative that serves the sponsor's decision
  - Recognise when to escalate to the data protection officer and record the agreement
  - [Lab 3.3: The risk list (25 min)](https://sdaiaacademy.github.io/ds-207/labs/D3_3_pushback_roleplay.ipynb)
- **Session 4: Explaining limits**
  - State what an analysis cannot show, separately from how uncertain it is
  - Write a limits statement a non-specialist cannot misread
  - Choose the capstone engagement and list what its pack must contain
  - [Lab 3.4: Three sentences and the capstone case (25 min)](https://sdaiaacademy.github.io/ds-207/labs/D3_4_limits_statement.ipynb)

### Capstone: Capstone: the responsible-practice pack

Slides: https://sdaiaacademy.github.io/ds-207/slides/capstone.md

## Capstone

A responsible-practice pack for one of three synthetic engagements (sharing decision, suppressed tables and log, group comparison, datasheet, analysis log, scope note) in a public repository; eight-minute defence that includes a short role-play

**What you submit:** A public GitHub repository holding the responsible-practice pack for one of the three synthetic engagements: the sharing decision with its conditions, the suppressed tables with the suppression log, the group comparison with intervals and named bias types, the datasheet, the analysis log and the scope note, with a README that links each part and states who approved each release and what the analysis must not be used for. Then an eight-minute defence: six minutes on the pack, including a two-minute role-play with the sponsor, and two minutes in which the assessor changes one fact of the request and the participant revises the sharing decision.

**Rubric:**

- Legal and classification decisions: 25%
- Release tables and suppression: 20%
- Group comparison: 20%
- Documentation: 20%
- Scope note: 15%

## Outcomes

- **LO1** Explain the PDPL principles and the classification and sharing rules an analysis engages, from lawful basis to data subjects' rights and transfer, given five analysis requests from the case (Awareness) Evidence: a note per request naming the rules engaged, at least four of five right
- **LO2** Classify the datasets and outputs of an analysis and decide what may be shared, with whom and in what form, given the student records, a partner's sharing request and the classification policy (Applied) Evidence: a classification and sharing table with the control each decision requires
- **LO3** Apply aggregation and small-cell suppression to results tables and check that no student can be singled out, given draft tables by college, nationality and disability status (Applied) Evidence: release-ready tables and a log of each suppressed cell and the reason
- **LO4** Analyse referral and error rates across student groups and report differences with their uncertainty and possible causes, given a support-referral rule and its results by group (Applied) Evidence: rates with intervals and two possible bias types with the check that separates them
- **LO5** Prepare a datasheet and an analysis log that let a reviewer trace each result to its data, decisions and approvals, given the case analysis and a template (Applied) Evidence: a datasheet and log a peer uses to answer five audit questions
- **LO6** Lead a stakeholder conversation that rescopes an unsafe or unclear request into a lawful, answerable question, and record the agreement, given a role-played sponsor asking for an individual-level risk list (Performance) Evidence: an observed role-play scored on a rubric and a written scope note

## Tools

- **Analysis environment and notebooks:** Python with JupyterLab or marimo, R with Quarto
- **Dataframes and analytical SQL engine:** DuckDB, Polars, pandas
- **Personal data detection:** Presidio, regular-expression rules
- **Group metrics:** Fairlearn, grouped metrics written in SQL or pandas
- **Documentation templates:** Markdown datasheet templates in Git, Quarto documents

## Prerequisites

- FN-106 Responsible Data and AI Practice in the Kingdom
- Computes rates and a confidence interval for a proportion by group in SQL or a dataframe
- Has written a short analytical report for a non-specialist reader

## Sources

### National references: personal data

- [Personal Data Protection Law (SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf)
- [Implementing Regulation of the Personal Data Protection Law (SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulationPersonalDataProtectionLaw.pdf)
- [Regulation on Personal Data Transfer outside the Kingdom (SDAIA)](https://sdaia.gov.sa/Documents/RegulationonPersonalDataEN.pdf)
- [Personal Data Destruction, Anonymization and Pseudonymisation Guideline (SDAIA)](https://sdaia.gov.sa/Documents/PersonalDataDestructionAnonymizationAndEncryptionGuideline.pdf)

### National references: data management (NDMO)

- [Data Classification Policy (NDMO, SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Documents/DataClassificationPolicy.pdf)
- [Data Sharing Policy, version 2.0 (NDMO, SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Documents/DataSharingPolicyEN.pdf)
- [General Rules for Secondary Use of Data, issue 1.0 (SDAIA)](https://sdaia.gov.sa/Documents/GeneralRulesForSecondaryUseOfData_EN.pdf)

### National references: AI ethics and bias

- [AI Ethics Principles (SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Documents/ai-principles.pdf)
- [AI Bias Reference Guide, first edition (SDAIA, May 2026)](https://sdaia.gov.sa/en/MediaCenter/KnowledgeCenter/ResearchLibrary/EN-AI-BIAS.pdf)
- [Generative AI Guidelines for Government (SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Files/GenAIGuidelinesForGovernmentENCompressed.pdf)
- [Regulations and policies index (SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Pages/RegulationsAndPolicies.aspx)

### Disclosure control, fairness and documentation

- [Frequently Asked Questions: Disclosure Avoidance (Privacy Technical Assistance Center, US Department of Education)](https://studentprivacy.ed.gov/sites/default/files/resource_document/file/FAQs_disclosure_avoidance_0.pdf)
- [Gebru et al., Datasheets for Datasets](https://arxiv.org/abs/1803.09010)
- [Suresh and Guttag, A Framework for Understanding Sources of Harm throughout the Machine Learning Life Cycle](https://arxiv.org/abs/1901.10002)
- [Kleinberg, Mullainathan and Raghavan, Inherent Trade-Offs in the Fair Determination of Risk Scores](https://arxiv.org/abs/1609.05807)
- [Chouldechova, Fair prediction with disparate impact](https://arxiv.org/abs/1610.07524)
- [Barocas, Hardt and Narayanan, Fairness and Machine Learning](https://fairmlbook.org/)

### Tools

- [pandas](https://pandas.pydata.org/)
- [DuckDB](https://duckdb.org/)
- [Polars](https://pola.rs/)
- [JupyterLab documentation](https://jupyterlab.readthedocs.io/en/stable/)
- [marimo](https://marimo.io/)
- [Quarto](https://quarto.org/)
- [Fairlearn: common fairness metrics](https://fairlearn.org/main/user_guide/assessment/common_fairness_metrics.html)
- [Presidio, personal data detection and anonymisation](https://data-privacy-stack.github.io/presidio/)
- [statsmodels: confidence intervals for a proportion (Wilson)](https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportion_confint.html)

---

SDAIA Academy · Data Science Track · Responsible Data Practice and Conduct in Analytical Work

Course version 2027.1.0 · engine 1.0.0 · built 2026-11-15 · commit e8058f5
