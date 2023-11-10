first_line = input().split(", ")
second_line = input().split(", ")
searched_words = []
for first_word in first_line:
    for second_word in second_line:
        if first_word in second_word:
            searched_words.append(first_word)
            break
print(searched_words)