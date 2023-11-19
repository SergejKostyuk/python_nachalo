# Задача 10: На столе лежат n монеток. Некоторые из 
# них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх 
# одной и той же стороной. Выведите минимальное 
# количество монет, которые нужно перевернуть.
# Вводные данные: 5 -> 1 0 1 1 0
# Результат: 2

coins = [0, 1, 0, 1, 1, 0]
countOrel = 0
countReshka = 0
for i in coins:
    if i == 0:
        countOrel += 1
    else:
        countReshka += 1
if countOrel > countReshka:
    print(countReshka)
else:
    print(countOrel)


# n = int(input("Введите количество монет: "))
# countOrel = 0
# countReshka = 0
# i = 0
# while i < n:
#     monet = int(input("0 -> Орел, 1 -> Решка: "))
#     if monet == 0:
#         countOrel += 1
#     else:
#         countReshka += 1
#     i += 1
# if countOrel > countReshka:
#     print(countReshka)
# else:
#     print(countOrel)

