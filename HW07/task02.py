# Урок 7. ООП. Продвинутый уровень
#
#   2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
#   Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
#   К типам одежды в этом проекте относятся пальто и костюм.
#   У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
#   Это могут быть обычные числа: V и H, соответственно.
#   Для определения расхода ткани по каждому типу одежды использовать формулы: 
#       для пальто (V/6.5 + 0.5), 
#       для костюма (2 * H + 0.3). 
#   Проверить работу этих методов на реальных данных.
#   Реализовать общий подсчет расхода ткани. 
#   Проверить на практике полученные на этом уроке знания: 
#       реализовать абстрактные классы для основных классов проекта, 
#       проверить на практике работу декоратора @property.
#

class Fabric:

    __consumption_dict = {'Пальто': lambda v, h: v/6.5 + 0.5, 'Костюм': lambda v, h: 2 * h + 0.3}

    def __init__(self, type_):
        self.type = type_

    def consumption(self, v, h):
        return self.__consumption_dict[self.type](v, h)

    @property
    def classic(self):
        return Fabric.consumption(self, 35, 32)

    @property
    def kids(self):
        return Fabric.consumption(self, 10, 16)


print(Fabric('Пальто').consumption(35, 32))
print(Fabric('Костюм').classic)
print(Fabric('Костюм').consumption(35, 32))
print(Fabric('Костюм').kids)


