# Урок 5. Работа с файлами
#
# 3. Создать текстовый файл (не программно), 
# построчно записать фамилии сотрудников и величину их окладов. 
# Определить, кто из сотрудников имеет оклад менее 20 тыс., 
# вывести фамилии этих сотрудников. 
# Выполнить подсчет средней величины дохода сотрудников.
#

n = 20000
file = 'task03.txt'
separator = '\t'
employees = []

with open(file, encoding='utf-8') as f:
    for line in f:
        employee = line.split(separator)
        if len(employee) > 1:
            if int(employee[1]) < n:
                employees.append(employee[0])

print(employees)



