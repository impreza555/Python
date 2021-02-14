try:
    with open('text_3.txt', 'r', encoding='utf-8') as my_f:
        empl_dict = {}
        for line in my_f:
            print(line, end='')
            line_list = line.split()
            empl_dict.setdefault(line_list[0], float(line_list[1]))
except IOError:
    print('Ошибка ввода-вывода!')
finally:
    my_f.close()
required_salary = 20000
losers = []
salaries = []
for name, salary in empl_dict.items():
    salaries.append(salary)
    if salary < required_salary:
        losers.append(name)
print(f'\n{"-" * 82}\nСотрудники: {(", ".join(name for name in list(losers)))} имеют оклад менее {required_salary}!')
print(f'{"-" * 82}\nСредняя величина дохода сотрудников {sum(salaries) / len(salaries)}')
