"""Write the synthetic case data of DS-207 (Al-Qimam University, Student Success Unit).

    cd labs
    uv run python prepare_data.py

Standard library only, seed 207, the same bytes on every run. Nobody in these files exists:
names, identity numbers, phone numbers and notes are generated. The planted problems and the
lab that finds each one are listed in solutions/answer_key.md.
"""

from __future__ import annotations

import csv
import hashlib
import hmac
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
CAP = HERE / "capstone"
SEED = 207
TERM = "2026-27 term 1"
PROJECT_KEY = "awn-evaluation-2026-t1-lab-key"

COLLEGES = {
    # name: (students, share of women, difficulty shift, share of non-Saudi students)
    "Engineering": (3600, 0.25, -0.10, 0.11),
    "Science": (2700, 0.60, 0.28, 0.10),
    "Business": (3900, 0.40, -0.22, 0.12),
    "Health Sciences": (2400, 0.75, 0.42, 0.08),
    "Arts and Humanities": (3000, 0.50, 0.00, 0.15),
    "Computing": (2400, 0.35, -0.10, 0.09),
}
PROGRAMMES = {
    "Engineering": ["Civil Engineering", "Electrical Engineering", "Mechanical Engineering", "Industrial Engineering"],
    "Science": ["Mathematics", "Physics", "Chemistry", "Biology"],
    "Business": ["Accounting", "Finance", "Management", "Marketing"],
    "Health Sciences": ["Nursing", "Public Health", "Clinical Nutrition", "Medical Laboratory Science"],
    "Arts and Humanities": ["Arabic Language", "English Language", "History", "Geography"],
    "Computing": ["Computer Science", "Information Systems", "Data Science", "Cybersecurity"],
}
OTHER_NATIONALITIES = [("Yemeni", 24), ("Egyptian", 20), ("Syrian", 14), ("Sudanese", 12), ("Jordanian", 10),
                       ("Pakistani", 8), ("Indian", 6), ("Indonesian", 4), ("Nigerian", 2)]
CITIES = ["Riyadh", "Jeddah", "Dammam", "Abha", "Tabuk", "Hail", "Buraydah", "Najran", "Jazan", "Al-Ahsa"]
DISTRICTS = ["Al-Nakheel", "Al-Rawdah", "Al-Safa", "Al-Wurud", "Al-Faisaliyah", "Al-Khaleej", "Al-Aziziyah", "Al-Rabwah"]
DISABILITY_TYPES = ["visual", "hearing", "mobility", "chronic illness", "learning"]
F_NAMES = ["Alanoud", "Bayan", "Deema", "Ghala", "Hadeel", "Jood", "Lamar", "Maysa", "Nahla", "Rimas", "Sadeem",
           "Taif", "Wasan", "Yasmin", "Zainab", "Ruwaida", "Shahd", "Malak", "Leen", "Farah"]
M_NAMES = ["Abdullah", "Bilal", "Daifallah", "Eyad", "Fawaz", "Ghassan", "Hammam", "Jaber", "Karim", "Luay",
           "Mansour", "Nizar", "Qusai", "Rashed", "Salman", "Talal", "Usama", "Wissam", "Yahya", "Zakaria"]
FAMILIES = ["Al-Abdali", "Al-Bishri", "Al-Dabbagh", "Al-Fayez", "Al-Ghunaim", "Al-Hilali", "Al-Jadaan", "Al-Kathiri",
            "Al-Luhaib", "Al-Madani", "Al-Naimi", "Al-Oraini", "Al-Qasabi", "Al-Rifai", "Al-Sabban", "Al-Tayyar",
            "Al-Umari", "Al-Wabel", "Al-Yousfi", "Al-Zamil", "Bahammam", "Bakhashab", "Banaja", "Batarfi"]

COLUMNS = ["student_id", "national_id", "full_name", "email", "phone", "date_of_birth", "gender", "nationality",
           "home_city", "home_address", "college", "programme", "level_year", "admission_year", "admission_route",
           "scholarship", "first_generation", "disability_status", "disability_type", "remote_accommodation",
           "counselling_visits", "bank_iban", "attendance_rate", "midterm_gpa", "lms_logins", "awn_referred",
           "referral_date", "term_gpa", "term_outcome", "advisor_note"]

ATTENDANCE_LIMIT = 0.75
GPA_LIMIT = 2.5


def clip(x, lo, hi):
    return max(lo, min(hi, x))


def pseudonym(student_id: str, key: str = PROJECT_KEY) -> str:
    return "P" + hmac.new(key.encode(), student_id.encode(), hashlib.sha256).hexdigest()[:10]


def write_csv(path: Path, rows: list[dict], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=columns, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip("\n") + "\n", encoding="utf-8", newline="\n")


# --------------------------------------------------------------------------- students

