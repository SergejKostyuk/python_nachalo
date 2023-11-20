# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# lst = [1, 2, 3, 4, 5]
# k = int(input())
# lst_1 = lst[:k]
# del lst[:k]
# lst.extend(lst_1)
# print(lst)

lst = [1, 2, 3, 4, 5]
lst1 = lst[0:3]
lst2 = lst[3:5]
print(lst1, lst2)

k = 502
if k >= len(lst):
    k = k%len(lst)
lst1 = lst[:k]
lst2 = lst[k:]
print(lst1, lst2)
print(lst2 + lst1)