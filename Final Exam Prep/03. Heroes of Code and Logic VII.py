number_of_heroes = int(input())
heroes = {}
hp = 100
mp = 200
for i in range(number_of_heroes):
    hero, health, mana = input().split()
    heroes[hero] = {'health': health, 'mana': mana}
while True:
    data = input()
    if data == "End":
        break
    splitted_data = data.split(" - ")
    command = splitted_data[0]
    if command == "CastSpell":
        hero = splitted_data[1]
        mana_needed = int(splitted_data[2])
        spell_name = splitted_data[3]
        spell_cast = int(heroes[hero]['mana'])
        if spell_cast >= mana_needed:
            spell_cast -= mana_needed
            heroes[hero]['mana'] = spell_cast
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['mana']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        hero = splitted_data[1]
        damage = int(splitted_data[2])
        attacker = splitted_data[3]
        damage_taken = int(heroes[hero]['health'])
        damage_taken -= damage
        (heroes[hero]['health']) = damage_taken
        if damage_taken > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {(heroes[hero]['health'])} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            del heroes[hero]

    elif command == "Recharge":
        hero = splitted_data[1]
        amount = int(splitted_data[2])
        mana_recharge = int(heroes[hero]['mana'])

        if mana_recharge + amount > mp:
            print(f"{hero} recharged for {mp - mana_recharge} MP!")
            mana_recharge = 200
            heroes[hero]['mana'] = mana_recharge
        else:
            print(f"{hero} recharged for {amount} MP!")
            mana_recharge += amount
            heroes[hero]['mana'] = mana_recharge

    elif command == "Heal":
        hero = splitted_data[1]
        amount = int(splitted_data[2])
        health_recharge = int(heroes[hero]['health'])
        if health_recharge + amount > 100:
            print(f"{hero} healed for {hp - health_recharge} HP!")
            health_recharge = 100
            heroes[hero]['health'] = health_recharge
        else:
            print(f"{hero} healed for {amount} HP!")
            health_recharge += amount
            heroes[hero]['health'] = health_recharge
for hero, value in heroes.items():
    print(f"{hero}\n  HP: {heroes[hero]['health']}\n  MP: {heroes[hero]['mana']}")
