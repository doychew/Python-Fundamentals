n = int(input())
students = {}
for _ in range(n):
    data = input()
    splittet_data = data.split()
    student_name = splittet_data[0]
    grade = float(splittet_data[1])
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(grade)
for name, grades in students.items():
    formatted_grades = ' '.join([f"{grade:.2f}" for grade in grades])
    print(f"{name} -> {formatted_grades}"
          f" (avg: {sum(grades) / len(grades):.2f})")
