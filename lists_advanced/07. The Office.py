employees_happiness = input().split()
factor = int(input())
avg_score = 0
score = 0
current_happiness = []
counter = 0
for employee in employees_happiness:
    current_happiness.append(int(employee) * factor)
    score += int(employee) * factor
avg_score = score / len(employees_happiness)
for every_employee in current_happiness:
    if every_employee >= avg_score:
        counter += 1
if counter >= len(employees_happiness) / 2:
    print(f"Score: {counter}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {counter}/{len(employees_happiness)}. Employees are not happy!")




