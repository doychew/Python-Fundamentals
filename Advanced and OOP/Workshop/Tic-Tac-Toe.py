def render_board(board_):
    for row in board_:
        print("| ", end="")
        print(f" | ".join([sign if sign else " " for sign in row]), end="")
        print(" |")


def is_valid_sign(player_one_sign_):
    return player_one_sign_ in ["X", "O"]


def is_row_win(board_):
    for row in board_:
        if len(set(row)) == 1 and set(row) != {None}:
            return True
    return False


def is_column_win(board_, current_sign_):
    for col in range(len(board_)):
        current_column = []
        for row in range(len(board_)):
            current_column.append(board_[row][col] == current_sign_)
        if all(current_column):
            return True
    return False


def is_diagonal_win(board_, current_sign_):
    diagonal_1, diagonal_2 = [], []
    for index in range(len(board_)):
        diagonal_1.append(board_[index][index] == current_sign_)
        diagonal_2.append(board_[index][len(board_) - 1 - index] == current_sign_)
    return all(diagonal_1) or all(diagonal_2)


def is_win(board_, current_sign_):
    if any([is_diagonal_win(board_, current_sign_), is_row_win(board_), is_column_win(board_, current_sign_)]):
        return True
    return False


def is_draw(board_):
    if any([None in row for row in board_]):
        return False
    return True


def is_valid_choice(board_, board_mapper_, choice_):
    if not choice_.isdigit():
        return False
    choice_ = int(choice_)
    if choice_ not in board_mapper_:
        return False
    if board_[board_mapper_[choice_][0]][board_mapper_[choice_][1]]:
        return False
    return True


player_one = input("Player one name: ").strip()
player_two = input("Player two name: ").strip()

while True:
    player_one_sign = input(f"{player_one}, would you like to play with 'X' or 'O'?")
    if is_valid_sign(player_one_sign):
        break
    print("Please, enter a one of 'X' or 'O'!")
player_two_sign = 'X' if player_one_sign == "O" else "O"

size = 3
board = [[None] * size for _ in range(size)]
board_mapper = {i + 1: (i // size, i % size) for i in range(size * size)}

print("This is the numeration of the board:")
[print(f"| {' | '.join([str(i + 1 + row * size) for i in range(size)])} |") for row in range(size)]
print(f"{player_one} starts first!")

turn = 1

while True:
    current_player = player_one if turn % 2 else player_two
    current_sign = player_one_sign if turn % 2 else player_two_sign
    while True:
        choice = input(f"{current_player} choose a free position [1-9]: ").strip()
        if is_valid_choice(board, board_mapper, choice):
            break
    row, col = board_mapper[int(choice)]
    board[row][col] = current_sign
    render_board(board)
    if is_win(board, current_sign):
        print(f"{current_player} won!")
        break
    if is_draw(board):
        print("Draw!")
        break
    turn += 1
