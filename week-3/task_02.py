
def validate_score(score):
    if score < 0 or score > 100:
        return False
    return True


def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def calculate_average(students):
    if len(students) == 0:
        return 0

    total = 0

    for student in students:
        total = total + student[1]

    return total / len(students)


def find_highest_score(students):
    highest = students[0][1]

    for student in students:
        if student[1] > highest:
            highest = student[1]

    return highest


def find_lowest_score(students):
    lowest = students[0][1]

    for student in students:
        if student[1] < lowest:
            lowest = student[1]

    return lowest


def count_passed(students):
    passed = 0

    for student in students:
        if student[1] >= 50:
            passed = passed + 1

    return passed


def count_failed(students):
    failed = 0

    for student in students:
        if student[1] < 50:
            failed = failed + 1

    return failed


def find_above_average(students, average):
    above_average = []

    for student in students:
        if student[1] > average:
            above_average.append(student)

    return above_average


def generate_report(students):
    # Validate all scores first
    for student in students:
        if not validate_score(student[1]):
            print("Invalid score for", student[0])
            return

    # Calculate class results
    average = calculate_average(students)

    print("===== STUDENT PERFORMANCE REPORT =====")

    for student in students:
        name = student[0]
        score = student[1]
        grade = calculate_grade(score)

        if score >= 50:
            status = "Pass"
        else:
            status = "Fail"

        print(
            name,
            "| Score:", score,
            "| Grade:", grade,
            "| Status:", status
        )

    print("--------------------------------------")
    print("Class Average:", round(average, 2))

    if len(students) > 0:
        print("Highest Score:", find_highest_score(students))
        print("Lowest Score:", find_lowest_score(students))

    print("Students Passed:", count_passed(students))
    print("Students Failed:", count_failed(students))

    print("Students Above Class Average:")

    above_average = find_above_average(students, average)

    for student in above_average:
        print(student[0], "-", student[1])


# Student data: each tuple contains (name, score)
students = [
    ("Sara", 85),
    ("Ahmed", 42),
    ("Musa", 93),
    ("Hana", 67)
]

generate_report(students)
