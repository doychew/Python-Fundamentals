number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
from math import ceil
max_attendances = 0
for i in range(number_of_students):
    attendances = int(input())
    max_attendances = max(attendances, max_attendances)
total_bonus = 0

if number_of_lectures != 0:
    total_bonus = (max_attendances / number_of_lectures) * (5 + additional_bonus)
print(f"Max Bonus: {ceil(total_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")
