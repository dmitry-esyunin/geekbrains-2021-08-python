# Урок 5. Работа с файлами
#
# 5. Создать (программно) текстовый файл, 
# записать в него программно набор чисел, разделенных пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
#


# Евгений, вопрос! Как импортировать функцию из другого py скрипта, не выполняя его?
# команда "from task04 import f_read" импортирует функцию, но зачем-то еще и выполняет скрипт (task04)


def f_read(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()


def generator(file, num, start=1000):
    with open(file, "w") as f:
        f.write(" ".join(str(start + a) for a in range(num)))


def summator(file):
    with open(file, "r") as f:
        result = 0
        for word in f.read().split():
            try:
                result += int(word)
            except:
                pass
    return result


file = 'task05.txt'
generator(file, 10)
print(f_read('task05.txt'))
print('Сумма всех чисел в файле: ' + str(summator('task05.txt')))


