def share_func(num_1, num_2):
    result = num_1 / num_2
    return result

while True:
    answ_1 = int(input('Вас приветствует программа деления чисел! Введите первое число для деления на второе: '))
    answ_2 = int(input('А теперь второе число: '))
    try:
        print('Ваш результат:', round(share_func(answ_1, answ_2), 2))
        break
    except ZeroDivisionError:
        print('На ноль делить нельзя! Попробуйте еще раз.')