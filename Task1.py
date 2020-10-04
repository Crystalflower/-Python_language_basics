from sys import argv


def salary(prod, rate, prem):
    return (float(prod) * float(rate)) + float(prem)


try:
    script_name, production, wage_rate, premium = argv
    print(f'Вас приветствует функция расчета ЗП. По формуле ваша зарплата = {salary(production, wage_rate, premium)}')
except ValueError:
    print('Введите ваши данные после названия скрипта: выработка в часах, ставка в час и премия.')
