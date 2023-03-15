while True:
    data = input()
    if data == "end":
        break
    reverse_word = data[::-1]
    print(f"{data} = {reverse_word}")