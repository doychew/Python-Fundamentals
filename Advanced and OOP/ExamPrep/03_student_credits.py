def students_credits(*args):
    student_information = dict()
    percentage_points = 0
    credits_recieved = 0
    final_strings = []
    total_credits = 0
    for info in args:
        course_name, credits, max_test_points, diyan_points = info.split("-")
        if course_name not in student_information:
            student_information[course_name] = 0
            percentage_points = int(diyan_points) / int(max_test_points)
            credits_recieved = int(credits) * percentage_points
            total_credits += credits_recieved
            student_information[course_name] = credits_recieved
    # sorted_dict = sorted(student_information, key=lambda x: x[-1])
    if total_credits >= 240:
        final_strings.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
         final_strings.append(f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.")

    for name, credit in sorted(student_information.items(), key=lambda a: -a[1]):
        final_strings.append(f"{name} - {credit}")
    return "\n".join(final_strings)


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

