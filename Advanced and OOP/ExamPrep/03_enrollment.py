def gather_credits(number_of_credits, *course_info):
    courses = []
    collected_credits = 0
    total_credits = int(number_of_credits)
    for course_information in course_info:
        if collected_credits >= number_of_credits:
            break
        course_name = course_information[0]
        course_credits = int(course_information[1])
        if course_name in courses:
            continue
        courses.append(course_name)
        total_credits -= course_credits
        collected_credits += course_credits

    if collected_credits >= number_of_credits:
        return f"""Enrollment finished! Maximum credits: {collected_credits}.
Courses: {', '.join(sorted(courses))}"""
    return f"You need to enroll in more courses! You have to gather {total_credits} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))
