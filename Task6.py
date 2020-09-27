products = []
how_many = int(input('Введите колличество товаров для добавления в базу данных: '))
count = 1
how_much = int(input(f'Введите колличество характеристик {count} товара: '))
while count <= how_many:
    prod_dict = {}
    future_tuple = []
    future_tuple.append(input(f'Введите товарный номер {count} товара: '))
    count_prod = 1
    while count_prod <= how_much:
        key = input(f'Введите {count_prod} характеристику {count} товара: ')
        value = input(f'Введите данные для нее: ')
        prod_dict.update({key: value})
        count_prod += 1
    future_tuple.append(prod_dict)
    now_tuple = tuple(future_tuple)
    products.append(now_tuple)
    count += 1
print(products)

result = {}
for i in products:
    for key, value in i[1].items():
        if key not in result:
            result[key] = [value]
        else: result[key].append(value)
print(result)


