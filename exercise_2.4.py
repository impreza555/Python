user_string = input('Введите несколько слов через пробелы.\nНапример какое-нибудь предложение: ')
user_string_list = user_string.split()
count = 1
for i in user_string_list:
    print(f'{count}). {i[:10]}')
    count += 1
