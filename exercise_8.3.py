class NotDigit(Exception):
    def __init__(self, text):
        self.text = text


some_list = []
while True:
    try:
        user_input = input(f'Введите число или введите\n"stop" для завершения ввода: ').lower()
        if user_input == 'stop':
            break
        if user_input.isdigit():
            some_list.append(user_input)
        else:
            raise NotDigit(f'Нужно вводить только числа')
    except NotDigit as exception:
        print(exception)
print(some_list)
