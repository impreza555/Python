some_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Исходный список:\n{"-" * 17}\n{some_list}')
new_list = [i for j, i in enumerate(some_list) if some_list[j - 1] < some_list[j]]
del new_list[0]
print(f'Новый список:\n{"-" * 17}\n{new_list}')
