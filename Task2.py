# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def square(self):
        return square


class Coat(Clothing):
    def __init__(self, name, V):
        super().__init__(name)
        self.V = V

    @property
    def square(self):
        return (f'Площадь пальто = {round((int(self.V) / 6.5 + 0.5), 2)} м.')


class Suit(Clothing):
    def __init__(self, name, H):
        super().__init__(name)
        self.H = H

    @property
    def square(self):
        return (f'Площадь костюма = {2 * int(self.H) + 0.3} м.')


class Summa(Coat, Suit):
    def __init__(self, V, H):
        self.V = V
        self.H = H

    def sum_sq(self):
        return (f'Общая площадь = {round((int(self.V) / 6.5 + 0.5) + (2 * int(self.H) + 0.3), 2)} м.')


one = Suit('victoria', 5)
two = Summa(10, 10)
print(one.square)
three = Coat('victoria', 4)
print(three.square)
print(two.sum_sq())
