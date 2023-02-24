neighborhood = [int(x) for x in input().split("@")]
jump_length = 0
while True:
    command = input()
    if command == "Love!":
        break
    jump, index = command.split()
    jump_length += int(index)
    if len(neighborhood) > jump_length:
        if neighborhood[jump_length] <= 0:
            print(f"Place {jump_length} already had Valentine's day.")
        else:
            neighborhood[jump_length] -= 2
            if neighborhood[jump_length] <= 0:
                print(f"Place {jump_length} has Valentine's day.")
    else:
        jump_length = 0
        if neighborhood[jump_length] <= 0:
            print(f"Place {jump_length} already had Valentine's day.")
        else:
            neighborhood[jump_length] -= 2
            if neighborhood[jump_length] <= 0:
                print(f"Place {jump_length} has Valentine's day.")
print(f"Cupid's last position was {jump_length}.")
counter = 0
for house in neighborhood:
    if house > 0:
        counter += 1
if counter > 0:
    print(f"Cupid has failed {counter} places.")
else:
    print("Mission was successful.")


