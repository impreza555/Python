class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} тачка {self.name} поехала.')

    def stop(self):
        print('Тачка затормозила')

    def turn(self, direction):
        self.direction = direction
        print(f'Тачка повернула {direction}')

    def show_speed(self):
        print(f'Со скоростью {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.speed}! Превышение скорости!')
        else:
            print(f'Со скоростью {self.speed}')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость {self.speed}! Превышение скорости!')
        else:
            print(f'Со скоростью {self.speed}')


class SportCar(Car):

    def go(self):
        print(f'{self.color} тачка {self.name} сорвалась с места!')

    def show_speed(self):
        print(f'Очень быстро понеслась со скоростью {self.speed}')


class PoliceCar(Car):

    def go(self):
        if self.is_police == True:
            print(f'Полицейская {self.color} тачка {self.name} поехала.')
        else:
            print(f'{self.color} тачка {self.name} поехала.')


speed = int(input('Укажите скорость, с которой поедут автомобили: '))

taz = Car(speed, 'Синяя', 'ВАЗ')
print(taz.name)
taz.go()
taz.show_speed()
taz.turn('налево')
taz.turn('направо')
taz.stop()

taz = TownCar(speed, 'Красная', 'ВАЗ')
print(taz.name)
taz.go()
taz.show_speed()
taz.turn('налево')
taz.turn('направо')
taz.stop()

volga = PoliceCar(speed, 'Белая', 'Волга', True)
print(volga.name)
volga.go()
volga.show_speed()
volga.turn('налево')
volga.turn('направо')
volga.stop()

kamaz = WorkCar(speed, 'Оранжевая', 'КамАЗ')
print(kamaz.name)
kamaz.go()
kamaz.show_speed()
kamaz.turn('налево')
kamaz.turn('направо')
kamaz.stop()

maz = SportCar(speed, 'Желтая', 'Maserati')
print(maz.name)
maz.go()
maz.show_speed()
maz.turn('налево')
maz.turn('направо')
maz.stop()
