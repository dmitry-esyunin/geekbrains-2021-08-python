# Урок 5. Работа с файлами
# 
# 7. Создать (не программно) текстовый файл, в котором каждая строка 
# должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, 
# а также среднюю прибыль. 
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
# а также словарь со средней прибылью. Если фирма получила убытки, 
# также добавить ее в словарь (со значением убытков).
# 
# Пример списка: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# 
# Подсказка: использовать менеджеры контекста.
#
import json


def get_companies(file):
    result = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            row = line.split()
            company = '_'.join(row[:-3])
            form = row[-3]
            revenue = float(row[-2])
            costs = float(row[-1])
            result[company] = revenue - costs
            print(f'company={company}, form={form}, revenue= {revenue}, costs= {costs}, profit= {result[company]}')

    profit_positivity = [result[item] for item in result if result[item] > 0]
    average_profit = 0 if len(profit_positivity) == 0 else sum(profit_positivity) / len(profit_positivity)
    return [result, {'average_profit': average_profit}]


def save_to_json(data, file):
    with open(file, "w") as f:
        json.dump(data, f)


data = get_companies('task07.txt')
print(data)
save_to_json(data, 'task07.json')


