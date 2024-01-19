# вариант 7
import re

for i in range(1, 5):  # для теста
    s = input("Введите строку: ")
    s2 = s[0: int(len(s) / 2)]
    s2 = re.sub("[пП]", "*",s2)

    print(s2 + s[int(len(s) / 2): int(len(s))])
