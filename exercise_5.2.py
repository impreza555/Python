some_file = open('exercise_5.2.txt', 'r', encoding='utf-8')
some_text = some_file.read()
some_file.close()
some_file = open('exercise_5.2.txt', 'r', encoding='utf-8')
lines = 0
words = 0

for line in some_file:
    lines += 1

    flag = 1
    for letter in line:
        if letter == '\n':
            continue
        elif letter != ' ' and flag == 1:
            words += 1
            flag = 0
        elif letter == ' ':
            flag = 1

print(f'{some_text}\n{"*" * 30}')
print(f'В данном тексте {lines} строк(a)')
print(f'И {words} слов')
some_file.close()
