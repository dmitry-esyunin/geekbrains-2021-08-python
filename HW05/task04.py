# Урок 5. Работа с файлами
#
# 4.  Создать (не программно) текстовый файл со следующим содержимым:
#     One — 1
#     Two — 2
#     Three — 3
#     Four — 4
#  Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
#  При этом английские числительные должны заменяться на русские. 
#  Новый блок строк должен записываться в новый текстовый файл.
#


def f_read(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()


def translate(file_in, file_out, dict_):
    with open(file_in, 'r', encoding='utf-8') as f_in, open(file_out, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            for word in set(line.split()):
                word_l = word.lower()
                if word_l in dict_:
                    line = line.replace(word, dict_[word_l])
            f_out.writelines(line)


file = 'task04.txt'
file_translate = 'task04_translate.txt'

print('Исходный файл:\n' + f_read(file))
translate(file, file_translate,  {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'})
print('Переведенный файл:\n' + f_read(file_translate))

