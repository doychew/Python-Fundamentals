from collections import deque


tools = deque(int(x) for x in input().split())
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances and challenges:
    current_tool = tools.popleft()
    current_substance = substances.pop()
    result = current_tool * current_substance

    if result in challenges:
        challenges.remove(result)
    else:
        current_tool += 1
        current_substance -= 1
        tools.append(current_tool)
        if current_substance > 0:
            substances.append(current_substance)

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join([str(t) for t in tools])}")
if substances:
    print(f"Substances: {', '.join([str(s) for s in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(c) for c in challenges])}")
    