
name = []
counter = 0
command = input()
while command != "End":
    name.append(command)
    counter += 1
    command = input()
print(f"Going: {', '.join(name)}")
print(f"Total: {counter}")