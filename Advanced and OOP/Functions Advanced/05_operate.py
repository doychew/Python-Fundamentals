def operate(sep, *args):

    if sep == "+":
        result = 0
        for el in args:
            result += el
        return result

    elif sep == "-":
        result = args[0]
        for index in range(1, len(args)):
            result -= args[index]
        return result

    elif sep == "*":
        result = 1
        for el in args:
            result *= el
        return result

    elif sep == "/":
        result = args[0]
        for index in range(1, len(args)):
            result /= args[index]
        return result
