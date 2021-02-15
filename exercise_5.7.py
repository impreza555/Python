from json import dumps

list_of_firms = []
profit = {}
total_profit = 0
i = 0
try:
    with open('text_7.txt', 'r', encoding='utf-8') as my_f:
        firm_content = my_f.read()
        my_f.seek(0)
        print(f'Фирмы и их выручка / издержки:\n{"-" * 30}\n{firm_content}')
        for line in my_f:
            name, type_of_ownership, earnings, expenses = line.split()
            profit[name] = float(earnings) - float(expenses)
            if profit.setdefault(name) >= 0:
                total_profit = total_profit + profit.setdefault(name)
                i += 1
        if i != 0:
            average_profit = round((total_profit / i), 2)
        else:
            print(f'Все фирмы работают в убыток')
        average_profit = {'средняя прибыль': average_profit}
        list_of_firms.extend([profit, average_profit])
        print(f'{"-" * 30}\nПрибыль каждой компании - {list_of_firms}')
    with open('text_7.json', 'w', encoding='utf-8') as my_file_js:
        my_file_js.write(dumps(list_of_firms, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': ')))
        print(f'{"-" * 30}\nБыл создан результирующий файл "text_7.json"')
except IOError:
    print('Ошибка ввода-вывода!')
finally:
    my_f.close()
