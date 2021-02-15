from googletrans import Translator

# Всю голову изломал с этим заданием. Всё время выходила ошибка,
# причём не в моём коде, а где-то в модуле googletrans.
# Погугил, и нашёл решение: надо усанавливать альфа-версию googletrans
# pip install googletrans==4.0.0-rc1

translator = Translator()

my_f = open('text_4.txt', 'r', encoding='utf-8')
contents = my_f.read()
result = translator.translate(contents, dest='ru')
with open('text_translate_4.txt', 'w', encoding='utf-8') as my_f:
    my_f.write(result.text)
