# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# platform darwin, python 3.7.3 x64
# Для анализа используются 3 варианта программы из 3 урока 9 задачи.
# Эти же варианты также ипользовались в 4 уроке для анализа быстродействия

import random
import sys

M = 40
N = 40
MIN_ITEM = 0
MAX_ITEM = 10

PRINT_MATRIX = False
SHOW_VARS = True
DETAIL = False

MATRIX = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(N)] for _ in range(M)]


if PRINT_MATRIX:
    for row in MATRIX:
        for element in row:
            print(f'{element:>4}', end='')
        print('')


def trace_func(frame, event, arg):

    if event == "return":

        global us_memory
        for key in frame.f_locals.keys():

            size = var_size(frame.f_locals[key])
            us_memory += size

            if SHOW_VARS:
                print(f'{key} {type(frame.f_locals[key])}: {size}')

            if DETAIL:
                print('')

    return trace_func


def var_size(x, level=0):

    res = sys.getsizeof(x)

    if DETAIL:
        print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}')

    if hasattr(x, '__iter__'):

        if hasattr(x, 'items'):
            for key, value in x.items():
                res += var_size(key, level + 1)
                res += var_size(value, level + 1)

        elif not isinstance(x, str):
            for item in x:
                res += var_size(item, level + 1)

    return res


# Реализация в один проход с чтением по строкам
# Такая реализация позволяет выиграть производительность за счет кэширования данных
def cache_optimized(matrix=MATRIX):

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

# Результат для матрицы 40x40:
# Дла функции cache_optimized:
# .0 <class 'range_iterator'>: 48
# _ <class 'int'>: 28
# matrix <class 'list'>: 61944
# min_array <class 'list'>: 1392
# row <class 'list'>: 1544
# i <class 'int'>: 24
# el <class 'int'>: 28
# min_el <class 'int'>: 24
# Суммарный объем памяти 65032


def column_move(matrix=MATRIX):

    res = float('-inf')
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

# Результат для матрицы 40x40:
# Дла функции column_move:
# matrix <class 'list'>: 61944
# res <class 'int'>: 24
# columns <class 'int'>: 28
# rows <class 'int'>: 28
# col <class 'int'>: 28
# min_el <class 'int'>: 24
# row <class 'int'>: 28
# Суммарный объем памяти 62104


def with_transpose(matrix=MATRIX):

    res = float('-inf')
    tr_matrix = zip(*matrix)

    for tr_row in tr_matrix:

        min_el = tr_row[0]
        for el in tr_row:

            if el < min_el:
                min_el = el

        if res < min_el:
            res = min_el

    return res

# Результат для матрицы 40x40:
# Дла функции with_transpose:
# matrix <class 'list'>: 61944
# res <class 'int'>: 24
# tr_matrix <class 'zip'>: 64
# tr_row <class 'tuple'>: 1464
# min_el <class 'int'>: 24
# el <class 'int'>: 28
# Суммарный объем памяти 63548


funcs = [(cache_optimized, ()), (column_move, ()), (with_transpose, ())]

sys.settrace(trace_func)
for func, args in funcs:
    us_memory = 0
    print(f'Дла функции {func.__name__}:')
    sys.call_tracing(func, args)
    print(f'Суммарный объем памяти {us_memory}\n')

# Итоговый результат для матрицы 40x40:
# cache_optimized - 65032, column_move - 62104, with_transpose - 63548

# Результаты из урока 4 для матрицы 40x40:
# cache_optimized - 137 usec, column_move - 149 usec, with_transpose - 66.9 usec

# Исходя из полученных результатов для матриц небольших размеров оптимальный вариант:
# – с точки зрения памяти получен с помощью фукнции column_move.
# – с точки зрения памяти и быстроействия получен с помощью функции with_transpose
