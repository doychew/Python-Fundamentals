def sum_nums(num1, num2):
    return num1 + num2


def subtract_nums(num1, num2):
    return num1 - num2


def multiply_nums(num1, num2):
    return num1 * num2


def divide_nums(num1, num2):
    try:
        num1 / num2
    except ZeroDivisionError:
        return None


def power(num1, num2):
    return num1 ** num2


sign_mapper = {
    "+": sum_nums,
    "-": subtract_nums,
    "/": divide_nums,
    "*": multiply_nums,
    "^": power
}
