from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(my_list)


def factor(prev_el, el):
    return prev_el * el


print(reduce(factor, my_list))
