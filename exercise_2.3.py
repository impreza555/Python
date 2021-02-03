# Решение через список
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
              'Декабрь']
month = abs(int(input('Введите номер месяца от "1" до "12": ')))
if month < 1 or month > 12:
    print('Такого месяца не существует')
elif month == 1 or month == 2 or month == 12:
    print(f'Месяц {month_list[month - 1]} относится ко времени года {season_list[0]}')
elif month == 3 or month == 4 or month == 5:
    print(f'Месяц {month_list[month - 1]} относится ко времени года {season_list[1]}')
elif month == 6 or month == 7 or month == 8:
    print(f'Месяц {month_list[month - 1]} относится ко времени года {season_list[2]}')
elif month == 9 or month == 10 or month == 11:
    print(f'Месяц {month_list[month - 1]} относится ко времени года {season_list[3]}')

# Решение через словарь
months_dict = {
    'Зима': ('Декабрь', 'Январь', 'Февраль'),
    'Весна': ('Март', 'Апрель', 'Май'),
    'Лето': ('Июнь', 'Июль', 'Август'),
    'Осень': ('Сентябрь', 'Октябрь', 'Ноябрь')
}
month = abs(int(input('Введите номер месяца от "1" до "12": ')))
if month < 1 or month > 12:
    print('Такого месяца не существует')
elif month == 12:
    print(
        f'Месяц {months_dict[list(months_dict.keys())[0]][0]} относится ко времени года {list(months_dict.keys())[0]}')
elif month in (1, 2):
    print(
        f'Месяц {months_dict[list(months_dict.keys())[0]][month]} относится ко времени года {list(months_dict.keys())[0]}')
elif month in (3, 4, 5):
    print(
        f'Месяц {months_dict[list(months_dict.keys())[1]][month - 3]} относится ко времени года {list(months_dict.keys())[1]}')
elif month in (6, 7, 8):
    print(
        f'Месяц {months_dict[list(months_dict.keys())[2]][month - 6]} относится ко времени года {list(months_dict.keys())[2]}')
elif month in (9, 10, 11):
    print(
        f'Месяц {months_dict[list(months_dict.keys())[3]][month - 9]} относится ко времени года {list(months_dict.keys())[3]}')