def make_students(rng: random.Random) -> tuple[list[dict], list[dict]]:
    rows, truth = [], []
    n = 0
    for college, (size, share_f, shift, share_ns) in COLLEGES.items():
        for _ in range(size):
            n += 1
            sid = f"S{n:06d}"
            gender = "F" if rng.random() < share_f else "M"
            saudi = rng.random() >= share_ns
            nationality = "Saudi" if saudi else rng.choices([a for a, _ in OTHER_NATIONALITIES],
                                                            weights=[b for _, b in OTHER_NATIONALITIES])[0]
            level = rng.choices([1, 2, 3, 4], weights=[32, 26, 22, 20])[0]
            bridging = rng.random() < (0.06 if saudi else 0.62)
            registered = rng.random() < 0.022
            remote = rng.random() < (0.60 if registered else 0.004)
            first_gen = rng.random() < 0.31
            scholarship = rng.random() < (0.18 if saudi else 0.55)
            u = rng.gauss(0, 1) + shift + (0.18 if level == 1 else 0.0)
            true_att = clip(0.905 - 0.065 * u + rng.gauss(0, 0.04), 0.30, 1.0)
            recorded_att = clip(true_att - (rng.uniform(0.10, 0.24) if remote else 0.0) + rng.gauss(0, 0.01), 0.20, 1.0)
            midterm = clip(3.62 - 0.72 * u + rng.gauss(0, 0.38), 0.0, 5.0)
            term_gpa = clip(3.60 - 0.78 * u + rng.gauss(0, 0.36), 0.0, 5.0)
            midterm_missing = bridging and level <= 2
            struggled = term_gpa < GPA_LIMIT
            referred = recorded_att < ATTENDANCE_LIMIT or (not midterm_missing and midterm < GPA_LIMIT)
            first = rng.choice(F_NAMES if gender == "F" else M_NAMES)
            family = rng.choice(FAMILIES)
            nid = ("1" if saudi else "2") + f"{rng.randrange(10**9):09d}"
            visits = min(9, int(rng.expovariate(1 / (0.25 + (0.9 if struggled else 0.0) + (0.5 if registered else 0.0)))))
            rows.append({
                "student_id": sid, "national_id": nid, "full_name": f"{first} {family}",
                "email": f"{sid.lower()}@students.qimam.example", "phone": "05" + f"{rng.randrange(10**8):08d}",
                "date_of_birth": f"{2026 - 18 - level - rng.choice([0, 0, 0, 1, 1, 2])}-{rng.randint(1, 12):02d}-{rng.randint(1, 28):02d}",
                "gender": gender, "nationality": nationality, "home_city": rng.choice(CITIES),
                "home_address": f"Building {rng.randint(1, 60)}, Street {rng.randint(1, 40)}, {rng.choice(DISTRICTS)}",
                "college": college, "programme": rng.choice(PROGRAMMES[college]), "level_year": level,
                "admission_year": 2027 - level, "admission_route": "bridging_year" if bridging else "direct",
                "scholarship": "yes" if scholarship else "no", "first_generation": "yes" if first_gen else "no",
                "disability_status": "registered" if registered else "none",
                "disability_type": rng.choice(DISABILITY_TYPES) if registered else "",
                "remote_accommodation": "yes" if remote else "no", "counselling_visits": visits,
                "bank_iban": "SA" + f"{rng.randrange(10**22):022d}",
                "attendance_rate": f"{recorded_att:.3f}", "midterm_gpa": "" if midterm_missing else f"{midterm:.2f}",
                "lms_logins": max(0, int(rng.gauss(46 - 9 * u, 9))),
                "awn_referred": "yes" if referred else "no",
                "referral_date": f"2026-10-{rng.randint(18, 29):02d}" if referred else "",
                "term_gpa": f"{term_gpa:.2f}", "term_outcome": "struggled" if struggled else "ok", "advisor_note": "",
            })
            truth.append({"student_id": sid, "true_attendance": true_att})
    return rows, truth


def plant_small_cells(rows: list[dict], rng: random.Random) -> None:
    """Computing ends with exactly one non-Saudi student with a registered disability."""
    hits = [r for r in rows if r["college"] == "Computing" and r["nationality"] != "Saudi"
            and r["disability_status"] == "registered"]
    for r in hits[1:]:
        r["disability_status"], r["disability_type"], r["remote_accommodation"] = "none", "", "no"
    if not hits:
        r = next(r for r in rows if r["college"] == "Computing" and r["nationality"] != "Saudi")
        r["disability_status"], r["disability_type"] = "registered", "visual"


NOTE_PLAIN = ["Missed two tutorials, will attend the make-up session.", "Asked about changing programme next term.",
              "Works evenings; agreed a study plan for the weekend.", "Improved after joining the peer study group.",
              "Advised to book the writing centre before the next report.", "No concerns raised at the meeting.",
              "Late registration; two courses added in week three."]
NOTE_PHONE = ["Prefers a call on {phone} after the afternoon lab.", "New mobile {phone}; the old number is closed.",
              "Brother can be reached on {phone} if she is unreachable."]
NOTE_ID = ["Stipend held until identity number {nid} is corrected in the bank file.",
           "Residency renewal pending, identity number {nid}."]
NOTE_HEALTH = ["Missed three weeks after surgery; medical report filed.", "Mentioned treatment for anxiety; referred to counselling.",
               "Dialysis sessions clash with the Sunday lecture.", "Hearing aid broken; asked for front-row seating."]
NOTE_OTHER = ["Shares notes with {other}, who is also behind in the course.", "Says {other} copied the lab report."]


def plant_notes(rows: list[dict], rng: random.Random) -> dict:
    picked = rng.sample(range(len(rows)), 2400)
    counts = {"plain": 0, "phone": 0, "national_id": 0, "health": 0, "other_person": 0}
    for k, i in enumerate(picked):
        r = rows[i]
        if k < 180:
            r["advisor_note"] = rng.choice(NOTE_PHONE).format(phone="05" + f"{rng.randrange(10**8):08d}")
            counts["phone"] += 1
        elif k < 250:
            r["advisor_note"] = rng.choice(NOTE_ID).format(nid=r["national_id"])
            counts["national_id"] += 1
        elif k < 460:
            r["advisor_note"] = rng.choice(NOTE_HEALTH)
            counts["health"] += 1
        elif k < 540:
            r["advisor_note"] = rng.choice(NOTE_OTHER).format(other=rows[rng.randrange(len(rows))]["full_name"])
            counts["other_person"] += 1
        else:
            r["advisor_note"] = rng.choice(NOTE_PLAIN)
            counts["plain"] += 1
    return counts


