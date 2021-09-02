#  Урок 8. ООП. Полезные дополнения
#
#  1. Реализовать класс «Дата», функция-конструктор которого должна принимать
#  дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. 
#  Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать 
#  их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
#  месяца и года (например, месяц — от 1 до 12). 
#  Проверить работу полученной структуры на реальных данных.
#  

import re


class Date:

    @classmethod
    def split_to_int(cls, dd_mm_yyyy):
        return [int(x) for x in re.findall('\d+', dd_mm_yyyy)]

    @staticmethod
    def check(date_list):
        chk_month = True if (0 < date_list[1] <= 12 and date_list[1] == date_list[1] // 1) else False
        chk_year = True if (1900 < date_list[2] < 2199 and date_list[2] == date_list[2] // 1) else False
        return [chk_month, chk_year]


print(Date.split_to_int('11-12-2021'))
print(Date.check(Date.split_to_int('11-12-2021')))
