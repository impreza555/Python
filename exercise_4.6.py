from itertools import count
from itertools import cycle

for i in count(3):
    if i >= 11:
        break
    else:
        print(i, end=', ')
print(f'\n{"*" * 24}')
some_list = ['Вася Пупкин', True, 555, None]
c = 0
for j in cycle(some_list):

    if c >= 10:
        break
    else:
        print(j)
        c += 1
