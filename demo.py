data = input()
courses = {}
while ":" in data:
    student_name, id, course_name = data.split(":")
    if course_name not in courses:
        courses[course_name] = {id: student_name}
    else:
        courses[course_name][id] = student_name
    data = input()
course_name = " ".join(data.split("_"))
students = courses[course_name]
for id, name in students.items():
    print(f"{name} - {id}")