text = input().split()
dict = {}
for word in text:
    for letter in word:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1
for char, counter in dict.items():
    print(f"{char} -> {counter}")