print(f'Создадим список из произвольных элементов\nМожно вводить строки натуральные и дробные числа\n{"-" * 49}')
user_list = []
j = 0
while True:
    elem = input('Введите элемент списка, или нажмите "Q" для зывершения ввода: ')
    if elem.upper() == 'Q':
        break
    else:
        try:
            if '.' in elem:
                user_list.append(float(elem))
            else:
                user_list.append(int(elem))
        except ValueError:
            user_list.append(elem)
print(f'Получили следующий список:\n{user_list}\nТеперь попарно поменяем местами элементы в списке')
for i in range(int(len(user_list) / 2)):
    user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
    j += 2
print(f'{"-" * 50}\nПолучили новый список:\n{user_list}')
