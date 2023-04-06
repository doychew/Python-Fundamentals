import re
text = input().lower()
searched_word = input().lower()
matches = re.findall(f'\\b{searched_word}\\b', text)
print(len(matches))