def analysis_extract(rows: list[dict]) -> list[dict]:
    out = []
    for r in rows:
        out.append({
            "pid": pseudonym(r["student_id"]), "college": r["college"], "level_year": r["level_year"],
            "admission_route": r["admission_route"], "gender": r["gender"],
            "nationality_group": "Saudi" if r["nationality"] == "Saudi" else "non-Saudi",
            "disability_status": r["disability_status"], "first_generation": r["first_generation"],
            "remote_accommodation": r["remote_accommodation"], "attendance_rate": r["attendance_rate"],
            "midterm_gpa": r["midterm_gpa"], "awn_referred": r["awn_referred"], "term_outcome": r["term_outcome"],
        })
    out.sort(key=lambda r: r["pid"])
    return out


def roll_call_audit(rows: list[dict], truth: list[dict], rng: random.Random) -> list[dict]:
    """Instructors' roll calls for an audit sample: every student with a remote accommodation and 1,300 others."""
    by_id = {t["student_id"]: t["true_attendance"] for t in truth}
    remote = [r for r in rows if r["remote_accommodation"] == "yes"]
    others = rng.sample([r for r in rows if r["remote_accommodation"] == "no"], 1300)
    out = [{"pid": pseudonym(r["student_id"]),
            "roll_call_rate": f"{clip(by_id[r['student_id']] + rng.gauss(0, 0.012), 0.2, 1.0):.3f}"} for r in remote + others]
    out.sort(key=lambda r: r["pid"])
    return out


def previous_release(rows: list[dict]) -> list[dict]:
    """The table published last month: students with a registered disability, by college, all students."""
    out = []
    for college in COLLEGES:
        n = sum(1 for r in rows if r["college"] == college and r["disability_status"] == "registered")
        out.append({"college": college, "registered_disability_all_students": n})
    return out


# --------------------------------------------------------------------------- documents of the case

PRIVACY_NOTICE = """
# Al-Qimam University: privacy notice for students (extract, synthetic)

The University collects and uses your personal data to admit and enrol you, to teach and assess
you, to give you academic advice and support, to pay stipends, and to meet its legal reporting
duties. Data about your health or disability is collected only when you register for an
accommodation or use the counselling service, and is seen only by the staff who provide that
service. The University does not use your data for advertising. It may produce statistics that
do not identify you. It discloses your data to another body only where the law allows, and tells
you which bodies in this notice: the Ministry responsible for universities, and the stipend bank.
You may ask the data protection officer for a copy of your data, for a correction, or for
destruction of data that is no longer needed. Records are kept for five years after graduation.
"""

RELEASE_POLICY = """
# Student Success Unit: release policy for statistics (synthetic, the University's own rule)

1. No count of 1 to 9 students is released. Such a cell is suppressed and logged with its reason.
2. Where one suppressed cell could be recovered from a total, a second cell is suppressed.
3. Before release, every table is compared with tables already released on the same population.
4. A table with any suppressed cell is Restricted until the suppression has been checked by a
   second person; a checked table may be proposed as Public.
5. Every release has a version, a date, an approver and a line that says what the table must
   not be used for.

The threshold of 10 is this University's choice. No national instrument sets a number.
"""

REQUESTS = [
    {"id": "R1", "from": "Jassim Al-Nuaimi, director of the Student Success Unit",
     "text": "Before we extend Awn next term, tell me whether its referrals reach the students who end the term struggling. By college and level is enough.",
     "data_wanted": "attendance, midterm marks, referral flag and term outcome for all students",
     "leaves_the_university": False},
    {"id": "R2", "from": "Dr. Nabil Al-Faraj, dean of engineering",
     "text": "Send me the names of my referred students with their counselling visits and any disability, so department heads can have a word with them.",
     "data_wanted": "names, counselling visits and disability type of referred engineering students",
     "leaves_the_university": False},
    {"id": "R3", "from": "Hazza Al-Marri, Masarat Labour Market Observatory (a government body)",
     "text": "For our labour-market planning study we need your student records with identity numbers, so we can link them to employment records.",
     "data_wanted": "record-level student data with national identity numbers",
     "leaves_the_university": True},
    {"id": "R4", "from": "The communications office",
     "text": "A tutoring company will sponsor the open day. Give us the email addresses of students with a low grade average so we can send them its offer.",
     "data_wanted": "email addresses of students below a grade threshold",
     "leaves_the_university": False},
    {"id": "R5", "from": "A colleague in the unit",
     "text": "The registry extract is slow on my laptop. I will upload it to a free online notebook service hosted abroad and ask its AI assistant to summarise it.",
     "data_wanted": "the full registry extract, uploaded to a service outside the Kingdom",
     "leaves_the_university": True},
]

RULES = ["lawful basis", "purpose limitation", "minimisation", "sensitive data", "disclosure", "transfer",
         "marketing consent", "classification", "records of processing"]
KINDS = ["within the collection purpose", "new internal purpose", "disclosure to another entity", "transfer outside the Kingdom"]

