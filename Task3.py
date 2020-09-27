winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [5, 7, 8]
autumn = [9, 10, 11]

person_answer = int(input('Введите месяц в числовом формате для вывода времени года от 1 до 12: '))
if person_answer in winter:
    print('Это зима!')
elif person_answer in spring:
    print('Весна!')
elif person_answer in summer:
    print('Это лето!')
elif person_answer in autumn:
    print('Это осень!')

seasons_dict = {1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето",8: "лето", 9: "осень", 10: "осень", 11: "осень", 12: "зима"}
print(seasons_dict.get(person_answer))