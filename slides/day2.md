---
course: "Responsible Data Practice and Conduct in Analytical Work"
code: "DS-207"
version: "2027.1.0"
deck: "day2"
day: 2
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/ds-207/slides/day2.html"
---

# Responsible Data Practice and Conduct in Analytical Work

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
