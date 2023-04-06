import re

text = input()

hidden_word_pattern = r"[@#][a-zA-Z]{2,}[@#][a-zA-Z]{2,}[@#]"

hidden_word_pairs = re.findall(hidden_word_pattern, text)

mirror_word_pairs = [(words[0], words[1]) for pair in hidden_word_pairs
                     if (words := pair[1:-1].split("@") if "@" in pair else pair[1:-1].split("#"))[0] == words[1][::-1]]

if not hidden_word_pairs:
    print("No word pairs found!")
else:
    print(f"{len(hidden_word_pairs)} word pairs found!")
    if not mirror_word_pairs:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        for pair in mirror_word_pairs:
            print(f"{pair[0]} <=> {pair[1]}, ", end="")
        print()