REQUEST_KEY = {
    "R1": {"kind": "within the collection purpose", "rules": ["lawful basis", "purpose limitation", "minimisation", "records of processing"],
           "dpo": False, "why": "Evaluating the support service is academic support, the purpose in the notice. The analyst still cuts the fields and the unit records the processing."},
    "R2": {"kind": "new internal purpose", "rules": ["purpose limitation", "minimisation", "sensitive data"],
           "dpo": True, "why": "Health data collected for an accommodation or for counselling is seen only by the staff who provide that service. A dean's talk is a different purpose and needs none of it."},
    "R3": {"kind": "disclosure to another entity", "rules": ["lawful basis", "purpose limitation", "minimisation", "disclosure", "classification", "records of processing"],
           "dpo": True, "why": "A public entity asking for a public-interest purpose is a case the law allows, but it is a disclosure and a secondary use: minimum data, the Data Sharing Policy and a record."},
    "R4": {"kind": "new internal purpose", "rules": ["lawful basis", "purpose limitation", "marketing consent"],
           "dpo": True, "why": "Advertising needs the recipient's prior consent and the notice says the University does not use data for advertising. Refuse."},
    "R5": {"kind": "transfer outside the Kingdom", "rules": ["minimisation", "sensitive data", "transfer", "classification"],
           "dpo": True, "why": "Uploading is a transfer outside the Kingdom and puts Restricted data into an AI tool. Neither the purpose nor the level allows it."},
}

DATASETS = [
    {"id": "D1", "kind": "dataset", "name": "Student registry", "description": "30 columns for 18,000 students: identity, contact, programme, marks, attendance, disability type, counselling visits, bank account."},
    {"id": "D2", "kind": "dataset", "name": "Accommodation and counselling register", "description": "Disability type, medical evidence reference and counselling visit dates for students who used either service."},
    {"id": "D3", "kind": "dataset", "name": "Course catalogue and timetable", "description": "Courses, sections, rooms and times, as printed in the student guide and on the website."},
    {"id": "D4", "kind": "dataset", "name": "Pseudonymised analysis extract", "description": "13 columns per student under a project pseudonym: college, level, group fields, attendance, midterm mark, referral, outcome."},
    {"id": "O1", "kind": "output", "name": "Referral rate by college", "description": "Six rows: students, referred students and the referral rate of each college. The smallest count is in the hundreds."},
    {"id": "O2", "kind": "output", "name": "Draft table: disability by college and nationality group", "description": "Registered-disability counts by college and nationality group, before suppression. Several cells are under 10 and one is 1."},
    {"id": "O3", "kind": "output", "name": "Advisor worklist", "description": "Names, student numbers and programme of the students Awn referred this week, for the advisors who contact them."},
]
LEVELS = ["Top Secret", "Secret", "Restricted", "Public"]
CONTROLS = ["protective marking", "need-to-know access", "minimum staff access for health data", "encrypted storage",
            "secure sharing channel", "retention schedule", "second-person check before release",
            "approval by the data owner before release", "no control beyond accuracy"]
CLASSIFICATION_KEY = {
    "D1": {"level": "Restricted", "controls": ["protective marking", "need-to-know access", "encrypted storage", "retention schedule"], "ai_tool": False,
           "why": "Disclosure harms individuals' privacy (low impact) and would break the PDPL, so step 4 of the process makes it Restricted."},
    "D2": {"level": "Restricted", "controls": ["protective marking", "minimum staff access for health data", "encrypted storage", "retention schedule"], "ai_tool": False,
           "why": "Health data: Restricted, with access limited to the staff who provide the service."},
    "D3": {"level": "Public", "controls": ["no control beyond accuracy"], "ai_tool": True,
           "why": "Already published; disclosure has no impact."},
    "D4": {"level": "Restricted", "controls": ["protective marking", "need-to-know access", "encrypted storage", "retention schedule"], "ai_tool": False,
           "why": "Pseudonymised data is still personal data: the key exists and the rows are about single students."},
    "O1": {"level": "Public", "controls": ["approval by the data owner before release"], "ai_tool": True,
           "why": "Large counts, nobody singled out, a benefit in publishing. Public once the data owner approves the release; Restricted until then."},
    "O2": {"level": "Restricted", "controls": ["protective marking", "need-to-know access", "second-person check before release"], "ai_tool": False,
           "why": "A cell of 1 points at one student's health data. Restricted until suppressed and checked."},
    "O3": {"level": "Restricted", "controls": ["protective marking", "need-to-know access", "retention schedule"], "ai_tool": False,
           "why": "Named students: personal data for the advisors who act on it, and nobody else."},
}

PARTNER_REQUEST = {
    "requester": "Masarat Labour Market Observatory", "requester_kind": "government entity",
    "contact": "Hazza Al-Marri, partnerships liaison", "sent_to": "the analyst's own email address",
    "purpose": "Link study records to employment records to plan which programmes the labour market needs (public interest).",
    "population": "all 18,000 current students",
    "requested_fields": ["national_id", "full_name", "date_of_birth", "phone", "nationality", "college", "programme",
                         "level_year", "term_gpa", "disability_type", "awn_referred"],
    "delivery": "a spreadsheet attached to an email",
    "access": "the Observatory's analysts and its contractors",
    "onward_sharing": "a consulting firm that builds the Observatory's dashboards",
    "retention": "kept for future studies",
    "location": "the Observatory's servers in the Kingdom",
    "legal_basis_stated": "the Observatory's mandate to study the labour market",
}
SHARING_KEY = {
    "tests": {"legitimate purpose": "met", "minimum data": "not met", "source entity consent": "met with conditions"},
    "needed_fields": ["national_id", "college", "programme", "level_year", "term_gpa"],
    "population": "final-year students only",
    "form": "record level, minimised",
    "signatory": "director of the data management office",
    "assessment_days": 10,
}
CONTROL_HEADINGS = ["legal basis", "authorisation", "data type", "pre-processing", "sharing means",
                    "usage and protection", "duration and termination", "liability"]

