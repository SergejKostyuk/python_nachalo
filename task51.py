"""Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.
Ввод:                                 Вывод:
values = [0, 2, 10, 6]                same
if same_by(lambda x: x % 2, values):
print('same')
else:
print('different')
"""

def same_by(characteristic, objects):
    lst = list(map(characteristic, objects))
    n = len(set(lst))
    return n == 1 or n == 0
    # return len(set(lst)) in (0, 1) сокращенный вариант двух строк выше


values = ['hello', 'pyton', [1, 2, 3, 4, 5]]

if same_by(lambda x: len(x), values):
    print('same')
else:
    print('different')