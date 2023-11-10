def palindrome(positive_ints):
    for character in positive_ints:
        is_palindrome = character[0] == character[-1]
        print(is_palindrome)
numbers = input().split(", ")
palindrome(numbers)