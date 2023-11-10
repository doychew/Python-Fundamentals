number_of_rooms = int(input())
total_free_chairs = 0
total_needed_chairs = 0
for room in range(1, number_of_rooms + 1):
    free_chairs, visitors = input().split()
    difference = len(free_chairs) - int(visitors)
    if difference >= 0:
        total_free_chairs += difference
    else:
        total_needed_chairs += abs(difference)
        print(f"{abs(difference)} more chairs needed in room {room}")
if total_free_chairs >= total_needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")