BRIEFS = [
    {"id": "B1", "sponsor": "Dr. Nabil Al-Faraj, dean of engineering",
     "request": "Our first-year results are a disaster. I need the data on why engineering students are failing.",
     "hidden": {"decision": "whether to add tutorial sections to two first-year courses next term",
                "population": "first-year engineering students, this term and the last two",
                "measure": "share ending the term below 2.5, by course",
                "deadline": "the timetable is fixed in three weeks",
                "out_of_scope": "naming students or instructors"}},
    {"id": "B2", "sponsor": "Jassim Al-Nuaimi, director of the Student Success Unit",
     "request": "Is Awn working? The vice-rector will ask me next month.",
     "hidden": {"decision": "whether to extend Awn to all colleges or change its thresholds first",
                "population": "all students this term",
                "measure": "share of struggling students Awn referred, and share of referrals that were not needed, by group",
                "deadline": "one page before the council meets in four weeks",
                "out_of_scope": "whether the support itself helps: there is no comparison group"}},
    {"id": "B3", "sponsor": "The communications office",
     "request": "We want a nice number about student success for the annual report.",
     "hidden": {"decision": "which single figure the annual report prints, with its definition",
                "population": "students enrolled in both terms of last year",
                "measure": "share who ended the year in good standing, with last year's figure beside it",
                "deadline": "the report goes to print in two weeks",
                "out_of_scope": "figures by nationality or disability with small counts"}},
]
SCOPE_FIELDS = ["decision", "question", "population", "measure", "success_criterion", "out_of_scope", "data", "deadline", "confirmed_by"]

RISK_LIST_REQUEST = {
    "sponsor": "Dr. Ibtisam Al-Khayyat, vice-rector for academic affairs",
    "request": "Give me a list of every student likely to fail this year, with names and a risk score. I want it on my desk and with the deans by Sunday.",
    "what_she_wants_to_decide": "where to put twelve new advisors and whether the colleges are acting on referrals",
    "why_it_is_unsafe": ["a named list of predicted failure is a new purpose and reaches people who do not advise the student",
                         "the score is wrong for known groups: false referrals for students with a remote accommodation, misses for bridging-year entrants",
                         "a label that travels to deans can follow a student into grading and discipline"],
    "pressures": ["the council meets on Monday", "another university does this already", "I am the vice-rector, I am allowed to see student data"],
}
ALTERNATIVES = [
    {"id": "A1", "title": "Counts for the vice-rector", "what": "Referred and struggling students by college and level, with suppression, to place the twelve advisors.", "serves_decision": True, "names_leave_advising": False},
    {"id": "A2", "title": "Worklists stay with advisors", "what": "Each advisor keeps the named worklist of their own students, as today; the vice-rector sees how many were contacted within two weeks.", "serves_decision": True, "names_leave_advising": False},
    {"id": "A3", "title": "The full named list, marked confidential", "what": "Send the list as asked, with a confidentiality marking.", "serves_decision": True, "names_leave_advising": True},
    {"id": "A4", "title": "Nothing until legal review", "what": "Decline and wait for a legal opinion.", "serves_decision": False, "names_leave_advising": False},
]
OBSERVER_RUBRIC = [
    {"id": "listen", "text": "Asked what decision the sponsor has to make before proposing anything"},
    {"id": "harm", "text": "Named the harm to students in plain words, not only a rule"},
    {"id": "rule", "text": "Named the rule or the role that decides (the notice, the law, the data protection officer)"},
    {"id": "alternative", "text": "Offered an alternative that serves the sponsor's decision"},
    {"id": "record", "text": "Said what will be written down and who confirms it"},
]

AUDIT_QUESTIONS = [
    "Which file and which version produced the referral table released in November?",
    "Who approved the use of disability status in the group comparison, and on what condition?",
    "Why are bridging-year entrants reported separately?",
    "What must the group comparison not be used for?",
    "How many cells were suppressed in the release, and who checked the suppression?",
]

DATASHEET_TEMPLATE = """
# Datasheet: {name}

## 1. Motivation
Why was this dataset made, for whom, and for which decision?

## 2. Composition
What is one row? How many rows? Which fields? Which fields are personal or sensitive? What is missing, and for whom?

## 3. Collection
Where does each field come from? How was it recorded? What is known to be recorded badly?

## 4. Preprocessing
What was dropped, coarsened or pseudonymised, and where is the raw data kept?

## 5. Uses
What is the approved use? What must it not be used for?

## 6. Distribution
Who may see it? What is its classification level? May it leave the University?

## 7. Maintenance
Who owns it? Until when is it kept? How is an error reported?
"""

LOG_SEED = [
    {"id": "L001", "date": "2026-11-02", "decision": "Evaluate Awn on a pseudonymised extract of 13 fields; names, contacts, identity numbers, addresses, bank accounts and free-text notes are not extracted.",
     "reason": "The purpose needs none of them.", "approver": "Rami Al-Tuwaijri, registrar (data owner)", "evidence": "minimisation log, Lab 1.2"},
    {"id": "L002", "date": "2026-11-04", "decision": "Include gender, nationality group, disability status and remote accommodation in the extract for the group comparison.",
     "reason": "Error rates by group cannot be checked without them. Disability status is health data, so the comparison runs only on the pseudonymised extract inside the unit and is reported in aggregate.",
     "approver": "Shatha Al-Omair, data protection officer", "evidence": "email of 2026-11-04, filed with the record of processing"},
]

