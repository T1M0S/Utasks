# Вариант 6
from random import randint


# 1. Для заданий из практической работы №8 для своего варианта.
# Организовать ввод данных (матриц) из файла (имя: ФИО_группа_vvod.txt)
# И вывод результатов в файл (имя: ФИО_группа_vivod.txt).
with open("kutkin_roman_aleksandrovich_ym232_vyvod.txt", "w") as f:
    f.write('')
def write_into():
    with open("kutkin_roman_aleksandrovich_ym232_vyvod.txt", "a") as f:
        for line in a:
            for elem in line:
                f.write(str(elem) + ' ')
            f.write('\n')


a = []
with open('kutkin_roman_aleksandrovich_ym232_vvod.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        a.append(row)
n = len(a)

max = []
write_into()
min = []

for i in range(n):
    max_temp = 0
    min_temp = 100
    for j in range(n):
        if a[i][j] > max_temp:
            max_temp = a[i][j]
        if a[j][i] < min_temp:
            min_temp = a[j][i]
    max.append(max_temp)
    min.append(min_temp)

with open("kutkin_roman_aleksandrovich_ym232_vyvod.txt", "a") as f:
    f.write("\nМаксимальные элементы строк:\n")
    for i in range(n):
         f.write(str(max[i]) + ' ')

    f.write("\n\nМинимальные элементы столбцов:\n")
    for i in range(n):
        f.write(str(min[i]) + ' ')


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

with open("kutkin_roman_aleksandrovich_ym232_vyvod.txt", "a") as f:
    f.write("\n\nМаксимальный элемент главной и побочной диагоналей - " + str(max_main) + ", i = " + str(max_i) + ", j = " + str(
        max_j))
    f.write("\nЭлемент на пересечении главной и побочной диагоналей - " + str(a[n // 2][n // 2]) + "\n\n")
a[n // 2][n // 2] = a[max_i][max_j]

write_into()
