

import random


class Card:
    def __init__(self, name):
        self.name = name
        self.count = 0
        self.generate()

    def generate(self):
        nums = []
        for i in range(0, 15, 5):
            mini_nums = []
            for i in range(5):
                num = random.randint(1, 91)
                while num in mini_nums or num in nums:
                    num = random.randint(1, 91)
                mini_nums.append(num)
            mini_nums = sorted(mini_nums)
            for i in range(4):
                mini_nums.insert(random.randint(0, 10), ' ')
            nums += mini_nums
        self.result = nums


    def out(self):
        print('-' * 5, self.name, '-' * (29 - len(self.name)))
        print('%4s' * 9 % tuple(self.result[0:9]))
        print('%4s' * 9 % tuple(self.result[9:18]))
        print('%4s' * 9 % tuple(self.result[18:27]))
        print('-' * 36)


class Game:
    def __init__(self, name_1):
        self.player1 = Card(name_1)
        self.computer = Card('computer')
        self.go()

    def check(self, obj, list):
        val = False
        for i in range(27):
            if list.result[i] != ' ':
                if list.result[i] == obj:
                    list.result[i] = '-'
                    val = True
        return val

    def go(self):
        print(f'Начало игры в лото.')
        a = []
        for i in range(1, 91):
            a.append(i)
        while True:
            self.player1.out()
            self.computer.out()
            num = random.choice(a)
            a.remove(num)
            print(f'Выпавшее число {num}! Осталось {len(a)}.')
            answer = ''
            while answer != 'y' and answer != 'n':
                answer = input('Присутствует оно у вас? (y/n): ')

            val1 = self.check(num, self.player1)

            if answer == 'y' and val1 == True:
                self.player1.count += 1
            elif answer == 'y' and val1 == False:
                print(f'Игрок {self.player1.name} проиграл за ложь!')
                break
            elif answer == 'n' and val1 == True:
                print(f'Игрок {self.player1.name} проиграл за ложь!')
                break

            if self.check(num, self.computer):
                self.computer.count += 1


            if (self.player1.count == 15):
                print('Выиграл игрок, поздравляем! У вас хорошее трпение.')
                break

            if (self.computer.count == 15):
                print('Вам не повезло, искусственный интеллект одержал победу :(')
                break


one = Game('Kate')
