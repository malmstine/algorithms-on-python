# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными
# числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы

from random import randint

MIN_ITEM = -100
MAX_ITEM = 99
SIZE = 20


def bubble_sort(array, compare=lambda a, b: a > b):

    len_array = len(array)

    while len_array > 1:

        end_pos = 0
        for i in range(len_array - 1):

            if compare(array[i], array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                end_pos = i + 1

        len_array = end_pos

    return array


def test_bubble_sort(n):
    # При достаточно большом количестве испытаний вероятность, что мы где-то что-то сделали не так довольно мала
    while n > 0:

        array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
        sorted_array = bubble_sort(array.copy())

        for i, num in enumerate(sorted(array)):
            assert sorted_array[i] == num
        n -= 1

    # Во всяком случае это лучне чем ничего ¯\_( ⋅- ⋅)_/¯
    print('yay!!!')


test_bubble_sort(1000)

random_array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Исходный массив: ', random_array)
print('Отсортированный массив: ', bubble_sort(random_array, lambda a, b: a < b))
