from collections import deque

darth_vader_ducky_counter = 0
thor_ducky_counter = 0
big_blue_rubbed_ducky_counter = 0
small_yellow_rubber_ducky_counter = 0

needed_time = deque([int(x) for x in input().split()])
number_of_task = ([int(x) for x in input().split()])

while needed_time and number_of_task:
    calculated_time = 0
    current_time = needed_time.popleft()
    current_task = number_of_task.pop()
    calculated_time = current_time * current_task
    if 0 <= calculated_time <= 60:
        darth_vader_ducky_counter += 1
    elif 61 <= calculated_time <= 120:
        thor_ducky_counter += 1
    elif 121 <= calculated_time <= 180:
        big_blue_rubbed_ducky_counter += 1
    elif 181 <= calculated_time <= 240:
        small_yellow_rubber_ducky_counter += 1
    if calculated_time > 240:
        needed_time.append(current_time)
        current_task -= 2
        number_of_task.append(current_task)
print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {darth_vader_ducky_counter}")
print(f"Thor Ducky: {thor_ducky_counter}")
print(f"Big Blue Rubber Ducky: {big_blue_rubbed_ducky_counter}")
print(f"Small Yellow Rubber Ducky: {small_yellow_rubber_ducky_counter}")

