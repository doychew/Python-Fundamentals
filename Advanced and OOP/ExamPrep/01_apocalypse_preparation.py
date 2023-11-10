from collections import deque

textiles = deque([int(x) for x in input().split()])
medicament = [int(x) for x in input().split()]
items_dict = {"Patch": 0,
              "Bandage": 0,
              "MedKit": 0
              }

while textiles and medicament:
    current_textile = textiles.popleft()
    current_medicament = medicament.pop()
    result = current_medicament + current_textile
    if result == 30:
        items_dict["Patch"] += 1
    elif result == 40:
        items_dict["Bandage"] += 1
    elif result == 100:
        items_dict["MedKit"] += 1
    elif result > 100:
        items_dict["MedKit"] += 1
        result -= 100
        medicament[-1] += result
    else:
        current_medicament += 10
        medicament.append(current_medicament)

if len(textiles) == 0 and len(medicament) == 0:
    print("Textiles and medicaments are both empty.")
else:
    if not textiles:
        print("Textiles are empty.")
    elif not medicament:
        print("Medicaments are empty.")

sorted_items = sorted(items_dict.items(), key=lambda x: (-x[1], x[0]))
for item in sorted_items:
    if int(item[1]) > 0:
        print(f"{item[0]} - {item[1]}")

if medicament:
    medicament.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicament))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")
