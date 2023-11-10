def characters_between_them(first, second):
    characters = []
    for current_character in range(ord(first) + 1, ord(second)):
        characters.append(chr(current_character))
    return characters

first_character = input()
second_character = input()

result = characters_between_them(first_character, second_character)
print(' '.join(result))