# Урок 5. Работа с файлами
#
# 2. Создать текстовый файл (не программно), 
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
#

file = "task02.txt"
analyze = {}
with open(file, "r") as f:
    for i, line in enumerate(f):
        analyze[i + 1] = len(line.split())


print(analyze)
