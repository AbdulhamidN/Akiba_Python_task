student_name = input("Enter student name: ")
python_score = float(input("Enter Python score: "))
english_score = float(input("Enter English score: "))
mathematics_score = float(input("Enter Mathematics score: "))

average = (python_score + english_score + mathematics_score) / 3

print("========================================")
print("           STUDENT RESULT")
print("========================================")
print()
print("Student:", student_name)
print()
print("Python:", python_score)
print("English:", english_score)
print("Mathematics:", mathematics_score)
print("----------------------------------------")
print("Average:", average)
print("========================================")