# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matr):
        self.matrix = matr

    def __str__(self):
        return '\n'.join(str(i).replace(',', ' ').replace('[', '').replace(']', '') for i in self.matrix) + '\n'

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            new_matrix = []
            mini_matrix = []
            count1 = 0
            count2 = 0
            for i in self.matrix:
                count2 = 0
                mini_matrix = []
                for j in i:
                    mini_matrix.append(self.matrix[count1][count2] + other.matrix[count1][count2])
                    count2 += 1
                new_matrix.append(mini_matrix)
                count1 += 1
            return '\n'.join(str(i).replace(',', ' ').replace('[', '').replace(']', '') for i in new_matrix) + '\n'
        else:
            return "Нельзя складывать матрицы разного размера!"


one = Matrix([[1, 1], [2, 2], [3, 3]])

two = Matrix([[1, 1], [1, 1], [1, 1]])
print(one + two)
print(one)
