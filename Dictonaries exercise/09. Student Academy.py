student_grades = {}

counter = 0
rows = int(input())
for i in range(0, rows):
    name = input()
    grade = float(input())
    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

for student, grade in student_grades.items():
    avg_grade = sum(grade) / len(grade)
    if avg_grade < 4.50:
        continue
    else:
        print(f"{student} -> {avg_grade:.2f}")


