"""
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 105
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
Ввод: Вывод:
300 220 284
"""

def get_divisors_sum(number):
    result = [1]
    for divisors in range(2, number // 2 + 1):
        if number % divisors == 0:
            result.append(divisors)
    return sum(result)

k = int(input())
st = set()
for number in range(k + 1):
    kandidat = get_divisors_sum(number)
    if get_divisors_sum(kandidat) == number and kandidat != number:
        st.add(tuple(sorted((number, kandidat))))

for a, b in st:
    print(a, b)