class Road:
    _length: float
    _width: float

    def __init__(self, length, width):
        Road._length = float(length)
        Road._width = float(width)

    def calc_mass_asph(self, thickness):
        return round((self._length * self._width * 25 * float(thickness)) / 1000, 2)


length = input("Введите длинну: ")
width = input("Введите ширину: ")
thickness = input("Введите толщину: ")
try:
    road = Road(length, width)
    print(f'Масса асфальта равна {road.calc_mass_asph(thickness)} тонн.')
except ValueError:
    print('Ошибка ввода')
