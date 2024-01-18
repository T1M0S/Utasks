import math

#вариант №7
x = float(input("Введите переменную Х: "))
y = float(input("Введите переменную y: "))
z = float(input("Введите переменную z: "))

s = 5 * math.atan(x) - 1 / 4 * math.acos(x) * ((x + 3 * abs((x - y)) + math.pow(x, 2))/((abs(x - y))* z + math.pow(x, 2)))

print("Ответ S = " + str(s))