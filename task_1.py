# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

QUARTERS = 4

enterprises = []
Enterprise = namedtuple('Enterprise', ['name', 'profit'])
sum_profit = 0

count = int(input('Введите количество предприятий: '))

for i in range(count):

    name = input(f'Введите наименование {i + 1} предприятия: ')
    profit = 0

    for quarter in range(QUARTERS):
        profit += int(input(f'Введите прибыль за {quarter + 1} квартал: '))

    enterprises.append(Enterprise(name=name, profit=profit))
    sum_profit += profit

avg_profit = sum_profit / count

unsuccessful_enterprises = []

for enterprise in enterprises:

    if enterprise.profit > avg_profit:
        print(f'Прибыль предприятия {enterprise.name} выше среднего на {enterprise.profit - avg_profit}')
    else:
        unsuccessful_enterprises.append(enterprise)

for enterprise in unsuccessful_enterprises:
    print(f'Прибыль предприятия {enterprise.name} ниже среднего на {avg_profit - enterprise.profit}')
