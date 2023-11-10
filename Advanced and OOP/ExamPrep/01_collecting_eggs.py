from collections import deque

size_of_the_eggs = deque([int(x) for x in input().split(", ")])
piece_of_paper = deque([int(x) for x in input().split(", ")])
boxes = 0
while size_of_the_eggs and piece_of_paper:
    current_egg = size_of_the_eggs.popleft()
    current_paper = piece_of_paper.pop()
    if current_egg == 13:
        first_paper = piece_of_paper.popleft()
        piece_of_paper.appendleft(current_paper)
        piece_of_paper.append(first_paper)
        continue
    if current_egg <= 0:
        piece_of_paper.append(current_paper)
        continue
    result = current_egg + current_paper
    if result <= 50:
        boxes += 1
if boxes >= 1:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if size_of_the_eggs:
    print(f"Eggs left: {', '.join(map(str, size_of_the_eggs))}")
if piece_of_paper:
    print(f"Pieces of paper left: {', '.join(map(str, piece_of_paper))}")