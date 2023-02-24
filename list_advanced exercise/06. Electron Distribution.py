number_of_electrons = int(input())
new_list = []
i = 0

while 0 < number_of_electrons:
    i += 1
    shell = 2*i**2

    if number_of_electrons >= shell:
        new_list.append(shell)
        number_of_electrons -= shell
    else:
        new_list.append(number_of_electrons)
        number_of_electrons = 0

print(new_list)