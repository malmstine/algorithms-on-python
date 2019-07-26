# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход
# функции дана строка. Требуется вернуть количество различных подстрок в этой строке.

from itertools import combinations


def calc_sub_str(st):

    hash_set = set()

    for left, right in combinations(range(0, len(st) + 1), 2):
        hash_set.add(hash(st[left:right]))

    return len(hash_set) - 1  # Добавлялись все подстроки, ключаяя уникальную целую строку, ее и вычитаем


print(calc_sub_str('papa'))
print(calc_sub_str('sova'))
