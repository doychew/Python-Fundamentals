import re

text1 = input()


pattern = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b"
numbers1 = re.findall(pattern, text1)
print(", ".join(numbers1))

