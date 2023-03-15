def valid_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def what_can_contain(name):
    for character in name:
        if name.isalnum() or character == "-" or character == "_":
            return True
    return False


def symbol(name):
    for character in name:
        if character == " ":
            return False
    return True


def is_valid_username(name):
    if valid_length(name) and what_can_contain(name) and symbol(name):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if is_valid_username(username):
        print(username)
