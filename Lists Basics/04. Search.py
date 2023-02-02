n = int(input())
searched_word = input()
all_words_list = []
searched_word_list = []
for i in range(n):
    word = input()
    all_words_list.append(word)
    if searched_word in word:
        searched_word_list.append(word)
print(all_words_list)
print(searched_word_list)

