from math import factorial


def fact(n):
    for j in range(1, n + 1):
        yield factorial(j)


n = int(input('Введите число "n": '))
print(f'Факториалы чисел от 1 до {n}:\n{"-" * 28}')
for n in fact(n):
    print(n, end=' ')
