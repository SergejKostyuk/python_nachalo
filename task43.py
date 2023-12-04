"""
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:
1 2 3 2 3
Вывод:
2
"""
list_n = [1, 2, 3, 2, 3]
count = 0
for i in range(len(list_n)-1):
    for j in range(i+1, len(list_n)):
        if list_n[i] == list_n[j]:
            count +=1
print(count)


"""
from collections import Counter

list_n = [1, 2, 3, 2, 3, 3, 3]
count = 0

cnt = dict(Counter(list_n))
print(cnt)

for n in cnt.values():
    count += (n * (n-1)) // 2

print(count)
"""
