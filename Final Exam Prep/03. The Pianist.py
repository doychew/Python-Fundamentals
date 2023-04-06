songs = {}
number_of_pieces = int(input())
for i in range(number_of_pieces):
    piece, composer, key = input().split("|")
    songs[piece] = {"composer": composer, "key": key}
while True:
    data = input()
    if data == "Stop":
        break
    splitted_data = data.split("|")
    command = splitted_data[0]

    if command == "Add":
        piece = splitted_data[1]
        composer = splitted_data[2]
        key = splitted_data[3]
        if piece in songs:
            print(f"{piece} is already in the collection!")
        else:
            songs[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command == "Remove":
        piece = splitted_data[1]
        if piece in songs:
            print(f"Successfully removed {piece}!")
            del songs[piece]
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        piece = splitted_data[1]
        new_key = splitted_data[2]
        if piece in songs:
            songs[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
for piece, value in songs.items():
    print(f"{piece} -> Composer: {songs[piece]['composer']}, Key: {songs[piece]['key']}")