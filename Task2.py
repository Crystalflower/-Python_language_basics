from __future__ import print_function


def my_f(**kwargs):
    count = 0
    for i in kwargs:
        count += 1
        print(i, ':', kwargs[i], end=', ') if count < 6 else print(i, ':', kwargs[i])


my_f(name='Ekaterina', surname='Dolgaya', year_of_birth='1995', city='San-Diego', email='sup@mail.ru',
     telephone='00918983787213')
