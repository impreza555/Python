def caps_word(word):
    """
    Функция принимает слово из маленьких букв и возвращает его же,
    но с прописной первой буквой.

    """
    return word.capitalize()


def caps_sentence(sentence):
    """
    Функция принимает строку слов из маленьких букв, разделенных пробелом и возвращает
    исходную строку, но каждое слово начинается с заглавной буквы.
    используется функция caps_word(word).

    """
    sentence_list = []
    for i in range(len(sentence)):
        # Вызывается функцмя caps_word(word)
        sentence_list.append(caps_word(sentence[i]))
    return print((' ').join(sentence_list))


print(caps_word(input('Ведите слово: ')))
caps_sentence(input('Введите несколько слов через пробелы, например предложение: ').split())
