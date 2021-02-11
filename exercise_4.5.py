import functools


def multipl(prev_el, el):
    return prev_el * el


some_list = [i for i in range(100, 1001, 2)]
print(
    f'Четные числа от 100 до 1000:\n{"-" * 28}\n{some_list}\nИх призведение:\n{"-" * 28}\n{functools.reduce(multipl, some_list)}')
