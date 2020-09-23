max_num = 1
person_num = (input('Введите целое положительное число для вывода максимальной цифры в нем: '))
count = 0
while len(person_num) > count:
    if int(person_num[count]) > max_num:
        max_num = int(person_num[count])
    count += 1
print(max_num)

#2 вариант решения

enter_num = int(input('Введите целое положительное число для вывода максимальной цифры в нем: '))
m_num = enter_num % 10
enter_num = enter_num // 10
while enter_num > 0:
    if enter_num % 10 > m_num:
        m_num = enter_num % 10
    enter_num = enter_num // 10
print(m_num)