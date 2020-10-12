# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Ваша ручка самостоятельно отрисовывает проект!')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш воссоздает картину Ван Гога, подождите.')


class Handle(Stationery):
    def draw(self):
        print(f'Не Бэнкси, но маркер {self.title} в процессе нанесения граффити.')


hand = Handle('Бик')
hand.draw()
pensil = Pencil('Графикс')
pensil.draw()
pen = Pen('Пилот')
pen.draw()
noname = Stationery('Фабер кастелл')
noname.draw()
