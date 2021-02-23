from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @property
    @abstractmethod
    def calc_fabric_consumption(self):
        pass

    @property
    @abstractmethod
    def total_fabric_consumption(self):
        pass

    @property
    def all_clothes_fabric(self):
        pass


class Clothes(AbstractClothes):
    all_clothes_fabric_consumption = []

    def __init__(self, quantity, clothing_size):
        self.quantity = quantity
        self.clothing_size = clothing_size
        self.all_clothes_fabric_consumption.append(self)

    @property
    def calc_fabric_consumption(self):
        pass

    def total_fabric_consumption(self):
        return round(self.calc_fabric_consumption() * self.quantity, 2)

    def all_clothes_fabric(self):
        return sum([item.total_fabric_consumption() for item in self.all_clothes_fabric_consumption])


class Coat(Clothes):
    def __init__(self, quantity, clothing_size):
        super().__init__(quantity, clothing_size)

    def calc_fabric_consumption(self):
        return round(self.clothing_size / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Пальто, размер {self.clothing_size} количество {self.quantity}'


class Suit(Clothes):
    def __init__(self, quantity, clothing_size):
        super().__init__(quantity, clothing_size)

    def calc_fabric_consumption(self):
        return round(2 * self.clothing_size + 0.3, 2)

    def __str__(self):
        return f'Костюм, рост {self.clothing_size} количество {self.quantity}'


coat = Coat(5, 52)
print(coat)
print(f'Для пошива одного пальто требуется: {coat.calc_fabric_consumption()}')
print(f'Для пошива {coat.quantity} пальто требуется: {coat.total_fabric_consumption()}')

suit = Suit(3, 5)
print(suit)
print(f'Для пошива одного костюма требуется: {suit.calc_fabric_consumption()}')
print(f'Для пошива {suit.quantity} пальто требуется: {suit.total_fabric_consumption()}')
print(f'Общая площадь ткани для всей одежды: {suit.all_clothes_fabric()}')
