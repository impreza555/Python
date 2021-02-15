disciplines_dict = {}
try:
    with open('text_6.txt', 'r', encoding='utf-8') as my_f:
        for line in my_f:
            data = line.replace('(', ' ').replace(':', '').replace(')', ' ').replace('-', '').split()
            disciplines_dict.setdefault(data[0], sum(int(i) for i in data if i.isdigit()))
        print(disciplines_dict)
except IOError:
    print('Ошибка ввода-вывода!')
finally:
    my_f.close()
