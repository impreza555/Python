from time import sleep


class TrafficLight:
    _color = [f'\033[31mКрасный', f'\033[33mЖелтый', f'\033[32mЗелёный']

    def running(self):
        i = 0
        for switch_time in [7, 2, 8]:
            color = self._color[i]
            print(f'Включился {color}\033[0m цвет!')
            i += 1
            sleep(switch_time)


tr = TrafficLight()
tr.running()
