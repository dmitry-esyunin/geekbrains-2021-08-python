# Урок 3. Функции
#
# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
#

def int_func(string):
    return '' if string == '' else string[0].upper() + string[1:]


def my_title_func(string, separator=' '):
    result = ''
    for word in string.split(separator):
        result += int_func(word) + separator
    return result[:-len(separator)]


text = 'text text     t xt text'
format_ = '%+50s:\t%s'

print(format_ % ("исходный текст", text))
print(format_ % ("применение int_func", int_func(text)))
print(format_ % ("применение int_func ко всем словам в строке", my_title_func(text)))
print(format_ % ("стандартный метод title", text.title()))
