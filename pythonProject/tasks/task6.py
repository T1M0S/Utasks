# вариант 7

n = int(input("Введите длинну массива: "))
print("Введите целочисленный список: ")

x = []
sum = 0
mult = 1
for i in range(n):
    x.append(int(input()))

for i in range(len(x)):
    if i % 2 == 0: mult *= x[i]
    if i % 2 == 1: sum += x[i]

print(x)
print("Сумма четных чисел - " + str(sum))
print("Произведение нечетных чисел - " + str(mult) + "\n")

print(x)

temp = min(x)
temp_x = x.index(max(x))
x[x.index(min(x))] = max(x)
x[temp_x] = temp

print(x)
