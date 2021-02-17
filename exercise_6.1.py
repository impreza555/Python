from time import sleep


class TrafficLight:
    _color = [f'\033[31mКрасный\033[0m', f'\033[33mЖелтый\033[0m', f'\033[32mЗелёный\033[0m']

    def running(self):
        i = 0
        for switch_time in [7, 2, 8]:
            color = self._color[i]
            print(f'Включился {color} цвет!')
            i += 1
            sleep(switch_time)


tr = TrafficLight()
tr.running()
