# Answer key for trainers

What is planted in the synthetic data and the numbers the solution notebooks print. The data is
generated with seed 207, so every run gives the same figures. The keys of the Day 1 decisions
(requests, classification, sharing conditions) and of the capstone data are in `keys.json`.

## The case in numbers

| Quantity | Value |
|---|---|
| Students, columns in `students.csv` | 18,000 · 30 |
| Referred by Awn (attendance under 75% or midterm under 2.5 of 5) | 2,040 (11.3%) |
| Ended the term struggling | 2,191 |
| Referred and struggled · referred and did not · struggled and not referred · neither | 1,209 · 831 · 982 · 14,978 |
| False-referral rate · missed rate | 5.3% · 44.8% |
| Share of struggling students referred | 55% (1,209 of 2,191), interval about 53% to 57% |

## Day 1

| Lab | What to expect |
|---|---|
| 1.1 Five requests | R1 within the purpose; R2 and R4 new internal purposes (R4 refused: advertising); R3 a disclosure; R5 a transfer outside the Kingdom. All but R1 go to the data protection officer |
| 1.2 Cut the extract | 30 columns become 8: 22 dropped, 7 kept, 1 coarsened. In the 2,400 advisor notes: 180 with a phone number, 70 with an identity number, 210 with health details, 80 naming another person |
| 1.3 Classify | Student records, the health file and the pseudonymised extract are Restricted; published statistics and tables with large counts are Public. Only Public data may go to a generative AI tool |
| 1.4 Sharing request | The observatory asks for 11 fields for 18,000 students; the decision offers 5 fields for 3,612, with conditions under each of the policy's control headings |

## Day 2

| Lab | What to expect |
|---|---|
| 2.1 Small cells | The cross table of college by nationality group for students with a registered disability has cells under 10 in five of the six colleges (non-Saudi: Arts 8, Business 8, Computing 1, Engineering 12, Health 3, Science 4). Primary suppression alone can be undone from the totals; the Saudi-only table released later would undo it by subtraction, which is the differencing check against the October release |
| 2.2 Entry points | Two recording problems are placed in the pipeline: attendance from card readings, and the midterm mark feed |
| 2.3 Group rates | Missed rate: non-Saudi 61.8% against Saudi 42.9%, difference 18.9 points (12.0 to 25.4). False-referral rate: registered disability 34.2%, difference 29.7 points (25.0 to 34.7). Referral rate by gender differs by 1.9 points (0.9 to 2.8) and the difference disappears within colleges |
| 2.4 Name the bias | Measurement bias: for the 300 students with a remote accommodation the record is 16.8 points below the roll call; 191 are under the attendance limit on record and 14 in truth. False-referral rate 59.4% for them, 3.6% for the 187 registered students without the accommodation, 4.6% for everyone else. Coverage bias: 1,244 students have no midterm mark, all bridging-year entrants (36.2% of non-Saudi students, 3.4% of Saudi students). Missed rate with a mark present and missing: Saudi 41.6% and 76.7%, non-Saudi 45.9% and 86.2% |

The gender difference is the planted example of a gap that is real, small and explained by
composition. Participants who report it as unfairness have skipped the check within colleges.

## Day 3

| Lab | What to expect |
|---|---|
| 3.1 Datasheet and log | Seven sections; the datasheet states both recording problems. Three log entries added to the two supplied (L003 to L005). The release record carries a file fingerprint. The mechanical auditor answers the five audit questions from the documents alone |
| 3.2 Scope in six minutes | What each sponsor's card holds is in `data/sponsor_briefs.json`. The solution's scope note is for brief B2; its out-of-scope line is "whether support helps: no comparison group" |
| 3.3 The risk list | Alternatives A1 and A2 pass both tests. The advisor table places 2.7 of 12 advisors in Health Sciences, the most. The observer's rubric has five behaviours scored 0 to 2; it is the rubric of the observed role-play |
| 3.4 Three sentences | Real limits: a, b, c, d, f, h. Not limits: e (sample size) and g (pseudonymisation). The solution's statement has three sentences and 83 words |

## The capstone engagements

Each engagement has 4,000 records, a rule, and one recording problem that makes the rule wrong
for one group. Do not tell participants which group.

| Engagement | Group affected | What is planted |
|---|---|---|
| Scholarships | Disability status | Students with a reduced-load accommodation are recorded below 12 credit hours although their load is approved |
| Housing | Nationality group | Non-Saudi students have no home address in the Kingdom on file, so the distance is recorded as 0 |
| Careers | Gender | Workshops ran in a building and at an hour that one campus section could not reach, so attendance is recorded low for it |

In all three the fitting type from the AI Bias Reference Guide is measurement bias, and a good
pack names a second candidate and the check that separates the two. Two of the three partners
(the charity and the employers' council) are not government entities, so a pack that applies
the Data Sharing Policy's entity-to-entity process to them without comment has missed a fact.
Each partner asks for more fields than its purpose needs and for row-level data.

## Scoring the defence

- Pack and role-play, six minutes: score the pack on the rubric of `capstone/README.md` and the
  role-play on the five behaviours of Lab 3.3.
- One fact changes, two minutes: change one of destination (outside the Kingdom), form (rows
  instead of tables), kind of partner, purpose (marketing), or add a health field. Full marks
  when the participant says what changes in the decision, which rule causes it and who decides.
