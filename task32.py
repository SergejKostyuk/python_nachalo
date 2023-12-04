# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# Вывод: [1, 9, 13, 14, 19]

import random

size_list = int(input("Введите размер списка: "))
list_1 = [0]*size_list
for i in range(size_list):
    list_1[i] = random.randint(-10, 10)
print(list_1)

min_number = int(input())
max_number = int(input())

for i, item in enumerate(list_1):
    if item >= min_number and item <= max_number:
        print(i)
