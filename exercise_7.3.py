class Cell:
    count = 0

    def __init__(self, num_cell: int):
        self.num_cell = int(num_cell)

    def __str__(self):
        return f'Количество ячеек:\n{self.num_cell * "*"}'

    def __add__(self, other):
        return Cell(self.num_cell + other.num_cell)

    def __sub__(self, other):
        diff_cell = Cell(self.num_cell - other.num_cell)
        return diff_cell if (self.num_cell - other.num_cell > 0) else f'Разность меньше нуля'

    def __mul__(self, other):
        return Cell(self.num_cell * other.num_cell)

    def __truediv__(self, other):
        return Cell(round(self.num_cell / other.num_cell))

    def make_order(self, cell_row):
        Cell.count += 1

        row = ''
        for i in range(int(self.num_cell / cell_row)):
            row += f'{"*" * cell_row}\n'
        row += f'{"*" * (self.num_cell % cell_row)}'
        return f'Организовать ячейки клетки {Cell.count} по рядам:\n{row}'


cell_1 = Cell(15)
cell_2 = Cell(9)
print(cell_1)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 / cell_2)
print(cell_2 / cell_1)
print(cell_1 * cell_2)
print(cell_2.make_order(5))
print(cell_1.make_order(10))
cell_3 = cell_1 * cell_2
print(cell_3.make_order(18))
