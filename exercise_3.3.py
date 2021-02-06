def sum_largest(arg_1, arg_2, arg_3):
    """
    Функция принимает три аргумента,
    и возвращает сумму наибольших двух аргументов.
    """
    tmp_list = [arg_1, arg_2, arg_3]
    tmp_1 = max(tmp_list)
    tmp_list.remove(tmp_1)
    tmp_2 = max(tmp_list)
    return tmp_1 + tmp_2


print(
    f'Сумма двух наибольших чисел равна: {sum_largest(arg_1=float(input("Введите первое число: ")), arg_2=float(input("Введите второе число: ")), arg_3=float(input("Введите третье число: ")))}')
