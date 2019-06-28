# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.


import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

one_i = 0
two_i = 1

if array[0] > array[1]:
    one_i = 1
    two_i = 0

for i, num in enumerate(array[2:], start=2):
    if num < array[one_i]:
        two_i = one_i
        one_i = i
    elif num < array[two_i]:
        two_i = i

print(array[one_i], array[two_i])
