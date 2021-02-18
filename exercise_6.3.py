class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'оклад': wage, 'премия': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Сотрудник {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход составляет {sum(self._income.values())}')


pos = Position('Василий', 'Пупкин', 'младший помошник старшего дворника', 15000, 2000)
print(pos.name)
print(pos.surname)
print(pos.position)
pos.get_full_name()
pos.get_total_income()
