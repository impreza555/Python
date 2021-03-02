class OffEquipWarehouse:

    def __init__(self):
        self.warehouse = []

    def __str__(self):
        return f'На складе находится сл. оргтехника:\n{"-" * 36}\n' + '\n'.join([str(x) for x in self.warehouse])

    def take_for_storage(self, item: object):
        self.item = item
        self.warehouse.append(self.item)

    def __getitem__(self, index: int):
        return self.warehouse[index]

    def accounting(self):
        total_price = 0
        quantity = 0
        i = 0
        while i < len(self.warehouse):
            quantity += self.warehouse[i].eq_count
            total_price += self.warehouse[i].price
            i += 1
        return f'{"-" * 36}\nОбщая стоимость всей оргтехники равна: {total_price}\nКоличество оргтехники: {quantity}'

    def transfer_equipment(self, item: object):
        self.item = item
        self.warehouse.remove(self.item)


if __name__ == "__main__":
    pass
