sequence = input().split()
result = ""
for word in sequence:
    lenght = len(word)
    result += word * lenght
print(result)