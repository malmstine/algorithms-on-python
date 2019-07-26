# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter, namedtuple, deque
from functools import reduce


class Node:

    def __init__(self, value, left=None, right=None):

        self.value = value
        self.left = left
        self.right = right

    def __str__(self):

        return f'Node({self.value})'

    def __repr__(self):

        return f'Node({self.value}, {self.left.__str__()} : {self.right.__str__()})'


# Составлиние словаря для кодирования по дереву
def get_dict(three):

    huffman_dict = {}

    def set_dict(node_three, path=''):

        if node_three.left is None:
            huffman_dict[node_three.value] = path
        else:
            set_dict(node_three.left, path + '0')
            set_dict(node_three.right, path + '1')

    set_dict(three)
    return huffman_dict


# Кодирование строки
def encode_huffman(endoding_st, enc_dict):

    return reduce(lambda a, x: a + enc_dict[x], endoding_st, '')


# Декодивание строки
def decode_huffman(decoding_st, dec_dict):

    code = ''
    res = ''

    for c in decoding_st:

        if dec_dict.get(code) is not None:  # Если в словаре есть такой символ
            res += dec_dict.get(code)
            code = ''
        code += c

    return res + dec_dict[code]


# Составление дерева по строке
def get_three(sting):

    # В узле дерева хранить будем именованный кортеж с символом и его частотой
    Frequency = namedtuple('Frequency', ['v', 'f'])  # Господи, как раньше мне не хватало такой штуки
    nodes = deque()

    # Заполняем очередь
    for v, f in Counter(sting).most_common():
        nodes.appendleft(Frequency(Node(v), f))

    while len(nodes) != 1:  # Если в очереди есть символ или узел
        # Забираем их
        a = nodes.popleft()
        b = nodes.popleft()

        # Помещаем в новый узел
        current_f = Frequency(Node(None, a.v, b.v), a.f + b.f)

        # Ищем куда вставить
        for i, p in enumerate(nodes):
            if p.f >= current_f.f:  # Если в очереди есть что-то с такой же или большей частотой
                nodes.insert(i, current_f)  # Вставляем на его место
                break
        else:
            nodes.append(current_f)   # Если такой частоты еще не было, вставляем в конец

    return nodes.pop().v


st = 'beep boop beer!'
print('Исходная строка: ', st)

encode_dict = get_dict(get_three(st))
decode_dict = {value: key for key, value in encode_dict.items()}
print('Таблица символов: ', encode_dict)

encode_st = encode_huffman(st, encode_dict)
print('Закодированная строка: ', encode_st)

decode_st = decode_huffman(encode_st, decode_dict)
print('Обтаное преобразование: ', decode_st)

if st == decode_st:
    print('Сжатие прошло успешно')
    print(f'Сжатие: {len(st) * 8 / len(encode_st)  * 100:.2f} %')
else:
    print('Упс! Что-то пошло не так')
