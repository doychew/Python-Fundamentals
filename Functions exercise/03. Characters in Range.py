def characters_collection(first, second):
    string_collection = []
    for current_element in range(ord(first) + 1, ord(second)):
        string_collection.append(chr(current_element))
    return string_collection


first_element = input()
second_element = input()
result = characters_collection(first_element, second_element)
print(*result)