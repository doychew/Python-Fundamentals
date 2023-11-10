current_version = input().split(".")
next_version = []
version_as_string = []
for number in current_version:
    next_version.append(int(number))
next_version[2] += 1
if next_version[2] > 9:
    next_version[2] = 0
    next_version[1] += 1
if next_version[1] > 9:
    next_version[1] = 0
    next_version[0] += 1
for num in next_version:
    version_as_string.append(str(num))
print(".".join(version_as_string))