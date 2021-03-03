class OfficeEquipment:
    eq_count = 0

    def __init__(self, type_eq: str, name: str, model: str, price: float):
        self.type_eq = type_eq
        self.name = name
        self.model = model
        self.price = price
        self.eq_count += 1
        try:
            if type(self.price) != float:
                raise ValueError('\033[31mЦена должна быть числом!\033[0m')
        except ValueError as exception:
            print(exception)

    def __str__(self):
        return f'Тип оргтехники: {self.type_eq} | Наименование: {self.name} | Модель: {self.model} | Цена: {self.price}'

    def __add__(self, other):
        total_price = self.price + other.price
        return total_price

    def turning_on(self):
        return f'{self.type_eq} {self.name} {self.model} включен'

    def turning_off(self):
        return f'{self.type_eq} {self.name} {self.model} выключен'


class Printer(OfficeEquipment):
    pr_count = 0

    def __init__(self, *args):
        super().__init__('Принтер', *args)
        Printer.pr_count += 1

    def printing(self):
        return f'Печать страницы: Бж-ж-ж-ж, Бж-ж-ж-ж!'


class Scanner(OfficeEquipment):
    sc_count = 0

    def __init__(self, *args):
        super().__init__('Сканер', *args)
        Scanner.sc_count += 1

    def scanning(self):
        return f'Сканирование: Вж-ж-ж-ж, Вж-ж-ж-ж!'


class Copier(OfficeEquipment):
    cop_count = 0

    def __init__(self, *args):
        super().__init__('Копир', *args)
        Copier.cop_count += 1

    def copying(self):
        return f'Копирование: Пш-ш-ш-ш, Пш-ш-ш-ш!'


class MultiDevice(Printer, Scanner, Copier):
    mu_count = 0

    def __init__(self, *args):
        OfficeEquipment.__init__(self, 'МФУ', *args)
        MultiDevice.mu_count += 1


if __name__ == "__main__":
    pr1 = Printer('HP', 'DeskJet', 2500.5)
    print(pr1)
    print(pr1.turning_on())
    print(pr1.printing())
    print(pr1.turning_off())
    print(Printer.pr_count)

    sca1 = Scanner('Cannon', 'Canoscan', 1300.5)
    print(sca1)
    print(sca1.turning_on())
    print(sca1.scanning())
    print(sca1.turning_off())
    print(Scanner.sc_count)

    cop1 = Copier('Cannon', 'imageRUNNER', 7000.5)
    print(cop1)
    print(cop1.turning_on())
    print(cop1.copying())
    print(cop1.turning_off())
    print(Copier.cop_count)

    mfd1 = MultiDevice('Brother', 'DCP', 5500.3)
    print(mfd1)
    print(mfd1.turning_on())
    print(mfd1.printing())
    print(mfd1.scanning())
    print(mfd1.copying())
    print(mfd1.turning_off())
    print(MultiDevice.mu_count)
