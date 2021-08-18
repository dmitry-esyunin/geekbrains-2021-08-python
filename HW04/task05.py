# Урок 4. Полезные инструменты
#
# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
#

from functools import reduce


def multiply(param_1, param_2):
    return param_1 * param_2


num_min = 100
num_max = 1000
print(reduce(multiply, range(num_min, num_max + 1)))
