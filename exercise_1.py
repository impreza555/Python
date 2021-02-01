var_str = (input('Введите ваше имя: '))
print(f'Здравтуйте {var_str}, ваше имя имеет тип {type(var_str)}')
var_int = int(input('Введите целое число: '))
print(f'Число {var_int} имеет тип {type(var_int)}')
var_float = (var_int + 1) / var_int
print(f'А число {var_float:.2f} имеет тип {type(var_float)}')
