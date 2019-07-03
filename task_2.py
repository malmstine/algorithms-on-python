# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения
# простого числа должна принимать на вход натуральное и возвращать соответствующее
# простое число. Проанализировать скорость и сложность алгоритмов.

import cProfile
from math import sqrt, log

TEST = False
PROFILE = False
PROFILE_N = 5000


# Стандартный алгоритм "Решето Эратосфена" без оптимизаций и с постой логикой
# Используется только для того, чтобы оценить эффективность других реализаций
def sieve(n):

    if n == 1:
        return 2

    size = n * n  # Искомое число гарантированно будет меньше
    sieve_array = [i for i in range(size)]
    sieve_array[1] = 0

    for i in range(2, size):
        if sieve_array[i] != 0:
            j = i + i
            while j < size:
                sieve_array[j] = 0
                j += i

    res = [i for i in sieve_array if i != 0]

    return res[n - 1]

# 'task_2.sieve(100)'
# 100 loops, best of 5: 3.87 msec per loop
# 'task_2.sieve(500)'
# 100 loops, best of 5: 128 msec per loop
# 'task_2.sieve(2000)'
# 100 loops, best of 5: 2.48 sec per loop
# 'task_2.sieve(5000)'
# 100 loops, best of 5: 16.8 sec per loop


# n = 500
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.004    0.004    0.146    0.146 <string>:1(<module>)
#      1    0.109    0.109    0.142    0.142 task_2.py:15(sieve)
#      1    0.023    0.023    0.023    0.023 task_2.py:21(<listcomp>)
#      1    0.010    0.010    0.010    0.010 task_2.py:31(<listcomp>)
#      1    0.000    0.000    0.146    0.146 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# n = 2000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.044    0.044    2.574    2.574 <string>:1(<module>)
#      1    2.130    2.130    2.531    2.531 task_2.py:15(sieve)
#      1    0.244    0.244    0.244    0.244 task_2.py:21(<listcomp>)
#      1    0.157    0.157    0.157    0.157 task_2.py:31(<listcomp>)
#      1    0.000    0.000    2.575    2.575 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# n = 5000
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.229    0.229   16.859   16.859 <string>:1(<module>)
#         1   14.306   14.306   16.630   16.630 task_2.py:15(sieve)
#         1    1.410    1.410    1.410    1.410 task_2.py:21(<listcomp>)
#         1    0.914    0.914    0.914    0.914 task_2.py:31(<listcomp>)
#         1    0.000    0.000   16.859   16.859 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Сложность незначительно меньшек O(n^2)

# Оптимизированный алгоритм "Решето Эратосфена" с выбором размера решета
# Если число не найдено, проводится повторый поиск на следующем сегменте чисел
def opt_sieve_segment(n, size=None):

    # Автовыбор размера
    if size is None:
        size = n

    # Из-за пропуска четных позиций размер должен быть кратен 2
    if size % 2 != 0:
        size += 1

    if n == 1:
        return 2

    right = 3
    res = []
    sieve_array = None

    while len(res) < n:

        left = right
        right = left + size

        # Чтобы не тратить дополнительно пямять, создаем новый сегмент на месте старого
        if sieve_array is not None:
            for i, num in enumerate(range(left, right)):
                sieve_array[i] = num
        else:
            sieve_array = [i for i in range(left, right)]

        # В очередном сегмента делаем дырки по найденым простым числав в прошых сегментах
        for prime in res:  # Для каждого простого числа
            for i in range(left, right, 2):  # Ищется позициия, откуда просеивать
                if i % prime == 0:  # Если число кратное, позиция найдена
                    j = i  # Делаем дырки дальше
                    while j < right:
                        sieve_array[j - left] = 0
                        j += prime
                    break

        # стандартная часть алгоритма
        # доходим до конца, т.к. не знаем сколько сегментов потребуется дальше
        for i in range(left, right, 2):
            if sieve_array[i - left] != 0:
                j = i * i - left
                while j < size:
                    sieve_array[j] = 0
                    j += i + i

        res.extend([i for i in sieve_array if i % 2 != 0])

    return res[n - 2]

# Размер решета n ** 2 как и в sieve(), поиск идет в одном сегменте

# 'task_2.opt_sieve_segment(100, 10000)':
# 100 loops, best of 5: 2.48 msec per loop
# 'task_2.opt_sieve_segment(500, 250000)':
# 100 loops, best of 5: 81 msec per loop
# 'task_2.opt_sieve_segment(2000, 4000000)':
# 100 loops, best of 5: 1.57 sec per loop
# 'task_2.opt_sieve_segment(5000, 25000000)'
# 100 loops, best of 5: 10.1 sec per loop

# Сложность уже заметно меньше O(n^2)

# Раземр решета n
# 'task_2.opt_sieve_segment(100, 100)'
# 100 loops, best of 5: 1.05 msec per loop
# 'task_2.opt_sieve_segment(500, 500)'
# 100 loops, best of 5: 33.9 msec per loop
# 'task_2.opt_sieve_segment(2000, 2000)'
# 100 loops, best of 5: 572 msec per loop
# 'task_2.opt_sieve_segment(5000, 5000)'
# 100 loops, best of 5: 4.14 sec per loop

# Сложность премерно такая же как и в opt_sieve_segment(n, n):

# Несмотря на затрату времени на стыковку сегментов, виден заметный прирост производительности
# Следовательно размер решета n * n сильно избыточен

