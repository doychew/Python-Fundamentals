# words = input().split()
# searched_palindrome = input()
# palindromes = []
# palindromes_counter = 0
# for word in words:
#     if word == "".join(reversed(word)):
#         palindromes.append(word)
#     if word in searched_palindrome:
#         palindromes_counter += 1
# print(palindromes)
# print(f"Found palindrome {palindromes_counter} times")


# reversed_word = word2[::-1]
palindromes = []
palindromes_counter = 0
words = input().split()
searched_word = input()
for word in words:
    if word[::-1] == word:
        palindromes.append(word)
    if searched_word in word:
        palindromes_counter += 1
print(palindromes)
print(f"Found palindrome {palindromes_counter} times")

