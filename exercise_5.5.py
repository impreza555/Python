some_file = open('exercise_5.5.txt', 'w', encoding='utf-8')
some_text = input('Введите несколько чисел через пробелы: ')
some_file.write(some_text)
some_file.close()
some_file = open('exercise_5.5.txt', 'r', encoding='utf-8')
content = some_file.read()
some_file.close()
content = content.split()
result_content = []
for i in content:
    if i.lstrip('-').replace('.', '', 1).isdigit(): result_content.append(i)
print(f'Сумма введённых чисел: {sum(map(float, result_content))}')
