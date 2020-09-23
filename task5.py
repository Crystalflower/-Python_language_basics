print('Доброго времени суток, вас приветствует экономический менеджер!')
proceeds = int(input('Введите вашу выручку: '))
costs = int(input('Введите ваши издержки: '))
if proceeds > costs:
    profit = proceeds - costs
    profitability = round(profit / proceeds, 2)
    print(f'У вас установлена прибыль - {profit}!\nРентабельность проекта - {profitability}')
    num_emp = int(input('Введите число сотрудников вашей фирмы: '))
    one_emp = round(profit / num_emp, 2)
    print(f'Каждый сотрудник получит {one_emp}, так держать!')
else:
    print(f'К сожалению, у вас обнаружен убыток - {costs - proceeds}, но не переживайте, у всех бывают взлеты и падения!')

