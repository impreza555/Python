seconds = int(input('Введите количество времени в секундах: '))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = (seconds % 3600) % 60
print(f'Время в формате "чч:мм:сс" будет таким {hours}:{minutes}:{seconds}')
