# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A. Последняя строка
# содержит число k
# 5
# 1 2 3 4 5
# 6 -> 5
"""
list_1 = [1, 4, 3, 7, 8, 9, 2]
k = 8
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)
"""

size = int(input("Введите размер масива: "))
list = list()
for i in range(size):
    i = int(input(f"Введите число в ячейку {i + 1}: "))
    list.append(i)
print(list)
levt = float('-inf')
reat = float('inf')
res = 0
k = int(input("Введите число: "))
for i in list:
    if i == k:
        res = k
    elif i < k:
        if levt < i:
            levt = i
    else:
        if reat > i:
            reat = i
if k == res:
    print(res)
elif k - levt < reat - k:
    print(levt)
else:
    print(reat)

