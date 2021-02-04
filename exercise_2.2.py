print(f'Создадим список из произвольных элементов\n{"-" * 42}')
user_list = []
j = 0
while True:
    elem = input('Введите элемент списка, или нажмите "q" для зывершения ввода: ')
    if elem == 'q':
        break
    else:
        try:
            user_list.append(int(elem))
        except ValueError:
            user_list.append(elem)
print(f'Получили следующий список:\n{user_list}\nТеперь попарно поменяем местами элементы в списке')
for i in range(int(len(user_list) / 2)):
    user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
    j += 2
print(f'{"-" * 50}\nПолучили новый список:\n{user_list}')
