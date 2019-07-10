# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict, deque

ENCODE_HEX = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

DECODE_HEX = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}


def hex_sum(a, b):
    res = ENCODE_HEX[a] + ENCODE_HEX[b]
    return DECODE_HEX[res // 16], DECODE_HEX[res % 16]


def hex_mul(a, b):
    res = ENCODE_HEX[a] * ENCODE_HEX[b]
    return DECODE_HEX[res // 16], DECODE_HEX[res % 16]


# Каждое число представляем как словарь, где ключ - разряд цифры
# add_dict добавляет число в такой словарь, таким образом в словаре хранятся несколько чисел
# Числа сохранненые в таком словаре удобно складывать
def add_dict(digits_dic, lst, start=0):

    for i, num in enumerate(reversed(lst), start=start):
        digits_dic[i].append(num)

    return digits_dic


# Сложение чисел
def sum_digits_dic(digits_dic):

    # получаем все разряды
    digits = list(digits_dic.keys())
    digits.reverse()

    res = deque()

    # Обрабатываем эти разряды. В процессе могут добавляться новые разряды, обработанный разряды удаляются
    while len(digits) != 0:

        p = digits.pop()  # Получаем очередной разряд
        acc = '0'  # Сумма цифр этого разряда

        cur_digits = digits_dic[p]  # Цифры этого разряда
        for i in cur_digits:
            x, acc = hex_sum(acc, i)
            if x != '0':  # Если был перенос разряда
                if len(digits_dic[p + 1]) == 0:  # Если перенос в пустой разряд
                    digits.append(p + 1)  # Добавляем в обрабатываемые разряды
                digits_dic[p + 1].append(x)

        res.appendleft(acc)

    return list(res)


one = list(input('Введите перое число: '))
two = list(input('Введите второе число: '))

digits_dic = add_dict(add_dict(defaultdict(list), one), two)
print(f'Сумма чисел {sum_digits_dic(digits_dic)}')

digits_dic = defaultdict(list)
for one_i, one_n in enumerate(reversed(one)):
    for two_i, two_n in enumerate(reversed(two)):
        add_dict(digits_dic, list(hex_mul(one_n, two_n)), one_i + two_i)

print(f'Произведение чисел: {sum_digits_dic(digits_dic)}')
