money_of_beggars = input().split(", ")
count_of_beggars = int(input())
money_of_beggars_as_numbers = []
final_sums = []
starting_index = 0

for element in money_of_beggars:
    money_of_beggars_as_numbers.append(int(element))

while starting_index < count_of_beggars:
    sum_of_beggars = 0
    for current_index in range(starting_index, len(money_of_beggars_as_numbers), count_of_beggars):
        sum_of_beggars += money_of_beggars_as_numbers[current_index]
    final_sums.append(sum_of_beggars)
    starting_index += 1
print(final_sums)

