first_player, second_player = input().split(", ")
size_of_the_matrix = 6
matrix = []
for _ in range(size_of_the_matrix):
    matrix.append(input().split())

first_player_needs_rest = False
second_player_needs_rest = False

while True:
    first_player_coordinates = input()
    if not first_player_needs_rest:
        row, col = map(int, first_player_coordinates.strip("(").strip(")").split(", "))
        if matrix[row][col] == "E":
            print(f"{first_player} found the Exit and wins the game!")
            break
        elif matrix[row][col] == "T":
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break
        elif matrix[row][col] == "W":
            print(f"{first_player} hits a wall and needs to rest.")
            first_player_needs_rest = True
    else:
        first_player_needs_rest = False

    second_player_coordinates = input()
    if not second_player_needs_rest:
        row, col = map(int, second_player_coordinates.strip("(").strip(")").split(", "))
        if matrix[row][col] == "E":
            print(f"{second_player} found the Exit and wins the game!")
            break
        elif matrix[row][col] == "T":
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break
        elif matrix[row][col] == "W":
            print(f"{second_player} hits a wall and needs to rest.")
            second_player_needs_rest = True
    else:
        second_player_needs_rest = False
