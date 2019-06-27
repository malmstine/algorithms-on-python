# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random


def swap(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
    return lst


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_i = 0
max_i = 0

for i, num in enumerate(array):

    if array[i] < array[min_i]:

        min_i = i

    elif array[i] > array[max_i]:

        max_i = i

if min_i != max_i:
    swap(array, min_i, max_i)

print(array)
