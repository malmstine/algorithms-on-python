# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

M = 10
N = 10
MIN_ITEM = 0
MAX_ITEM = 10

matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(N)] for _ in range(M)]
for row in matrix:
    for element in row:
        print(f'{element:>4}', end='')
    print('')

# Реализация в один проход с чтением по строкам
# Такая реализация позволяет выиграть производительность за счет кэширования данных

# Минимальные элементы столбцов
min_array = [MAX_ITEM for _ in range(N)]


for row in matrix:
    for i, el in enumerate(row):
        if min_array[i] > el:
            min_array[i] = el


min_el = MIN_ITEM - 1

for i in min_array:
    if i > min_el:
        min_el = i

print(min_el)


