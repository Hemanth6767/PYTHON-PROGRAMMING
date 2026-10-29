
# University Scholarship Allocation System

MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 60
MIN_ATTENDANCE = 85
MAX_INCOME = 300000


def check_eligibility(student):
    reasons = []

    if student["aggregate"] < MIN_AGGREGATE:
        reasons.append("Aggregate marks below 75%")

    if min(student["subjects"]) < MIN_SUBJECT_MARK:
        reasons.append("Subject marks below 60%")

    if student["attendance"] < MIN_ATTENDANCE:
        reasons.append("Attendance below 85%")

    if student["income"] > MAX_INCOME:
        reasons.append("Family income exceeds Rs. 3,00,000")

    return reasons


students = []
eligible_students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details of Student {i + 1}")

    name = input("Student name: ")
    subjects = list(map(
        float,
        input("Enter subject marks separated by spaces: ").split()
    ))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    if not subjects or any(mark < 0 or mark > 100 for mark in subjects):
        print("Invalid subject marks. Enter marks between 0 and 100.")
        continue

    student = {
        "name": name,
        "subjects": subjects,
        "aggregate": sum(subjects) / len(subjects),
        "attendance": attendance,
        "income": income
    }

    if not 0 <= attendance <= 100 or income < 0:
        print("Invalid attendance or income.")
        continue

    reasons = check_eligibility(student)
    student["reasons"] = reasons
    students.append(student)

    if not reasons:
        eligible_students.append(student)


# Ranking and tie-breaking rules
eligible_students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        -min(s["subjects"]),
        s["name"].lower()
    )
)

print("\n========== SCHOLARSHIP RESULTS ==========")

if eligible_students:
    print("\nEligible Students - Merit Ranking")
    print("Rank  Name       Aggregate  Attendance  Income")

    for rank, student in enumerate(eligible_students, start=1):
        print(
            f"{rank:<6}{student['name']:<11}"
            f"{student['aggregate']:<11.2f}"
            f"{student['attendance']:<12.1f}"
            f"Rs.{student['income']:.0f}"
        )
else:
    print("\nNo eligible students found.")

print("\nNot Eligible Students")

for student in students:
    if student["reasons"]:
        print(
            f"{student['name']}: "
            + ", ".join(student["reasons"])
        )

