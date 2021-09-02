#  Урок 8. ООП. Полезные дополнения
#  
#  4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
#  А также класс «Оргтехника», который будет базовым для классов-наследников. 
#  Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
#  В базовом классе определить параметры, общие для приведенных типов. 
#  В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#  

# не помню и не нашел, как называется декоратор, который позволяет собирать параметры класса по вх.параметрам
class Storage:
    def __init__(self, bar_code, vendor, part_number):
        self.bar_code = bar_code
        self.vendor = vendor
        self.part_number = part_number


class Office_equipment(Storage):
    def __init__(self, is_electric, is_printing):
        self.is_electric = is_electric
        self.is_printing = is_printing


class Printer(Office_equipment):
    def __init__(self, type_of_print, color, max_paper_size, interfaces):
        self.type_of_print = type_of_print
        self.color = color
        self.max_paper_size = max_paper_size
        self.interfaces = interfaces


class Scanner(Office_equipment):
    def __init__(self, dpi, color, interfaces):
        self.dpi = dpi
        self.color = color
        self.interfaces = interfaces


class MFP(Printer, Scanner):
    pass

#
# HP = MFP('Laser', 'CMYK', 'A4', ['USB', 'WIFI'])
# HP.vendor = 'HP'
# HP.bar_code = 'AE12000-Y21'


