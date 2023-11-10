symbols = input().split()
letters = {}
for word in symbols:
    for letter in word:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
for letter, count in letters.items():
    print(f"{letter} -> {count}")
