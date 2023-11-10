words = input().split()
searched_word = input()
palindromes = []
counter = 0
for word in words:
    if word == word[::-1]:
        palindromes.append(word)
    if word == searched_word:
        counter += 1
print(palindromes)
print(f"Found palindrome {counter} times")