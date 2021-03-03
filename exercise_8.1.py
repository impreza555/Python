class Data:
    months = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
              'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}

    @classmethod
    def conversion_to_number(cls, date):
        convert_date = []
        try:
            date_list = date.lower().split()
            if len(date_list) != 3:
                raise ValueError('Некорректный ввод!')
            for i in date_list:
                if i.isdigit():
                    convert_date.append(int(i))
                if i in Data.months:
                    convert_date.append(Data.months.get(i))
        except ValueError as exception:
            return exception

        return convert_date, cls.validation(date_list)

    @staticmethod
    def validation(date_list):
        day = date_list[0]
        month = date_list[1]
        year = date_list[2]
        answer = 'Дата корректна'
        if int(day) not in range(1, 32):
            answer = 'Неверная дата!'
        if int(day) > 30 and month in ['апреля', 'июня', 'сентября', 'ноября']:
            answer = 'В указанном месяце не может быть более 30 дней'
        if int(day) > 29 and month == 'февраля':
            answer = 'В феврале не может быть больше 29 дней'
        if month not in Data.months:
            answer = 'Неверное название месяца!'
        if int(year) < 0:
            answer = 'Год не может быть равен нулю!'
        return answer


data = input(f'Введите дату в формате дд мммм гггг \nпример: "24 апреля 1995": ')

print(Data.conversion_to_number(data))
my_data = Data()
print(my_data.conversion_to_number(data))
