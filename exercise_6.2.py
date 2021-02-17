class Road:
    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def calc_mass_asph(self, thickness):
        return round((self._length * self._width * 25 * float(thickness)) / 1000, 2)


length = input("Введите длинну: ")
width = input("Введите ширину: ")
try:
    road = Road(length, width)
    print(f'Масса асфальта равна {road.calc_mass_asph(input("Введите толщину: "))} тонн.')
except ValueError:
    print('Ошибка ввода')
