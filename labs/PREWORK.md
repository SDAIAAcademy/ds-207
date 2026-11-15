# Pre-work: back to the law and the classification levels

Do this before Day 1. It takes about two hours. You revisit what FN-106 (Responsible Data and AI
Practice in the Kingdom) taught about the Personal Data Protection Law and data
classification, read three short parts that are new, and take an entry quiz of ten questions.

This course does not teach the law again. It starts from the summaries below and asks a
different question: what do they mean for someone who analyses data?

**AI policy for the pre-work.** An assistant may tutor you through an instrument, but check every
answer against the official text: assistants invent article numbers. Take the entry quiz without
an assistant.

## Part 1 · Revisit your FN-106 summaries (about 70 minutes)

Open your notes and the session summaries of FN-106. For each row, write two sentences of your
own before you look anything up.

| # | From FN-106 | Write, from memory |
|---|---|---|
| 1 | Day 1 · Where personal data flows | What makes data "personal"? Which kinds does the law call sensitive? |
| 2 | Day 1 · Lawful basis and minimisation | When may data be processed without consent? What does "minimum necessary" ask you to do? |
| 3 | Day 1 · Pseudonymisation and its limits | Why is a pseudonymised file still personal data? What would make it anonymous? |
| 4 | Day 1 · Rights, retention and breaches | Which rights does a data subject have? How long does a controller have to answer? |
| 5 | Day 2 · Data classification levels | What are the four levels, and what decides the level of a dataset? |
| 6 | Day 2 · What may reach an external model | Which data may be entered into a generative AI tool? |
| 7 | Day 2 · Sharing with another entity | What must a requester state, and what limits it afterwards? |

Then check each answer against the text. All instruments are on SDAIA's regulations and policies
page: <https://sdaia.gov.sa/en/SDAIA/about/Pages/RegulationsAndPolicies.aspx>.

## Part 2 · Three short readings that are new (about 35 minutes)

| # | Instrument | Read | Answer while you read |
|---|---|---|---|
| 1 | [Personal Data Protection Law](https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf) | Articles 10, 15 and 27 | When may data be collected or processed for a purpose other than the one it was collected for? What does the law ask of processing for scientific, research or statistical purposes? |
| 2 | [General Rules for Secondary Use of Data](https://sdaia.gov.sa/Documents/GeneralRulesForSecondaryUseOfData_EN.pdf) | The definitions and the principles | What is "secondary use"? Name two conditions a secondary use must meet. |
| 3 | [AI Bias Reference Guide](https://sdaia.gov.sa/en/MediaCenter/KnowledgeCenter/ResearchLibrary/EN-AI-BIAS.pdf) | The entries on measurement, coverage, aggregation and automation bias | For each of the four: one sentence, and one example from your own work. |

## Part 3 · Entry quiz (about 15 minutes)

Answer without an assistant, then open the answers. Seven or more correct: you are ready. Fewer:
read again the part named beside each answer you missed. The quiz is for you; it is not part of
the course grade.

1. A file has student names removed and student numbers replaced by codes. The registrar keeps the key. For the analyst who receives it, the file is:
   a) Anonymous data  b) Personal data  c) Public data  d) Outside the law
2. Which of these fields is sensitive data under the law?
   a) College  b) Level of study  c) A registered disability  d) University email address
3. A student asks the University what data it holds about him. Without an extension, the University answers within:
   a) 72 hours  b) 7 days  c) 30 days  d) 90 days
4. "Minimum necessary" means the analyst:
   a) Takes every field in case it is useful later  b) Takes the fields the stated purpose needs  c) Takes only fields that are not personal  d) Takes what the system exports by default
5. Under the Generative AI Guidelines for Government, which data may be entered into a public generative AI tool?
   a) Restricted data with the names removed  b) Any data on an official device  c) Data classified Public only  d) Any data, if the tool is licensed
6. Which list gives the four classification levels of the Data Classification Policy?
   a) Critical, Sensitive, Internal, Public  b) Top Secret, Secret, Restricted, Public  c) High, Medium, Low, None  d) Secret, Private, Internal, Open
7. A dataset holds personal data whose disclosure would harm individuals' privacy. Under the policy its level is at least:
   a) Public  b) Restricted  c) Unclassified  d) Open
8. Another entity asks for data "for research". Under the Data Sharing Policy the requester must first:
   a) Show it has paid a fee  b) State a specific purpose  c) Promise to delete the data in a year  d) Name a senior sponsor
9. Data collected to advise students is later used to rank lecturers. This is best described as:
   a) The same purpose  b) Anonymisation  c) A new purpose  d) Minimisation
10. People who trust a system's output over their own judgement show:
    a) Measurement bias  b) Coverage bias  c) Aggregation bias  d) Automation bias

<details><summary>Answers</summary>

1. b: pseudonymised data stays personal data while a key exists (the pseudonymisation guideline; FN-106 Day 1, session 3).
2. c: health data is on the law's list of sensitive data (Article 1).
3. c: 30 days, which may be extended with notice (Implementing Regulation, Article 3).
4. b: the content of the data is limited to what the purpose needs (Article 11).
5. c: only data classified Public (Generative AI Guidelines for Government).
6. b: Top Secret, Secret, Restricted, Public (Data Classification Policy, table of levels).
7. b: Restricted (Data Classification Policy, classification steps).
8. b: purpose limitation is a principle of the policy; sharing is for a stated, specific purpose.
9. c: a purpose other than the one the data was collected for (Article 10).
10. d: automation bias (AI Bias Reference Guide).
</details>

## Before Day 1

- Run `00_setup_check.ipynb`, in Colab or locally (see [`README.md`](README.md)).
- Bring your two-sentence answers from Part 1. Day 1 opens with them.
