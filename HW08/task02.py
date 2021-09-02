#  Урок 8. ООП. Полезные дополнения
#
#  2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
#  Проверьте его работу на данных, вводимых пользователем. 
#  При вводе пользователем нуля в качестве делителя программа должна корректно 
#  обработать эту ситуацию и не завершиться с ошибкой.
#  

class ZeroDenominator(Exception):
    pass


def divide_integer(numerator, denominator, default_output=0):
    result = default_output
    try:
        if int(denominator) == 0:
            raise ZeroDenominator
        result = int(numerator) // int(denominator)
    except ZeroDenominator:
        print(f'Error: знаменатель равен нулю!')
    except ZeroDivisionError:
        print(f'Error: деление на ноль!')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        return result


while True:
    user_input = input('Укажите число или \'пустую строку\' для выхода:')
    if user_input == '':
        break
    print(divide_integer(1000, user_input))


