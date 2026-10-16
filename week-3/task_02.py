
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
    total = 0

    for student in students:
        total = total + student["score"]

    if len(students) == 0:
        return 0

    return total / len(students)


def find_highest_score(students):
    highest = students[0]["score"]

    for student in students:
        if student["score"] > highest:
            highest = student["score"]

    return highest


def find_lowest_score(students):
    lowest = students[0]["score"]

    for student in students:
        if student["score"] < lowest:
            lowest = student["score"]

    return lowest


def count_passed(students):
    passed = 0

    for student in students:
        if student["score"] >= 50:
            passed = passed + 1

    return passed


def count_failed(students):
    failed = 0

    for student in students:
        if student["score"] < 50:
            failed = failed + 1

    return failed


def find_above_average(students, average):
    above_average = []

    for student in students:
        if student["score"] > average:
            above_average.append(student)

    return above_average


def generate_report(students):
    # Validate all scores first
    for student in students:
        if not validate_score(student["score"]):
            print("Invalid score for", student["name"])
            return

    # Calculate class results
    average = calculate_average(students)

    print("===== STUDENT PERFORMANCE REPORT =====")

    for student in students:
        grade = calculate_grade(student["score"])

        if student["score"] >= 50:
            status = "Pass"
        else:
            status = "Fail"

        print(
            student["name"],
            "| Score:", student["score"],
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
        print(student["name"], "-", student["score"])


# Example student data
students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]

generate_report(students)
