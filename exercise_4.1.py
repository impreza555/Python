from sys import argv

_, hours_worked, rate_hour, bonus = argv
try:
    print(f'Зар. плата равна: {float(hours_worked) * float(rate_hour) + float(bonus)}')
except ValueError:
    print('Требуется вводить числа')
