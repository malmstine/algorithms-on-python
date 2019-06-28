# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве. Примечание к задаче:
# пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.


import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

target_num = 0
index = None

while len(array):

    num = array.pop()
    if num < 0:
        target_num = num
        break

for i, num in enumerate(array):

    if num < 0 and target_num < num:
        index = i
        target_num = num

if target_num != 0:

    if index is None:
        index = len(array)
    print(index, target_num)

else:
    print('Отрицательных чисел нет')
