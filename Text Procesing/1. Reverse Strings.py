while True:
    data = input()
    if data == "end":
        break
    reverse_data = data[::-1]
    print(f"{data} = {reverse_data}")