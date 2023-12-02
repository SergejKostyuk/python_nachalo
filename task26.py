# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
"""
def f(a, b):
  if b == 0:
    return 1
  return f(a, b - 1) * a
"""

numA = int(input())
numB = int(input())

def vzved(numA,numB):
    res = 1
    if numB <=0:
        return res
    else:
        return numA * vzved(numA, numB-1)
print(vzved(numA, numB))

