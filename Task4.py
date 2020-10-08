# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на
# чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


with open('task4.txt', 'r', encoding='utf-8') as numbers:
    for line in numbers:
        if 'One' in line:
            print(f'Один{line[3:]}', end='')
        elif 'Two' in line:
            print(f'Два{line[3:]}', end='')
        elif 'Three' in line:
            print(f'Три{line[5:]}', end='')
        elif 'Four' in line:
            print(f'Четыре{line[4:]}', end='')
