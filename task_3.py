# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в
# массиве  медиану. Медианой называется элемент ряда, делящий его на две равные части: в
# одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

MIN_ITEM = 1
MAX_ITEM = 30
SIZE = 31


# Логика работы - делается несколько итераций алгоритма быстрой сортировки
# После каждый итерации получаем два участка массива, в одном из них находится медиана
# Проводим слеующую итерацию на этом участке. Итерации продолжаются, пока участок содержит больше одного элемента
def median(array):

    left = 0
    right = len(array) - 1
    pos = right // 2

    while left < right:  # Пока сортируемый участок больше одного элемента

        # Делаем итерацию алгоритма быстрой сортировки
        # После каждой итерации, медиана приближается к середине массива
        pivot = array[random.randint(left, right)]
        fst, lst = left, right

        while fst <= lst:
            while array[fst] < pivot:
                fst += 1
            while array[lst] > pivot:
                lst -= 1
            if fst <= lst:
                array[fst], array[lst] = array[lst], array[fst]
                fst += 1
                lst -= 1

        # После итерации выбираем тот диапазон, который содержит середину массива
        if lst < pos < fst:  # Если удача оказалась на нашей стороне и опорный элемент - медиана
            return array[pos]
        else:  # Иначе ограничиваем участок
            if pos < fst:
                right = lst
            else:
                left = fst

    return array[pos]


def test_median(n):

    while n > 0:
        array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
        assert sorted(array)[SIZE // 2] == median(array)
        n -= 1

    print("yay!!!")


test_median(1000)

random_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Исходный массив', random_array)
print('Медиана', median(random_array))
