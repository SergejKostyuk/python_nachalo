"""
Задача №39. 
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод: Вывод:
Ввод:
7
3 1 3 4 2 4 12
6
4 15 43 1 15 1
ывод:
3 3 2 12
"""
import random
a = int(input())
b = int(input())
list_1 = [0]*a
list_2 = [0]*b
answer = []
for i in range(a):
    list_1[i] = random.randint(1, 10)
for i in range(b):
    list_2[i] = random.randint(1, 10)
print(list_1, list_2)
for i in list_1:
    if i not in list_2:
        answer.append(i)
print(*answer)