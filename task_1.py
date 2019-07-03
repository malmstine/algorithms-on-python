# Проанализировать скорость и сложность одного любого алгоритма из
# разработанных в рамках домашнего задания первых трех уроков

# Задача: "Найти максимальный элемент среди минимальных элементов столбцов матрицы"

import random
import cProfile

M = 400
N = 400
MIN_ITEM = 0
MAX_ITEM = 10
PRINT_MATRIX = False
TEST = False
PROFILE = False

MATRIX = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(N)] for _ in range(M)]

if PRINT_MATRIX is True:
    for row in MATRIX:
        for element in row:
            print(f'{element:>4}', end='')
        print('')


# Реализация в один проход с чтением по строкам
# Такая реализация позволяет выиграть производительность за счет кэширования данных
def cache_optimized(matrix=None):

    if not matrix:
        matrix = MATRIX

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

    return min_el

# M = 40,    N = 40:    100 loops, best of 5: 137 usec per loop
# M = 100,   N = 16:    100 loops, best of 5: 152 usec per loop
# M = 16,    N = 100:   100 loops, best of 5: 144 usec per loop

# M = 400,   N = 400:   100 loops, best of 5: 12.4 msec per loop
# M = 1000,  N = 160:   100 loops, best of 5: 11.5 msec per loop
# M = 160,   N = 1000:  100 loops, best of 5: 13.7 msec per loop

# M = 4000,  N = 4000:  100 loops, best of 5: 1.39 sec per loop
# M = 10000, N = 1600:  100 loops, best of 5: 1.36 sec per loop
# M = 1600,  N = 10000: 100 loops, best of 5: 1.56 sec per loop

# Профилирование для M = 4000,  N = 4000:
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    1.518    1.518 <string>:1(<module>)
#      1    1.518    1.518    1.518    1.518 task_1.py:24(cache_optimized)
#      1    0.000    0.000    0.000    0.000 task_1.py:30(<listcomp>)
#      1    0.000    0.000    1.518    1.518 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Сложность O(n)
# Кеширование данных позволяет получить значительный прирост производительности по сравнению с column_move


# Однопроходное решение с движеним по столбцам
def column_move(matrix=None):

    res = float('-inf')

    if not matrix:
        matrix = MATRIX

    columns = len(matrix[0])
    rows = len(matrix)

    for col in range(columns):

        min_el = matrix[0][col]
        for row in range(rows):

            if min_el > matrix[row][col]:
                min_el = matrix[row][col]

        if res < min_el:
            res = min_el

    return res

# M = 40,    N = 40:    100 loops, best of 5: 149 usec per loop
# M = 100,   N = 16:    100 loops, best of 5: 131 usec per loop
# M = 16,    N = 100:   100 loops, best of 5: 190 usec per loop

# M = 400,   N = 400:   100 loops, best of 5: 14.2 msec per loop
# M = 1000,  N = 160:   100 loops, best of 5: 15.1 msec per loop
# M = 160,   N = 1000:  100 loops, best of 5: 12.9 msec per loop

# M = 4000,  N = 4000:  100 loops, best of 5: 2.72 sec per loop
# M = 10000, N = 1600:  100 loops, best of 5: 2.61 sec per loop
# M = 1600,  N = 10000: 100 loops, best of 5: 2.5 sec per loop

# Профилирование для M = 4000,  N = 4000:
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    2.984    2.984 <string>:1(<module>)
#      1    2.984    2.984    2.984    2.984 task_1.py:62(column_move)
#      1    0.000    0.000    2.984    2.984 {built-in method builtins.exec}
#      2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Сложность O(n)
# Самый медленных алгоритм. Потребление памяти минимально


def with_transpose(matrix=None):

    res = float('-inf')

    if not matrix:
        matrix = MATRIX

    tr_matrix = zip(*matrix)

    for tr_row in tr_matrix:

        min_el = tr_row[0]
        for el in tr_row:

            if el < min_el:
                min_el = el

        if res < min_el:
            res = min_el

    return res

# M = 40,    N = 40:    100 loops, best of 5: 66.9 usec per loop
# M = 100,   N = 16:    100 loops, best of 5: 65.4 usec per loop
# M = 16,    N = 100:   100 loops, best of 5: 77.2 usec per loop

# M = 400,   N = 400:   100 loops, best of 5: 6.24 msec per loop
# M = 1000,  N = 160:   100 loops, best of 5: 6.4 msec per loop
# M = 160,   N = 1000:  100 loops, best of 5: 6.15 msec per loop

# M = 4000,  N = 4000:  100 loops, best of 5: 1.92 sec per loop
# M = 10000, N = 1600:  100 loops, best of 5: 2 sec per loop
# M = 1600,  N = 10000: 100 loops, best of 5: 1.18 sec per loop

# Анамально-низкая скорость работы на маленьких резмерностях. Чтобы убедиться в линейности, делаем еще один замер
# M = 8000,  N = 8000:  100 loops, best of 5: 8.64 sec per loop
# M = 20000, N = 3200:  100 loops, best of 5: 8.88 sec per loop
# M = 3200,  N = 20000: 100 loops, best of 5: 8.33 sec per loop

# Профилирование для M = 4000,  N = 4000:
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    2.374    2.374 <string>:1(<module>)
#      1    2.373    2.373    2.373    2.373 task_1.py:101(with_transpose)
#      1    0.000    0.000    2.374    2.374 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Сложность O(n)
# Данная реализация требует значительного объема дополнительной памяти
# Анамально-низкая скорость работы на маленьких резмерностях,
# На больших размерностях за счет кешированя выигрывает по скоросту column_move, но по непонятным причинам
# Значительно отстает от cache_optimized


# Создает несолко тестовых матриц и сравнивает результат работы каждой функции, они должны совпадать
def test(funcs):

    for _ in range(10):
        matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(N)] for _ in range(M)]
        assert len(set([f(matrix) for f in funcs])) == 1


if TEST is True:
    test([cache_optimized, column_move, with_transpose])
    print('test ok')

if PROFILE is True:
    cProfile.run('cache_optimized()')
    cProfile.run('column_move()')
    cProfile.run('with_transpose()')
