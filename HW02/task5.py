# ДЗ № 2. Встроенные типы и операции с ними
#
# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]

while True:
    user_input = input('Введите новый элемент рейтинга, либо \'пустую строку\' для завершения\\> ')
    if user_input == '':
        break

    user_int = int(user_input)
    if user_int in my_list:
        my_list.insert(my_list.index(user_int), user_int)
    else:
        flag = False
        for index, el in enumerate(my_list):
            if user_int > el:
                flag = True
                break
        if flag:
            my_list.insert(index, user_int)
        else:
            my_list.append(user_int)

    print(my_list)

