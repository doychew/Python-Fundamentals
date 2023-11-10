text = input()

forbidden_vowels = ['a', 'o', 'u', 'e', 'i']
result = [el for el in text if not el.lower() in forbidden_vowels]
# for el in text:
#     if not el.lower() in forbidden_vowels:
#         result.append(el)
print("".join(result))
