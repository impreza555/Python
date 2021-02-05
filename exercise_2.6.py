print(f'Создадим структуру данных «Товары»\n{"*" * 35}')
features = {'Название': '', 'Цена': '', 'Количество': '', 'Единицы': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Единицы': []}
feature = None
control = None
while True:
    control = input('Для выхода нажмите "Q", Для продолжения нажмите "Enter", Для вывода аналитики нажмите "A"').upper()
    if control == 'Q':
        break
    if control == 'A':
        print(f'\nТекущая аналитика:\n{"-" * 19}')
        for key, value in analytics.items():
            print(f'{key}: {set(value)}') if key == 'Единицы' else print(f'{key}: {value}')
    for f in features.keys():
        feature = input(f'Введите "{f}" товара: ')
        features[f] = feature
        analytics[f].append(features[f])