LIMITS_RESULT = {
    "claim": "",
    "misreadings": [
        {"id": "M1", "text": "Awn causes students to pass.", "blocked_by": "a sentence that says the analysis did not test whether support helps"},
        {"id": "M2", "text": "A student Awn did not refer is safe.", "blocked_by": "the share of struggling students that Awn missed"},
        {"id": "M3", "text": "The rule works equally well for every group.", "blocked_by": "naming the groups for which it is known to be worse"},
        {"id": "M4", "text": "The list of referred students can be used to decide who repeats a course.", "blocked_by": "a sentence that says what the result must not be used for"},
    ],
}


PIPELINE = [
    {"id": "S1", "stage": "attendance recording", "what_happens": "A student's card is read at the door of a teaching room. Sessions followed remotely under an approved accommodation have no card reading."},
    {"id": "S2", "stage": "midterm marks", "what_happens": "Instructors enter midterm marks in the registry. Bridging-year entrants are marked in the bridging programme's own system for their first two years, and those marks are not copied over."},
    {"id": "S3", "stage": "thresholds", "what_happens": "The limits of 75% attendance and 2.5 were set in 2023 from one year of records of two colleges, Business and Engineering."},
    {"id": "S4", "stage": "outcome label", "what_happens": "'Struggled' means a term grade average below 2.5. A student who withdraws during the term keeps the average of the courses completed."},
    {"id": "S5", "stage": "referral and support", "what_happens": "An advisor contacts each referred student. Students who are helped may pass, and then count as referrals that were 'not needed'."},
    {"id": "S6", "stage": "reporting", "what_happens": "The unit reports one referral rate and one hit rate for the whole University each term."},
]

BIAS_TYPES = [
    {"type": "measurement bias", "in_short": "The recorded values are systematically too high or too low compared with the true ones, because of how the data is collected or recorded."},
    {"type": "coverage bias", "in_short": "The data does not adequately represent part of the population, so results are worse for those who are under-represented."},
    {"type": "historical bias", "in_short": "The data carries assumptions, standards or circumstances of the past that no longer fit the present."},
    {"type": "sampling bias", "in_short": "The data selected does not representatively capture the full range of the domain."},
    {"type": "aggregation bias", "in_short": "Groups that differ are combined as if they were alike, so the result fits the largest group and overlooks smaller ones."},
    {"type": "labeling bias", "in_short": "The labels reflect the subjective judgement of the people who assigned them."},
    {"type": "detection bias", "in_short": "Outcomes are identified or verified with different methods or intensity for different groups."},
    {"type": "feedback loop bias", "in_short": "A system's outputs come back as its future inputs, so an early skew is preserved or magnified."},
    {"type": "exclusion bias", "in_short": "Important information was removed or left out of the data, leaving blind spots."},
    {"type": "automation bias", "in_short": "People favour the output of an automated system over their own judgement or other evidence."},
]


# --------------------------------------------------------------------------- capstone engagements

ENGAGEMENTS = {
    "scholarships": {
        "title": "Scholarship Office: the award review rule",
        "unit": "Scholarship Office", "rule_name": "the review flag",
        "rule": "An award is flagged for review when the term grade average is below 3.0 or the recorded study load is below 12 credit hours.",
        "flag": "flagged_for_review", "outcome": "award_withdrawn", "x1": "term_gpa", "x2": "credit_hours",
        "bias_group": "disability_status", "bias_note": "students with a reduced-load accommodation are recorded below 12 credit hours although their load is approved",
        "partner": {"requester": "Al-Ata Charitable Foundation", "requester_kind": "non-government entity (a charity that co-funds awards)",
                    "purpose": "Report to its donors how the students it funds are doing.",
                    "requested_fields": ["full_name", "national_id", "phone", "college", "term_gpa", "disability_status", "family_income_band", "flagged_for_review"],
                    "delivery": "a shared online folder", "retention": "for as long as the Foundation exists", "onward_sharing": "the Foundation's donors, by name",
                    "location": "a cloud folder whose region is not stated"},
        "brief": "The vice-rector for student affairs: \"Tell me which scholarship students do not deserve their award, so we can free the money before next term.\"",
    },
    "housing": {
        "title": "Student Housing: the room priority rule",
        "unit": "Student Housing Office", "rule_name": "the priority score",
        "rule": "A student gets priority for a campus room when the recorded home distance is above 150 km or the family income band is the lowest.",
        "flag": "priority_given", "outcome": "needed_room", "x1": "home_distance_km", "x2": "income_band_low",
        "bias_group": "nationality_group", "bias_note": "non-Saudi students have no home address in the Kingdom on file, so the distance is recorded as 0",
        "partner": {"requester": "Al-Qimam City Municipality", "requester_kind": "government entity",
                    "purpose": "Plan bus routes between student districts and the campus (public interest).",
                    "requested_fields": ["full_name", "national_id", "home_address", "phone", "college", "gender", "priority_given"],
                    "delivery": "a spreadsheet by email", "retention": "not stated", "onward_sharing": "the bus operator",
                    "location": "the municipality's servers in the Kingdom"},
        "brief": "The director of student housing: \"We have 300 complaints about room allocation. Prove the priority rule is fair.\"",
    },
    "careers": {
        "title": "Career Centre: the internship shortlist rule",
        "unit": "Career Centre", "rule_name": "the shortlist rule",
        "rule": "A student is shortlisted for an internship interview when the grade average is at least 3.75 or the student attended at least three career workshops.",
        "flag": "shortlisted", "outcome": "ready_for_internship", "x1": "gpa", "x2": "workshops_attended",
        "bias_group": "gender", "bias_note": "workshops ran in a building and at an hour that one campus section could not reach, so attendance is recorded low for it",
        "partner": {"requester": "The Regional Employers' Council", "requester_kind": "non-government entity (a private-sector association)",
                    "purpose": "Let member companies contact promising students directly.",
                    "requested_fields": ["full_name", "phone", "email", "national_id", "college", "gpa", "disability_status", "shortlisted"],
                    "delivery": "an upload to the Council's recruiting platform", "retention": "until the student unsubscribes", "onward_sharing": "all member companies",
                    "location": "a platform hosted outside the Kingdom"},
        "brief": "The dean of business: \"Send me the names of the students who were not shortlisted, with the reason, so their departments can push them.\"",
    },
}


