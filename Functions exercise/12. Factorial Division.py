factorial_number = int(input())
divisor = int(input())
result = 1
sum = 1
for i in range(1, factorial_number + 1):
    result *= i
for j in range(1, divisor + 1):
    sum *= j
print(f"{result / sum:.2f}")