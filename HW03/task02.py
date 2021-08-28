# Урок 3. Функции
#
# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
#
# Реализовать вывод данных о пользователе одной строкой.
#

def user_input(fields, defaults, prompt='Укажите значение для поля %field% (По умолчанию = %default%): '):
    result = {}
    for i, el in enumerate(fields):
        _input = input(prompt.replace('%field%', el).replace('%default%', defaults[i]))
        if _input == '':
            result[el] = defaults[i]
        else:
            result[el] = _input
    return result


def print_user_data(**kwargs):
    result = 'Получены следующие данные пользователя --> '
    for field, value in kwargs['user_data'].items():
        result += field + ' = \"' + value + '\"; '
    print(result)


data_fields = ('firstname', 'surname', 'birth_year', 'city', 'email', 'phone')
data_defaults = ('Иван', 'Иванов', '2000', 'Москва', 'ivanov2000@mail.ru', '+7(999)123-4567')
print_user_data(user_data=user_input(data_fields, data_defaults))