def make_engagement(key: str, spec: dict, rng: random.Random) -> None:
    folder = CAP / key
    rows = []
    for i in range(4000):
        college = rng.choices(list(COLLEGES), weights=[v[0] for v in COLLEGES.values()])[0]
        gender = "F" if rng.random() < COLLEGES[college][1] else "M"
        saudi = rng.random() >= 0.11
        registered = rng.random() < 0.03
        u = rng.gauss(0, 1)
        need = u > 0.55                      # the outcome the rule is meant to find
        x1_good = u + rng.gauss(0, 0.7) > 0.55
        x2_good = u + rng.gauss(0, 0.9) > 0.9
        group_value = {"disability_status": registered, "nationality_group": not saudi, "gender": gender == "F"}[spec["bias_group"]]
        if key == "scholarships":
            gpa = clip(3.5 - 0.7 * u + rng.gauss(0, 0.4), 0, 5)
            hours = rng.choice([12, 15, 15, 18]) if not (group_value and rng.random() < 0.55) else rng.choice([6, 9])
            flag = gpa < 3.0 or hours < 12
            outcome = gpa < 2.6 and rng.random() < 0.8
            extra = {"term_gpa": f"{gpa:.2f}", "credit_hours": hours, "family_income_band": rng.choice(["low", "middle", "middle", "high"])}
        elif key == "housing":
            dist = 0 if (group_value and rng.random() < 0.8) else int(abs(rng.gauss(140 + 120 * (1 if need else 0), 90)))
            low = rng.random() < (0.45 if need else 0.15)
            flag = dist > 150 or low
            outcome = need
            extra = {"home_distance_km": dist, "income_band_low": "yes" if low else "no"}
        else:
            gpa = clip(3.4 + 0.6 * u + rng.gauss(0, 0.35), 0, 5)
            shops = max(0, int(rng.gauss(2.2 + 0.8 * u, 1.2)) - (2 if (group_value and rng.random() < 0.7) else 0))
            flag = gpa >= 3.75 or shops >= 3
            outcome = u + rng.gauss(0, 0.5) > 0.4
            extra = {"gpa": f"{gpa:.2f}", "workshops_attended": shops}
        first = rng.choice(F_NAMES if gender == "F" else M_NAMES)
        rows.append({"record_id": f"{key[:2].upper()}{i + 1:05d}", "full_name": f"{first} {rng.choice(FAMILIES)}",
                     "national_id": ("1" if saudi else "2") + f"{rng.randrange(10**9):09d}",
                     "phone": "05" + f"{rng.randrange(10**8):08d}", "email": f"{key[:2]}{i + 1:05d}@students.qimam.example",
                     "home_address": f"Building {rng.randint(1, 60)}, Street {rng.randint(1, 40)}, {rng.choice(DISTRICTS)}",
                     "gender": gender, "nationality_group": "Saudi" if saudi else "non-Saudi", "college": college,
                     "disability_status": "registered" if registered else "none", **extra,
                     spec["flag"]: "yes" if flag else "no", spec["outcome"]: "yes" if outcome else "no"})
    write_csv(folder / "records.csv", rows, list(rows[0].keys()))
    write_json(folder / "partner_request.json", spec["partner"])
    write_text(folder / "brief.md", f"""
# {spec['title']}

**Unit.** {spec['unit']}, Al-Qimam University (fictional). 4,000 synthetic records in `records.csv`.

**The rule.** {spec['rule']} The flag is the column `{spec['flag']}`; the outcome the rule is meant
to find is the column `{spec['outcome']}`.

**The sponsor's request.** {spec['brief']}

**The partner's request.** In `partner_request.json`.

**Known about the data.** Ask the trainer only after your own group comparison: something in the
way one field is recorded differs for one group.
""")


