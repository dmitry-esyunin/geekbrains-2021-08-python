# Урок 5. Работа с файлами
# 1. Создать программно файл в текстовом формате, 
# записать в него построчно данные, вводимые пользователем. 
# Об окончании ввода данных свидетельствует пустая строка.
#

output_file = 'task01.txt'

result = ''
while True:
    user_input = input('Введите данные построчно, либо \'пустую строку\' для завершения\\> ')
    if user_input == '':
        break
    else:
        result += user_input + "\n"


if result != "":
    with open(output_file, "w") as f:
        f.write(result)



