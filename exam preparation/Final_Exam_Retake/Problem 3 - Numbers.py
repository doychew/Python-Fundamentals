sequences = [int(x) for x in input().split()]
avg_score = 0
new_list = []
is_greater = False
for current_number in sequences:
    avg_score = sum(sequences) / len(sequences)
    if current_number > avg_score:
        new_list.append(current_number)

if len(new_list) == 0:
    print("No")
else:
    filtered_list = sorted(new_list, reverse=True)
    if len(filtered_list) > 5:
        filtered_list = filtered_list[0:5]
    filtered_list = [str(y) for y in filtered_list]
    print(' '.join(filtered_list))
