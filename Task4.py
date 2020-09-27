person_answer = input('Введите несколько слов через пробел для их разделения: ')
list = person_answer.split()
for i in list:
    if len(i) <= 10:
        print(i)
    else:
        print(i[:10])