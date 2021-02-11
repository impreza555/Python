some_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Исходный список:\n{"-" * 17}\n{some_list}')
new_list = [i for i in some_list if some_list.count(i) == 1]
print(f'Новый список:\n{"-" * 17}\n{new_list}')
