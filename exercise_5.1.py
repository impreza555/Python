some_file = open('exercise_5.1.txt', 'w', encoding="utf-8")
some_text = input('Введите какой-нибудь текст: ')
while some_text:
    some_file.write(some_text + '\n')
    some_text = input('Введите какой-нибудь текст: ')
    if not some_text:
        break
some_file.close()