def make_capstone(rng: random.Random) -> dict:
    notes = {}
    for key, spec in ENGAGEMENTS.items():
        make_engagement(key, spec, rng)
        notes[key] = {"bias_group": spec["bias_group"], "bias_note": spec["bias_note"]}
    write_text(CAP / "README.md", """
# Capstone: the responsible-practice pack

Choose one engagement. Each folder holds `brief.md`, `records.csv` (4,000 synthetic records) and
`partner_request.json`.

| Folder | Engagement | Partner |
|---|---|---|
| `scholarships/` | Scholarship Office: the award review rule | a charity that co-funds awards |
| `housing/` | Student Housing: the room priority rule | the city's municipality |
| `careers/` | Career Centre: the internship shortlist rule | a private employers' council |

## What the pack contains

Copy `pack_template/` into a new public repository and fill each file.

| File | Contents | Rubric criterion |
|---|---|---|
| `01_sharing_decision.md` | The rules the partner's request engages, the classification of what is asked for, the decision, the form of release and the conditions, who signs | Legal and classification decisions, 25 |
| `02_release_tables/` | Two tables ready for release, with `suppression_log.csv` and the result of your differencing check | Release tables and suppression, 20 |
| `03_group_comparison.md` | Flag rate, false-flag rate and missed rate by group with intervals; two candidate bias types for the largest gap and the check that separates them | Group comparison, 20 |
| `04_datasheet.md` and `05_analysis_log.md` | The datasheet, and a log in which every decision has a reason, a date and an approver | Documentation, 20 |
| `06_scope_note.md` | The sponsor's request rescoped into a lawful, answerable question, and what the analysis must not be used for | Scope note, 15 |

## The defence

Eight minutes: six on the pack, including a two-minute role-play in which a peer plays the
sponsor of your brief, and two in which the assessor changes one fact of the partner's request
and you revise the sharing decision aloud.

AI policy: an assistant may help you draft the documents. You defend every sentence live, and
the role-play is yours alone.
""")
    for name, text in {
        "01_sharing_decision.md": "# Sharing decision\n\n## The request\n\n## Rules engaged\n\n## Classification of what is asked for\n\n## Decision and form of release\n\n## Conditions (eight headings)\n\n## Who signs, and by when",
        "02_release_tables/README.md": "# Release tables\n\nTwo tables, the suppression log and the differencing check. State the threshold and who checked the suppression.",
        "03_group_comparison.md": "# Group comparison\n\n## Rates with intervals\n\n## The largest gap\n\n## Two candidate bias types and the check that separates them\n\n## What stays open",
        "04_datasheet.md": DATASHEET_TEMPLATE.format(name="(the engagement's records)"),
        "05_analysis_log.md": "# Analysis log\n\n| Id | Date | Decision | Reason | Approver | Evidence |\n|---|---|---|---|---|---|",
        "06_scope_note.md": "# Scope note\n\n" + "\n".join(f"- **{f.replace('_', ' ').capitalize()}:**" for f in SCOPE_FIELDS) + "\n\n## Must not be used for",
        "README.md": "# Responsible-practice pack\n\nEngagement: \n\nLinks to each part, who approved each release, and what the analysis must not be used for.",
    }.items():
        write_text(CAP / "pack_template" / name, text)
    return notes


# --------------------------------------------------------------------------- main

def main() -> None:
    rng = random.Random(SEED)
    rows, truth = make_students(rng)
    plant_small_cells(rows, rng)
    note_counts = plant_notes(rows, rng)
    write_csv(DATA / "students.csv", rows, COLUMNS)
    extract = analysis_extract(rows)
    write_csv(DATA / "analysis_extract.csv", extract, list(extract[0].keys()))
    audit = roll_call_audit(rows, truth, random.Random(SEED + 1))
    write_csv(DATA / "roll_call_audit.csv", audit, ["pid", "roll_call_rate"])
    write_csv(DATA / "release_2026_10_disability_by_college.csv", previous_release(rows),
              ["college", "registered_disability_all_students"])
    write_text(DATA / "privacy_notice.md", PRIVACY_NOTICE)
    write_text(DATA / "release_policy.md", RELEASE_POLICY)
    write_json(DATA / "requests.json", {"requests": REQUESTS, "rules": RULES, "kinds": KINDS})
    write_json(DATA / "datasets.json", {"items": DATASETS, "levels": LEVELS, "controls": CONTROLS})
    write_json(DATA / "partner_request.json", PARTNER_REQUEST)
    write_json(DATA / "control_headings.json", CONTROL_HEADINGS)
    write_json(DATA / "sponsor_briefs.json", {"briefs": [{k: v for k, v in b.items()} for b in BRIEFS], "scope_fields": SCOPE_FIELDS})
    write_json(DATA / "risk_list_request.json", {"request": RISK_LIST_REQUEST, "alternatives": ALTERNATIVES, "observer_rubric": OBSERVER_RUBRIC})
    write_json(DATA / "audit_questions.json", AUDIT_QUESTIONS)
    write_text(DATA / "datasheet_template.md", DATASHEET_TEMPLATE.format(name="(name of the dataset)"))
    write_json(DATA / "analysis_log_seed.json", LOG_SEED)
    struggled = [r for r in rows if r["term_outcome"] == "struggled"]
    caught = sum(r["awn_referred"] == "yes" for r in struggled)
    LIMITS_RESULT["claim"] = f"Awn referred {round(100 * caught / len(struggled))}% of the students who ended the term struggling ({caught} of {len(struggled)})."
    write_json(DATA / "limits_result.json", LIMITS_RESULT)
    write_json(DATA / "awn_pipeline.json", PIPELINE)
    write_json(DATA / "bias_types.json", BIAS_TYPES)
    cap_notes = make_capstone(random.Random(SEED + 2))
    write_json(HERE / "solutions" / "keys.json", {
        "requests": REQUEST_KEY, "classification": CLASSIFICATION_KEY, "sharing": SHARING_KEY,
        "note_counts": note_counts, "capstone": cap_notes})
    print(f"students: {len(rows)}  notes: {note_counts}")
    print("referred:", sum(r["awn_referred"] == "yes" for r in rows), " struggled:", sum(r["term_outcome"] == "struggled" for r in rows))


if __name__ == "__main__":
    main()
