#вариант 7

for i in range(1,5): # для теста
    s = input("Введите строку: ")
    s2 = s[0 : int(len(s)/2)]
    print(s2.replace("п","*") + s[int(len(s)/2) : int(len(s))])