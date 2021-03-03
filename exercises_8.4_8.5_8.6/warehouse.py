import offequip


class WarehouseError(Exception):
    def __init__(self, text):
        self.text = text


class OffEquipWarehouse:

    def __init__(self):
        self.warehouse = []

    def __str__(self):
        return f'На складе находится сл. оргтехника:\n{"-" * 36}\n' + '\n'.join([str(x) for x in self.warehouse])

    def take_for_storage(self, item: object):
        self.item = item
        try:
            if not isinstance(item, offequip.OfficeEquipment):
                raise WarehouseError(f'\033[31m{item} не оргтехника\033[0m')
        except WarehouseError as exception:
            print(exception)
        self.warehouse.append(self.item)

    def __getitem__(self, index: int):
        return self.warehouse[index]

    def accounting(self):
        total_price = 0
        quantity = 0
        index = 0
        while index < len(self.warehouse):
            quantity += self.warehouse[index].eq_count
            total_price += self.warehouse[index].price
            index += 1
        return f'{"-" * 36}\nОбщая стоимость всей оргтехники равна: {total_price}\nКоличество оргтехники: {quantity}'

    def transfer_equipment(self, item: object):
        self.item = item
        self.warehouse.remove(self.item)


if __name__ == "__main__":
    pass
