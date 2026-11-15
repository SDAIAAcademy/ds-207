<!-- academy:title -->
# Responsible Data Practice and Conduct in Analytical Work

الممارسة المسؤولة للبيانات وقواعد السلوك في العمل التحليلي

Data Science Track · SDAIA Academy · DS-207 · Level 200

REPLACE: one line under the title: what participants can do after the course

Participants handle an analytical engagement for a fictional university's student-success unit. They test requests against the Personal Data Protection Law (PDPL), classify the data and decide what may be shared with a government partner, suppress small cells in aggregate outputs, compare outcome and error rates across student groups, keep an analysis log and a datasheet, and handle three stakeholder conversations: scoping, pushing back on an unsafe request and explaining limits. Deeper de-identification and fairness audits are in DS-309.

**Format:** Intensive: 3 teaching days of four sessions and a capstone day, with guided pre-work and a tracked follow-up task

**Course page:** https://sdaiaacademy.github.io/ds-207/
<!-- /academy:title -->

## Outcomes

| | Outcomes | Level | Evidence |
|---|---|---|---|
| LO1 | Explain the PDPL principles and the classification and sharing rules an analysis engages, from lawful basis to data subjects' rights and transfer, given five analysis requests from the case | Awareness | a note per request naming the rules engaged, at least four of five right |
| LO2 | Classify the datasets and outputs of an analysis and decide what may be shared, with whom and in what form, given the student records, a partner's sharing request and the classification policy | Applied | a classification and sharing table with the control each decision requires |
| LO3 | Apply aggregation and small-cell suppression to results tables and check that no student can be singled out, given draft tables by college, nationality and disability status | Applied | release-ready tables and a log of each suppressed cell and the reason |
| LO4 | Analyse referral and error rates across student groups and report differences with their uncertainty and possible causes, given a support-referral rule and its results by group | Applied | rates with intervals and two possible bias types with the check that separates them |
| LO5 | Prepare a datasheet and an analysis log that let a reviewer trace each result to its data, decisions and approvals, given the case analysis and a template | Applied | a datasheet and log a peer uses to answer five audit questions |
| LO6 | Lead a stakeholder conversation that rescopes an unsafe or unclear request into a lawful, answerable question, and record the agreement, given a role-played sponsor asking for an individual-level risk list | Performance | an observed role-play scored on a rubric and a written scope note |

<!-- academy:units -->
## Units

| Unit | Title | Sessions | Slides |
|---|---|---|---|
| Day 1 | Lawful analysis | What the law asks of an analyst; Purpose, minimisation and secondary use; Classifying data and outputs; Sharing requests | [`slides/day1.html`](slides/day1.html) |
| Day 2 | Fair and safe outputs | Aggregate release and small cells; Where bias enters; Comparing groups; Naming the bias | [`slides/day2.html`](slides/day2.html) |
| Day 3 | Professional conduct | Datasheets and analysis logs; Scoping with a sponsor; Pushing back without obstructing; Explaining limits | [`slides/day3.html`](slides/day3.html) |
| Capstone | Capstone project presentations |  | [`slides/capstone.html`](slides/capstone.html) |
<!-- /academy:units -->

## Case study

**REPLACE: the name of the fictional organisation every lab works on.** REPLACE: two sentences on the case study and its synthetic data

<!-- academy:labs -->
## Labs

Every lab is a notebook in `labs/`. Open it in Google Colab from the course page, or run it locally with `uv`. Exercises raise `NotImplementedError` until they are done; the reference versions are in `labs/solutions/`.

