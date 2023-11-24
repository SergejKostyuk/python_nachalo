"""
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
"""

c = 'a a a b c a a d c d d'
c = c.split()
dt = {}
for i in c:
    if i not in dt:
        dt[i] = 1 # /=0
        print(i, end=' ')
    else:
        # print(F'{i}_{dt[i]}', end=' ')
        dt[i] = dt[i] + 1
        print(F'{i}_{dt[i]-1}', end=' ')