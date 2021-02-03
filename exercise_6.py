ini_result = int(input('Введите расстояние пробежки в первый день: '))
tar_result = int(input('Введите требуемый результат пробежки: '))
i = 1
while ini_result <= tar_result:
    ini_result = ini_result + ini_result * 0.1
    i += 1
print('Требуемый результат будет достигнут на', i, 'день')
