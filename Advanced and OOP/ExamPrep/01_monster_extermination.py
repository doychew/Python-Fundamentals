from collections import deque
armor_of_monsters = deque([int(x) for x in input().split(",")])
soldiers_damage = [int(x) for x in input().split(",")]
killed_monsters = 0
while armor_of_monsters and soldiers_damage:

    current_armor_monster = armor_of_monsters.popleft()
    current_soldier_damage = soldiers_damage.pop()
    if current_soldier_damage >= current_armor_monster:
        current_soldier_damage -= current_armor_monster
        killed_monsters += 1
        if not soldiers_damage:
            if current_soldier_damage > 0:
                soldiers_damage.append(current_soldier_damage)
        else:
            soldiers_damage[-1] += current_soldier_damage
    else:
        current_armor_monster -= current_soldier_damage
        armor_of_monsters.append(current_armor_monster)

if len(armor_of_monsters) == 0:
    print("All monsters have been killed!")
if len(soldiers_damage) == 0:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")







