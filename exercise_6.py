ini_result = int(input('Введите расстояние пробежки в первый день: '))
tar_result = int(input('Введите требуемый результат пробежки: '))
i = 1
inter_result = ini_result
while inter_result <= tar_result:
    inter_result = inter_result + inter_result * 0.1
    i += 1
print('Требуемый результат будет достигнут на', i, 'день')