| | Session | Lab | File |
|---|---|---|---|
| 1.1 | Day 1 · Session 1 | Map five requests to the PDPL principles they engage | [`D1_1_map_five_requests.ipynb`](labs/D1_1_map_five_requests.ipynb) |
| 1.2 | Day 1 · Session 2 | Cut an extract to the fields the purpose needs, recording why | [`D1_2_cut_extract_fields.ipynb`](labs/D1_2_cut_extract_fields.ipynb) |
| 1.3 | Day 1 · Session 3 | Classify four datasets and three outputs and name each control | [`D1_3_classify_four_datasets.ipynb`](labs/D1_3_classify_four_datasets.ipynb) |
| 1.4 | Day 1 · Session 4 | Assess a partner's sharing request and draft approval conditions | [`D1_4_assess_partner_s.ipynb`](labs/D1_4_assess_partner_s.ipynb) |
| 2.1 | Day 2 · Session 1 | Apply a threshold rule and test for singling out by differencing | [`D2_1_apply_threshold_rule.ipynb`](labs/D2_1_apply_threshold_rule.ipynb) |
| 2.2 | Day 2 · Session 2 | Mark four points where bias can enter the referral data | [`D2_2_mark_four_points.ipynb`](labs/D2_2_mark_four_points.ipynb) |
| 2.3 | Day 2 · Session 3 | Compare referral and error rates by group with intervals | [`D2_3_compare_referral_error.ipynb`](labs/D2_3_compare_referral_error.ipynb) |
| 2.4 | Day 2 · Session 4 | Match two observed gaps to bias types in the national guide | [`D2_4_match_two_observed.ipynb`](labs/D2_4_match_two_observed.ipynb) |
| 3.1 | Day 3 · Session 1 | Fill a datasheet and log three decisions with their approver | [`D3_1_fill_datasheet_log.ipynb`](labs/D3_1_fill_datasheet_log.ipynb) |
| 3.2 | Day 3 · Session 2 | Turn a vague request into a question in a timed role-play | [`D3_2_turn_vague_request.ipynb`](labs/D3_2_turn_vague_request.ipynb) |
| 3.3 | Day 3 · Session 3 | Role-play a request for a risk list; agree a lawful alternative | [`D3_3_role_play_request.ipynb`](labs/D3_3_role_play_request.ipynb) |
| 3.4 | Day 3 · Session 4 | Write a three-sentence limits statement; choose the capstone case | [`D3_4_write_three_sentence.ipynb`](labs/D3_4_write_three_sentence.ipynb) |
<!-- /academy:labs -->

## Capstone

A responsible-practice pack for one of three synthetic engagements (sharing decision, suppressed tables and log, group comparison, datasheet, analysis log, scope note) in a public repository; eight-minute defence that includes a short role-play

**Submission:** REPLACE: what participants submit and how: a public repository link, or a shared folder for a course without code

## Prerequisites

- FN-106 Responsible Data and AI Practice in the Kingdom
- Computes rates and a confidence interval for a proportion by group in SQL or a dataframe
- Has written a short analytical report for a non-specialist reader

<!-- academy:tools -->
## Tools

Each line is a capability; the examples are interchangeable.

- **Analysis environment and notebooks:** Python with JupyterLab or marimo, R with Quarto
- **Dataframes and analytical SQL engine:** DuckDB, Polars, pandas
- **Personal data detection:** Presidio, regular-expression rules
- **Group metrics:** Fairlearn, grouped metrics written in SQL or pandas
- **Documentation templates:** Markdown datasheet templates in Git, Quarto documents
<!-- /academy:tools -->

<!-- academy:sources -->
## Sources

- REPLACE: every source the course cites, with its address, in course.json under "sources"; this list is written from there
<!-- /academy:sources -->

### National references

- Personal Data Protection Law and its implementing regulations: REPLACE: the address of the official text
- Regulation on Personal Data Transfer outside the Kingdom: REPLACE: the address of the official text
- PDPL guideline on destruction, anonymisation and pseudonymisation of personal data: REPLACE: the address of the official text
- NDMO Data Classification Policy: REPLACE: the address of the official text
- NDMO Data Sharing Policy: REPLACE: the address of the official text
- General Rules for Secondary Use of Data: REPLACE: the address of the official text
- SDAIA AI Ethics Principles: REPLACE: the address of the official text
- SDAIA AI Bias Reference Guide: REPLACE: the address of the official text
