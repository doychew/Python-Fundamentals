from pyfiglet import figlet_format


def print_art(msg):
    ascii_art = figlet_format(msg)
    return ascii_art


msg = input()
print(print_art(msg))
