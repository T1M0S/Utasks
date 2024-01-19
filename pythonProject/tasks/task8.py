# Вариант 6
from random import randint


# 1. Дана целочисленная квадратная матрица.
# Найти в каждой строке наибольший элемент и в каждом столбце наименьший. Вывести на экран.
# 2. Дана действительная квадратная матрица порядка N (N — нечетное),
# все элементы которой различны. Найти наибольший элемент среди стоящих на главной
# и побочной диагоналях и поменять его местами с элементом, стоящим на пересечении этих диагоналей.

# 1
def show_matrix():
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()


n = int(input("Введите размер матрицы: "))
a = [[randint(1, 99) for j in range(n)] for i in range(n)]

max = []
show_matrix()
min = []

for i in range(n):
    max_temp = a[0][0]
    min_temp = a[0][0]
    for j in range(n):
        if a[i][j] > max_temp:
            max_temp = a[i][j]
        if a[j][i] < min_temp:
            min_temp = a[j][i]
    max.append(max_temp)
    min.append(min_temp)

print("\nМаксимальные элементы строк:")
for i in range(n):
    print(max[i], end=' ')

print("\n\nМинимальные элементы столбцов:")
for i in range(n):
    print(min[i], end=' ')

print()

# 2
max_main = a[0][0]

max_i = 0
max_j = 0

for i in range(n):
    if a[i][i] > max_main:
        max_main = a[i][i]
        max_i = i
        max_j = i
    if a[i][n - 1 - i] > max_main:
        max_main = a[i][n - 1 - i]
        max_i = i
        max_j = n - 1 - i

print("\nМаксимальный элемент главной и побочной диагоналей - " + str(max_main) + ", i = " + str(max_i) + ", j = " + str(max_j))
print("Элемент на пересечении главной и побочной диагоналей - " + str(a[n // 2][n // 2]))
print()
a[n // 2][n // 2] =a[max_i][max_j]
show_matrix()
