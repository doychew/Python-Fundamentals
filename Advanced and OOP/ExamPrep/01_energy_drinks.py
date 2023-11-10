from collections import deque
result = 0
max_caffeine = 300
stamat_caffeine = 0
milligrams_caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])

while milligrams_caffeine and energy_drinks:
    current_caffeine = milligrams_caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    result = current_caffeine * current_energy_drink
    if result + stamat_caffeine <= 300:
        stamat_caffeine += result
    else:
        energy_drinks.append(current_energy_drink)
        stamat_caffeine -= 30
        if stamat_caffeine < 0:
            stamat_caffeine = 0
if len(energy_drinks) > 0:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")