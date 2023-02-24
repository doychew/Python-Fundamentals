employee_efficiency = int(input())
employee1_efficiency = int(input())
employee2_efficiency = int(input())
students_count = int(input())
hour = 0

answers_per_hour = employee_efficiency + employee1_efficiency + employee2_efficiency
while students_count > 0:
    students_count -= answers_per_hour
    hour += 1
    if hour % 4 == 0:
        hour += 1
print(f"Time needed: {hour}h.")

