def division(*args):
    while True:
        try:
            dividend = float(input('Введите делимое: '))
            break
        except ValueError:
            print('Вы должны ввести число!')
    while True:
        try:
            divider = float(input('Введите делитель: '))
            if divider == 0.0:
                print('Делить на "0" нельзя! ...в этом измерении...')
                continue
            break
        except ValueError:
            print('Вы должны ввести число!')

    return round(dividend / divider, 3)


print(f'Резуьтат: {division()}')
