rate = [7, 5, 3, 3, 2]
person_answ = int(input('Введите число от 0 до 9 для добавления в рейтинговую систему: '))
if person_answ in rate:
    index = rate[::-1].index(person_answ)
    print(index)
    rate.insert(-index, person_answ)
elif person_answ > rate[0]:
    rate.insert(0, person_answ)
else:
    rate.append(person_answ)
print(rate)