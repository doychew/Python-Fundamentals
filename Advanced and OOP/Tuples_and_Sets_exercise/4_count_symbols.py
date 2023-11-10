text = tuple(input())
unique_symbols = sorted(set(text))
for element in unique_symbols:
    print(f"{element}: {text.count(element)} time/s")