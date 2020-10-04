from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

score = 1
new_list = [2, 23, 44]
for i in cycle(new_list):
    if score > 9:
        break
    else:
        print(i)
        score += 1