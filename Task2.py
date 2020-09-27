person_list = []

while True:
    try:
        how_many = int(input('Сколько объектов поместить в список?'))
        if how_many <= 0 or how_many > 100:
            print('Невозможное число, введите от 1 до 100')
        else:
            break
    except ValueError:
        print('Введено не число, попробуйте еще раз!')

count = 1
while count <= how_many:
    obj = input(f'Введите {count} объект из {how_many}: ')
    person_list.append(obj)
    count += 1
print(person_list)
if len(person_list) % 2 == 0:
    i = 0
    while i < len(person_list):
        el = person_list[i]
        person_list[i] = person_list[i+1]
        person_list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(person_list) - 1:
        el = person_list[i]
        person_list[i] = person_list[i + 1]
        person_list[i + 1] = el
        i += 2
print(person_list)