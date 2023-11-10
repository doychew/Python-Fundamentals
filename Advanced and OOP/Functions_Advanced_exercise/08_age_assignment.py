def age_assignment(*args, **kwargs):
    people = {}
    for name in args:
        people[name] = kwargs[name[0]]
    result = sorted(people.items(), key=lambda x: x[0])
    final_result = []
    for name, age in result:
        final_result.append(f"{name} is {age} years old.")
    return "\n".join(final_result)
