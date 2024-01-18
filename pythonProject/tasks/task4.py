#вариант 7

n = int(input("Введите натуральное число N: "))
s = 0

for i in range(1, n+1):
    sum = 1
    j = i
    while(j > 0):
        sum *= j
        j -= 1
    s +=sum
print("Результат - " + str(s))