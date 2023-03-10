word_keys = [el.lower() for el in input().split()]
default = 0
occurences = dict.fromkeys(word_keys, default)
for word in word_keys:
    occurences[word] += 1

for word, count in occurences.items():
    if count % 2 != 0:
        print(word, end=" ")