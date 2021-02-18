class Stationery:
    title: str

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        print(f'{self.title}. Запуск отрисовки')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print(f'{self.title}. Запуск отрисовки')


class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        print(f'{self.title}. Запуск отрисовки')


s = Stationery()
s.draw()
p = Pen()
p.draw()
pn = Pencil()
pn.draw()
h = Handle()
h.draw()
