# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

import random


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, 'поехала.')

    def stop(self):
        print(self.name, 'притормозила')

    def turn(self, direction):
        print(f'Крутой поворот {direction}')

    def show_speed(self):
        print(self.name, random.randrange(0, self.speed), 'км/ч')


class Towncar(Car):
    def show_speed(self):
        speed = random.randrange(0, self.speed)
        print(self.name, speed, 'км/ч')
        if speed > 60:
            print('Вы превысили скорость! Разрешенная 60 км/ч!')


new_car = Towncar(220, 'голубая', 'Тойота камри')
new_car.show_speed()
new_car.go()
new_car.turn('налево')
print(new_car.is_police)


class Workcar(Car):
    def show_speed(self):
        speed = random.randrange(0, self.speed)
        print(self.name, speed, 'км/ч')
        if speed > 40:
            print('Вы превысили скорость! Разрешенная 40 км/ч!')


second_car = Workcar(115, 'черная', 'Газель')
second_car.show_speed()
second_car.stop()
second_car.turn('направо')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


fast_car = SportCar(330, 'желтая', 'Порше турбо')
police_car = PoliceCar(315, 'серебристая', 'Ниссан скайлайн', True)

fast_car.show_speed()
police_car.show_speed()
print(police_car.is_police)
