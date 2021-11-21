# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json
profit_dict = {}
profit = 0
i = 0

with open('task07.txt', 'r') as file:
    for line in file:
        name, firm, revenue, expenses = line.split()
        profit_dict[name] = float(revenue) - float(expenses)
        if profit_dict[name] >= 0:
            profit = profit + profit_dict[name]
            i += 1
    if i != 0:
        average_profit = profit / i
        print(f'Средняя прибыль - {average_profit}')
    else:
        print(f'Все фирмы работают в убыток')
    average_profit_dict = {'average_profit': round(average_profit)}
    x = [profit_dict, average_profit_dict]
    print(x)

with open('task07.json', 'w') as file_json:
    json.dump(x, file_json)
