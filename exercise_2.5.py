origin_list = [7, 5, 3, 3, 2]
print(
    f'Реализуем структуру «Рейтинг», для исходного списка\n{origin_list}\nС возможностьб вносить новые элементы\n{"-" * 38}')
while True:
    elem = input('Введите новый элемент рейтинга, или нажмите "q" для зывершения ввода: ')
    if elem == 'q':
        break
    else:
        try:
            elem = (int(elem))
            for i in range(len(origin_list)):
                if origin_list[i] == elem:
                    origin_list.insert(i + 1, elem)
                    break
                elif origin_list[0] < elem:
                    origin_list.insert(0, elem)
                    break
                elif origin_list[-1] > elem:
                    origin_list.append(elem)
                    break
                elif origin_list[i] > elem > origin_list[i + 1]:
                    break
                    origin_list.insert(i + 1, elem)
        except ValueError:
            print('Вы должны ввести число!')
            continue
print(f'{"-" * 28}\nПолучился следующий список:\n{origin_list}')
