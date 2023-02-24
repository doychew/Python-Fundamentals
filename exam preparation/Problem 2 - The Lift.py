people_waiting = int(input())
state_of_the_lift = [int(x) for x in input().split()]
max_people = 4 * len(state_of_the_lift)
for current_wagon in range(len(state_of_the_lift)):
    if people_waiting < 4:
        state_of_the_lift[current_wagon] += people_waiting
        people_waiting -= people_waiting
        break
    if state_of_the_lift[current_wagon] == 0:
        state_of_the_lift[current_wagon] += 4
        people_waiting -= 4
    else:
        people_to_add = 4 - state_of_the_lift[current_wagon]
        state_of_the_lift[current_wagon] += people_to_add

        people_waiting -= people_to_add

    if people_waiting <= 0:
        break
if people_waiting <= 0 and max_people > sum(state_of_the_lift):
    print(f"The lift has empty spots!")
    print(' '.join([str(x) for x in state_of_the_lift]))
elif people_waiting > 0 and max_people == sum(state_of_the_lift):
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(' '.join([str(x) for x in state_of_the_lift]))
elif max_people == sum(state_of_the_lift) and people_waiting == 0:
    print(' '.join([str(x) for x in state_of_the_lift]))


