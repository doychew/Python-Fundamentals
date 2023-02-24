needed_experience = float(input())
count_of_battles = int(input())
total_xp = 0
battle_counter = 0
xp_gained = False
for battle in range(1, count_of_battles + 1):
    battle_counter += 1
    experience_per_battle = float(input())
    total_xp += experience_per_battle
    if battle % 3 == 0:
        total_xp = total_xp + experience_per_battle * 0.15
    if battle % 5 == 0:
        total_xp = total_xp - experience_per_battle * 0.1
    if battle % 15 == 0:
        total_xp = total_xp + experience_per_battle * 0.05
    if total_xp >= needed_experience:
        xp_gained = True
        break

if xp_gained:
    print(f"Player successfully collected his needed experience for {battle_counter} battles.")
else:
    print(f"Player was not able to collect the needed experience, {needed_experience - total_xp:.2f} more needed.")



