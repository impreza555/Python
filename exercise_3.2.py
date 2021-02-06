def user_data(name, surname, year_of_birth, city, email, phone_num):
    print(
        f'{"*" * 70}\n{name} {surname}, {year_of_birth} года рождения, город {city}, e-mail {email}, тел. {phone_num}')


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year_of_birth = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите e-mail: ')
phone_num = input('Введите номер телефона: ')
user_data(name, surname, year_of_birth, city, email, phone_num)
