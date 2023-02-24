first_input = input().split(", ")
second_input = input().split(", ")
sequences = []
for first_word in first_input:
    for second_word in second_input:
        if first_word in second_word:
            sequences.append(first_word)
            break
print(sequences)

