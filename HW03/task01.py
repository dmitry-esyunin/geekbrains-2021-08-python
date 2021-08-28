# Урок 3. Функции
#
# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
#

def dev_func(numerator, denominator):
    if denominator == 0:
        return None
    else:
        return float(numerator / denominator)


numerator = float(input('Укажите числитель: '))
denominator = float(input('Укажите знаменатель: '))
result = dev_func(numerator, denominator)

if result is None:
    print('Знаменатель дроби равен нулю. Результат неопределен')
else:
    print(f'Результат деления: {result}')
