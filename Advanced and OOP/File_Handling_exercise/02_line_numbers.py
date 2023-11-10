from string import punctuation

with open("text.txt", "r") as input_file, open("output.txt", "w") as output_file:
    result = []
    for row, line in enumerate(input_file.readlines()):
        letters_count = 0
        symbol_count = 0
        for character in line:
            if character.isalpha():
                letters_count += 1
            elif character in punctuation:
                symbol_count += 1
        result.append(f"Line {row + 1}: {line[:-1]} ({letters_count})({symbol_count})")
    output_file.write("\n".join(result))
