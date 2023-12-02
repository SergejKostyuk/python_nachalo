# Задача №31.
# Последовательностью Фибоначчи называется
# последовательность чисел
# a0, a1, ..., an , ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def fibonaci(n):
    if n <= 0:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)
print(fibonaci(5))