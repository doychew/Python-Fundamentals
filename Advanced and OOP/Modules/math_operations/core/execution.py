from operation import sum_nums, subtract_nums, divide_nums, multiply_nums, power

sign_mapper = {
    "+": sum_nums,
    "-": subtract_nums,
    "/": divide_nums,
    "*": multiply_nums,
    "^": power
}


def execute_string(string):
    num1, sign, num2 = string.split()
    num1 = float(num1)
    num2 = float(num2)
    return sign_mapper[sign](num1, num2)