# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

with open('task2.txt', 'r', encoding='utf-8') as my_f:
    # count_lines = 0
    # my_list = []
    # for line in my_f:
    #     count_lines += 1
    #     my_list.append(line.split())
    # list_count = []
    # for line in my_list:
    #     count_word = 0
    #     for word in line:
    #         count_word += 1
    #     list_count.append(count_word)
    for line, value in enumerate(my_f, 1):
        (print(f'В {line} строке - {len(value.split())} слов(а).'))
    print(f'В файле {line} строк(и)!')

# print(f'В указанном файле {count_lines} строк(и)!')
# new_count = 1
# while new_count <= count_lines:
#     print(f'В {new_count} строке {list_count[new_count - 1]} слов(а).')
#     new_count += 1
