# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
# случайными числами на промежутке[0; 50).Выведите на экран исходный и отсортированный массивы.

from random import uniform
from collections import deque

MIN_ITEM = 0
MAX_ITEM = 50
SIZE = 20


def merge_sort(array):

    def merge(left, right):

        if left == right:
            return deque([array[left]])

        mid = (left + right) // 2
        fst, lst = merge(left, mid),  merge(mid + 1, right)

        res = deque()
        while True:
            res.append(fst.popleft() if fst[0] < lst[0] else lst.popleft())

            if len(fst) == 0:
                res.extend(lst)
                return res

            elif len(lst) == 0:
                res.extend(fst)
                return res

    return list(merge(0, len(array) - 1))


def test_merge_sort(n):

    while n > 0:

        array = [uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
        sorted_array = merge_sort(array)

        for i, num in enumerate(sorted(array)):
            assert sorted_array[i] == num
        n -= 1

    print('yay!!!')


test_merge_sort(1000)

random_array = [uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Исходный массив: ', random_array)
print('Отсортированный массив: ', merge_sort(random_array))
