def int_func(word):
    return word.title()


print(int_func('hello'))

person_word = input('Введите несколько слов на английском в нижнем регистре: ')
print(int_func(person_word))
