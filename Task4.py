def my_func(x, y):
    # return x ** y
    count = 1
    z = 1 / x
    while count < abs(y):
        z *= (1 / x)
        count += 1
    return (z)


print(my_func(2, -6))
