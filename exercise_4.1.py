from sys import argv

_, out_hours, rate_hour, prize = argv
try:
    print(f'Зар. плата равна: {float(out_hours) * float(rate_hour) + float(prize)}')
except ValueError:
    print('Требуется вводить числа')
