# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

numA = int(input())
numB = int(input())

def sum(numA,numB):
    if numB == 0:
        return numA
    elif numA == 0:
        return numB
    else:
        return sum(numA + 1, numB - 1)
print(sum(numA, numB))


