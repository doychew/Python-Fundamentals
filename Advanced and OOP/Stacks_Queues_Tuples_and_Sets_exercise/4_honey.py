from collections import deque
working_bees = deque(int(x) for x in input().split())
nectar = ([int(x) for x in input().split()])
symbols = deque(input().split())
total_honey = 0
while working_bees and nectar:
    if working_bees[0] > nectar[-1]:
        nectar.pop()
    elif working_bees[0] <= nectar[-1]:
        current_symbol = symbols.popleft()
        if current_symbol == "+":
            result = working_bees[0] + nectar[-1]
            total_honey += abs(result)
            nectar.pop()
            working_bees.popleft()

        elif current_symbol == "-":
            result = working_bees[0] - nectar[-1]
            total_honey += abs(result)
            nectar.pop()
            working_bees.popleft()

        elif current_symbol == "*":
            result = working_bees[0] * nectar[-1]
            total_honey += abs(result)
            nectar.pop()
            working_bees.popleft()

        elif current_symbol == "/":
            if nectar[-1] == 0:
                nectar.pop()
                working_bees.popleft()
                continue
            else:
                result = working_bees[0] / nectar[-1]
                total_honey += abs(result)
                nectar.pop()
                working_bees.popleft()

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
