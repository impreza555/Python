my_list = [-47, 12.348, {'Вашингтон', 15, False}, True, [13, 'Зима'], 'Вася Пупкин', None, ('Осень', 34, True), {'Имя': 'Вася', 'Фамилия': 'Пупкин'}]
print(f'Имеем следующий список:\n{"-" * 24}\nmy_list = {my_list}\n{"-" * 150}')
n = 1
for i in my_list:
    print(f'{n}-й элемент списка "{i}" имеет тип "{type(i)}"')
    n += 1
