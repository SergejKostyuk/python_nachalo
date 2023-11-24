"""
Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов
первого множества. m - кол-во элементов второго множества. Затем пользователь 
вводит сами элементы множеств.
vsl = '11 6'
vals1 = '2 4 6 8 10 12 10 8 6 4 2'
vals2 = '3 6 9 12 15 18'
resalt = '6 12'
"""
# mol = [int(x) for x in var1.split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in var2.split()]
# k = set(a)
# for i in k:
#    set_1.add(i)
# b = [int(x) for x in var3.split()]
# k1 = set(b)
# for i in k1:
#    set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#    print(i, end=' ')

size1 = int(input("Введите размер первого набора целых чисел: ")) 
list_1, list_2 = list(), list()
for i in range(size1):
    n = int(input())
    list_1.append(n)

size2 = int(input("Введите размер вторго набора целых чисел: ")) 
for i in range(size2):
    n = int(input())
    list_2.append(n)

set_1 = set(list_1)
set_2 = set(list_2)


resalt =set_1.intersection(set_2)
 
resalt_1 = list(resalt)
resalt_1.sort()

print(resalt_1)
# st = " "
# for i in resalt_1:
#     st += i + ' ' 
# print(st)

