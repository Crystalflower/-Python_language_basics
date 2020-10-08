# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль
# каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать.
#
# Далее реализовать список. Он должен содержать словарь с
# фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

with open('task7.txt', 'r', encoding='utf-8') as profit:
    result = []
    dict_res = {}
    count_pos = 0
    s_prof = 0
    for line in profit:
        diff = int(line.split()[2]) - int(line.split()[3])
        if diff > 0:
            dict_res[line.split()[0]] = diff
            s_prof += diff
            count_pos += 1
    result.append(dict_res)
    sec_dict = {'average_profit': s_prof / count_pos}
    result.append(sec_dict)
with open('task7_res.json', 'w', encoding='utf-8') as task_res:
    json.dump(result, task_res)
