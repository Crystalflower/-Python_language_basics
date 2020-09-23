time_now = int(input('Запишите время в секундах, а я переведу их в чч:мм:сс - '))
second_now = time_now % 60
minute = time_now // 60
minute_now = minute % 60
hour_now = minute // 60
print(f'Текущее время: {hour_now}:{minute_now}:{second_now}.')