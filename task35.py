# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

n = int(input())

def funct(n):
    for i in range(2, n):
        if n % i ==0:
            return('NO')
    return('Yes')
print(funct(n))