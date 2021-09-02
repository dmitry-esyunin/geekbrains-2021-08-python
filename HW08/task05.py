#  Урок 8. ООП. Полезные дополнения
#  
#  5. Продолжить работу над первым заданием.
#  Разработать методы, отвечающие за приём оргтехники на склад и передачу в
#  определенное подразделение компании. Для хранения данных о наименовании и 
#  количестве единиц оргтехники, а также других данных, можно использовать любую 
#  подходящую структуру, например словарь.
#  

from task04 import Storage, Printer, Scanner, MFP


class StorageAction(Storage):
    def __init__(self, placement):
        self.placement = placement

    def registration(self):
        pass

    def deregistration(self):
        pass

    def move(self, new_placement):
        pass


class StorageStaff(StorageAction, Printer, Scanner, MFP):

    def staff_in(self, placement):
        return [item for item in self if self.placement == placement]

    def count_in(self, placement):
        return len(self.staff_in(placement))

