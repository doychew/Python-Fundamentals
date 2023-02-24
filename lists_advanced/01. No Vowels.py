text = input()
result = []
forbidden_vowels = ['a', 'o', 'u', 'e', 'i']
for el in text:
    if not el.lower() in forbidden_vowels:
        result.append(el)
print("".join(result))
