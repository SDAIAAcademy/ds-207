<!-- academy:title -->
# Responsible Data Practice and Conduct in Analytical Work

الممارسة المسؤولة للبيانات وقواعد السلوك في العمل التحليلي

Data Science Track · SDAIA Academy · DS-207 · Level 200

Handle an analytical request lawfully and fairly: test it against the PDPL, classify and share with conditions, release tables that single nobody out, compare groups honestly, document the work and hold the conversation that rescopes an unsafe request

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
| Capstone | Capstone: the responsible-practice pack |  | [`slides/capstone.html`](slides/capstone.html) |
<!-- /academy:units -->

## Case study

**Al-Qimam University, Student Success Unit.** Al-Qimam University is a fictional public university with six colleges. Its Student Success Unit runs Awn, a rule that refers students to academic support from attendance and midterm marks, and its analyst is asked to evaluate the rule, publish tables, answer a government partner and serve three sponsors. All 18,000 student records are synthetic, generated with a fixed seed, and planted with the problems the labs find: identifiers in free-text notes, small cells that a subtraction recovers, attendance that is under-recorded for one group, marks that are missing for another, a gap that vanishes inside colleges, and a sharing request that asks for too much.

<!-- academy:labs -->
## Labs

Every lab is a notebook in `labs/`. Open it in Google Colab from the course page, or run it locally with `uv`. Exercises raise `NotImplementedError` until they are done; the reference versions are in `labs/solutions/`.

| | Session | Lab | File |
|---|---|---|---|
| 1.1 | Day 1 · Session 1 | Five requests, which rules | [`D1_1_five_requests.ipynb`](labs/D1_1_five_requests.ipynb) |
| 1.2 | Day 1 · Session 2 | Cut the extract | [`D1_2_cut_extract.ipynb`](labs/D1_2_cut_extract.ipynb) |
| 1.3 | Day 1 · Session 3 | Classify and control | [`D1_3_classify_control.ipynb`](labs/D1_3_classify_control.ipynb) |
| 1.4 | Day 1 · Session 4 | The Observatory's request | [`D1_4_sharing_request.ipynb`](labs/D1_4_sharing_request.ipynb) |
| 2.1 | Day 2 · Session 1 | Suppress, then attack | [`D2_1_small_cells.ipynb`](labs/D2_1_small_cells.ipynb) |
| 2.2 | Day 2 · Session 2 | Four entry points | [`D2_2_bias_entry_points.ipynb`](labs/D2_2_bias_entry_points.ipynb) |
| 2.3 | Day 2 · Session 3 | Rates with intervals | [`D2_3_group_rates.ipynb`](labs/D2_3_group_rates.ipynb) |
| 2.4 | Day 2 · Session 4 | Two gaps, two names | [`D2_4_name_the_bias.ipynb`](labs/D2_4_name_the_bias.ipynb) |
| 3.1 | Day 3 · Session 1 | Datasheet and log | [`D3_1_datasheet_log.ipynb`](labs/D3_1_datasheet_log.ipynb) |
| 3.2 | Day 3 · Session 2 | Scope in six minutes | [`D3_2_scoping_roleplay.ipynb`](labs/D3_2_scoping_roleplay.ipynb) |
| 3.3 | Day 3 · Session 3 | The risk list | [`D3_3_pushback_roleplay.ipynb`](labs/D3_3_pushback_roleplay.ipynb) |
| 3.4 | Day 3 · Session 4 | Three sentences and the capstone case | [`D3_4_limits_statement.ipynb`](labs/D3_4_limits_statement.ipynb) |
<!-- /academy:labs -->

## Capstone

A responsible-practice pack for one of three synthetic engagements (sharing decision, suppressed tables and log, group comparison, datasheet, analysis log, scope note) in a public repository; eight-minute defence that includes a short role-play

**Submission:** a public GitHub repository holding the pack, with a README that links each part and states who approved each release and what the analysis must not be used for. The defence takes eight minutes: six on the pack, including a two-minute role-play with the sponsor, and two in which the assessor changes one fact of the partner's request and the participant revises the sharing decision.

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
<!-- /academy:sources -->

### National references

- Personal Data Protection Law and its implementing regulations: <https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf> and <https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulationPersonalDataProtectionLaw.pdf>
- Regulation on Personal Data Transfer outside the Kingdom: <https://sdaia.gov.sa/Documents/RegulationonPersonalDataEN.pdf>
- PDPL guideline on destruction, anonymisation and pseudonymisation of personal data: <https://sdaia.gov.sa/Documents/PersonalDataDestructionAnonymizationAndEncryptionGuideline.pdf>
- NDMO Data Classification Policy: <https://sdaia.gov.sa/en/SDAIA/about/Documents/DataClassificationPolicy.pdf>
- NDMO Data Sharing Policy: <https://sdaia.gov.sa/en/SDAIA/about/Documents/DataSharingPolicyEN.pdf>
- General Rules for Secondary Use of Data: <https://sdaia.gov.sa/Documents/GeneralRulesForSecondaryUseOfData_EN.pdf>
- SDAIA AI Ethics Principles: <https://sdaia.gov.sa/en/SDAIA/about/Documents/ai-principles.pdf>
- SDAIA AI Bias Reference Guide: <https://sdaia.gov.sa/en/MediaCenter/KnowledgeCenter/ResearchLibrary/EN-AI-BIAS.pdf>
