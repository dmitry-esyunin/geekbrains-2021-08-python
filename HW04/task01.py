# Урок 4. Полезные инструменты
# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
#

from sys import argv
script_name, work_hours, rate_per_hour, premium = argv


def payroll_calc(work_hours, rate_per_hour, premium):
    return float(work_hours) * float(rate_per_hour) + float(premium)


print("%.02f" % payroll_calc(work_hours, rate_per_hour, premium))