# Профилирование для n = 500, size = n
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.038    0.038 <string>:1(<module>)
#      8    0.000    0.000    0.000    0.000 task_2.py:102(<listcomp>)
#      1    0.038    0.038    0.038    0.038 task_2.py:54(opt_sieve_segment)
#      1    0.000    0.000    0.000    0.000 task_2.py:81(<listcomp>)
#      1    0.000    0.000    0.038    0.038 {built-in method builtins.exec}
#      9    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      8    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
# Исходя из результатов определяем, что было использовано 9 сегментов

# Профилирование для n = 2000, size = n
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.588    0.588 <string>:1(<module>)
#      9    0.001    0.000    0.001    0.000 task_2.py:102(<listcomp>)
#      1    0.586    0.586    0.588    0.588 task_2.py:54(opt_sieve_segment)
#      1    0.000    0.000    0.000    0.000 task_2.py:81(<listcomp>)
#      1    0.000    0.000    0.588    0.588 {built-in method builtins.exec}
#     10    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      9    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
# Использовано 10 сегментов

# n = 5000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    4.220    4.220 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_2.py:100(<listcomp>)
#     10    0.003    0.000    0.003    0.000 task_2.py:121(<listcomp>)
#      1    4.216    4.216    4.220    4.220 task_2.py:73(opt_sieve_segment)
#      1    0.000    0.000    4.220    4.220 {built-in method builtins.exec}
#     11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     10    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
# Использовано 11 сегментов


# Алгоритм "Решето Эратосфена" с оптимизацией и выбором оптимального размера
def opt_quick_sieve(n):

    if n == 1:
        return 2

    if n > 5:
        size = int(n * log(n) + n * log(log(n)))
    else:
        size = n * n

    sieve_array = [i for i in range(size)]
    sieve_array[1] = 0

    for i in range(3, int(sqrt(size)), 2):
        if sieve_array[i] != 0:
            j = i * i
            while j < size:
                sieve_array[j] = 0
                j += i + i

    res = [i for i in sieve_array if i % 2 != 0]

    return res[n - 2]

# 'task_2.opt_quick_sieve(100)'
# 100 loops, best of 5: 94.6 usec per loop
# 'task_2.opt_quick_sieve(500)'
# 100 loops, best of 5: 693 usec per loop
# 'task_2.opt_quick_sieve(2000)'
# 100 loops, best of 5: 3.53 msec per loop
# 'task_2.opt_quick_sieve(5000)'
# 100 loops, best of 5: 10.7 msec per loop

# Сложность близка к O(n)

# Профилирование для n = 2000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#      1    0.002    0.002    0.004    0.004 task_2.py:139(opt_quick_sieve)
#      1    0.001    0.001    0.001    0.001 task_2.py:149(<listcomp>)
#      1    0.001    0.001    0.001    0.001 task_2.py:159(<listcomp>)
#      1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#      3    0.000    0.000    0.000    0.000 {built-in method math.log}
#      1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Профилирование для n = 100000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.020    0.020    0.468    0.468 <string>:1(<module>)
#      1    0.265    0.265    0.449    0.449 task_2.py:152(opt_quick_sieve)
#      1    0.105    0.105    0.105    0.105 task_2.py:162(<listcomp>)
#      1    0.079    0.079    0.079    0.079 task_2.py:172(<listcomp>)
#      1    0.000    0.000    0.468    0.468 {built-in method builtins.exec}
#      3    0.000    0.000    0.000    0.000 {built-in method math.log}
#      1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#  Каждое очередное число проверяется на простоту посредством проверки кратности найденым простым числам
def opt_simple_prime(n):

    prime_array = [2]
    number = 1

    while n > 1:

        number += 2  # Избегаем четные числа
        p = int(sqrt(number)) + 1

        for prime in prime_array:

            if prime > p:  # Если True, значит дальше число не будет кратно следующим числам
                prime_array.append(number)
                n -= 1
                break

            elif number % prime == 0:  # Если число кратно
                break  # Не подходит

        else:  # Если вышли естественным образом
            prime_array.append(number)
            n -= 1

    return prime_array[-1]

# 'task_2.opt_simple_prime(100)'
# 100 loops, best of 5: 214 usec per loop
# 'task_2.opt_simple_prime(500)'
# 100 loops, best of 5: 1.73 msec per loop
# 'task_2.opt_simple_prime(2000)'
# 100 loops, best of 5: 10 msec per loop
# 'task_2.opt_simple_prime(5000)'
# 100 loops, best of 5: 31.9 msec per loop

# Сложность так же близка к O(n)

# Профилирование для n = 2000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.016    0.016 <string>:1(<module>)
#      1    0.014    0.014    0.016    0.016 task_2.py:206(opt_simple_prime)
#      1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
#   8694    0.001    0.000    0.001    0.000 {built-in method math.sqrt}
#   1999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Профилирование для n = 100000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    2.160    2.160 <string>:1(<module>)
#      1    2.070    2.070    2.159    2.159 task_2.py:195(opt_simple_prime)
#      1    0.000    0.000    2.160    2.160 {built-in method builtins.exec}
# 649854    0.076    0.000    0.076    0.000 {built-in method math.sqrt}
#  99999    0.013    0.000    0.013    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Тест на случайно выбранных значениях
def test(func):

    data = [1, 2, 13, 37, 168]
    expected = [2, 3, 41, 157, 997]

    for i, prime in enumerate(expected):
        assert prime == func(data[i])


if TEST is True:
    for test_func in [sieve, opt_quick_sieve, opt_sieve_segment, opt_simple_prime]:
        test(test_func)
    print('test ok')

if PROFILE is True:
    cProfile.run('sieve(PROFILE_N)')
    cProfile.run('opt_sieve_segment(PROFILE_N)')
    cProfile.run('opt_quick_sieve(PROFILE_N)')
    cProfile.run('opt_simple_prime(PROFILE_N)')
