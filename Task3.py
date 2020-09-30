def my_func(num1, num2, num3):
    my_list = [num1, num2, num3]
    one_max = max(my_list)
    my_list.remove(one_max)
    two_max = max(my_list)
    return one_max + two_max


print(my_func(10, 77, 1))
