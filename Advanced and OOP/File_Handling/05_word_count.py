import re

with open("words.txt", "r") as file:
    searched_words = file.read().split()


with open("input.txt", "r") as file:
    text = file.read()

words = {}


for searched_word in searched_words:
    pattern = re.compile(rf"\b{searched_word}\b")
    result = re.findall(pattern, text)
    words[searched_word] = len(result)

sorted_words = sorted(words.items(), key=lambda kvp: -kvp[1])

with open("output.txt", "w") as file:
    for key, value in sorted(words.items(), key=lambda kvp: -kvp[1]):
        file.write(f"{key}-{value}\n")