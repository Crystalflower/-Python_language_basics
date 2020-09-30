def my_func():
    num_sum = 0
    while True:
        person_answer = input(
            'Введите числа через пробел для их суммирования, для выхода - q: ')
        num_list = person_answer.split()
        for i in num_list:
            if i.lower() == 'q':
                print(num_sum)
                return 'Выход'
            else:
                num_sum += int(i)
        print(num_sum)


print('Вас приветствует сумматор чисел! ')
print(my_func())
