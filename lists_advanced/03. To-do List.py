text = input()

to_do_list = [0] * 10
while text != "End":
    importance, task = text.split("-")
    importance = int(importance)
    index = importance - 1
    to_do_list[index] = task
    text = input()
print([task for task in to_do_list if task != 0])
