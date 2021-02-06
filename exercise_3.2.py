def user_data(name, surname, year_of_birth, city, email, phone_num):
    """
    Функция принимает данные пользователя: имя, фамилия, год рождения,
    город проживания, email, телефон, и выводит одной строкой.
    """
    print(
        f'{"*" * 70}\n{name} {surname}, {year_of_birth} года рождения, город {city}, e-mail {email}, тел. {phone_num}')


user_data(name=input('Введите имя: '), surname=input('Введите фамилию: '),
          year_of_birth=input('Введите год рождения: '), city=input('Введите город проживания: '),
          email=input('Введите e-mail: '), phone_num=input('Введите номер телефона: '))
