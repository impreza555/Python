def number_sum():
    """
    Функцмя запрашивает у пользователя строку чисел, разделенных пробелом.
    При нажатии Enter выводиться сумма чисел.
    Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
    Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
    Если вводится символ "Q", выполнение программы завершается.

    """
    result_sum = 0
    sel = True
    while sel == True:
        user_input = input('Ввведите несколько чисел через пробел либо введите "Q", если хотите выйти: ').split()
        tmp_sum = 0
        for i in range(len(user_input)):
            if user_input[i].upper() == 'Q':
                sel = False
                break
            try:
                tmp_sum = tmp_sum + float(user_input[i])
            except ValueError:
                print('Нужно вводить только числа!')
                continue
        result_sum = result_sum + tmp_sum
        print(f'Сумма введённых чисел равна: {result_sum}\n{"-" * 30}')


number_sum()
