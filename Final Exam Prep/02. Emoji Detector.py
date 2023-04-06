import re
text = input()
pattern = r"(:{2}|\*{2})([A-Z][a-z]{2,})(\1)"
treshold = 1
valid_emojis = [obj.group() for obj in re.finditer(pattern, text)]
for char in text:
    if char.isdigit():
        current_num = int(char)
        treshold *= current_num
cool_emojis = []
cool_treshhold = {}
for emoji in valid_emojis:
    current_count = 0
    if emoji not in cool_emojis:
        cool_treshhold[emoji] = {"current_count": 0}
    for letter in emoji:
        if letter == ":" or letter == "*":
            continue
        else:
            current_count += ord(letter)
    cool_treshhold[emoji]["current_count"] = current_count
print(f"Cool threshold: {treshold}")
print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")
for key, value in cool_treshhold.items():
    if value["current_count"] >= treshold:
        print(f"{key}")

