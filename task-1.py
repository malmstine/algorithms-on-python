# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9

FIRST_NUM = 2
LAST_NUM = 99

FIRST_M_NUM = 2
LAST_M_NUM = 9

lst = [0 for _ in range(LAST_M_NUM - FIRST_M_NUM + 1)]
m_list = [i for i in range(FIRST_M_NUM, LAST_M_NUM + 1)]

for num in range(FIRST_NUM, LAST_NUM):

    for i in m_list:

        if num % i == 0:
            lst[i - FIRST_M_NUM] += 1

print(f'Для диапазона от {FIRST_NUM} до {LAST_NUM} чисел кратных')
for i, count in enumerate(lst):
    print(f'{i + FIRST_M_NUM}: {count}')