#вариант 7

n = int(input("Введите натуральное число N: "))
result = 0

for i in range(1, n+1):
    sum = 1
    j = i
    while(j > 0):
        sum *= j
        j -= 1
    result +=sum
print("Результат - " + str(result))