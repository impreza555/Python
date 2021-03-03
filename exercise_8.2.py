class ErrorZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


try:
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))
    if b == 0:
        raise ErrorZeroDivision('Делитиь на ноль нельзя! В этом измерении...')
    c = a / b
except ValueError:
    print('Вы дожны ввести число!')
except ErrorZeroDivision as exception:
    print(exception)
else:
    print(c)
finally:
    print('Программа завершена.')
