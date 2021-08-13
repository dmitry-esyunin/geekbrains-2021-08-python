# Урок 3. Функции
#
# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
#

def my_func(a, b, c):
    return a + b if (c <= a and c <= b) else b + c if (a <= c and a <= b) else a + c


print(my_func(1, 1, 0))
print(my_func(1, 0, 1))
print(my_func(0, 1, 1))
