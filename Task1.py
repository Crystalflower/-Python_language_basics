#1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

list = []
while True:
    person_answ = input('Введите строку для записи в файл: ')
    if person_answ == '':
        break
    list.append(person_answ + '\n')
print(list)

with open('text_file.txt', 'w') as new_file:
    new_file.writelines(list)