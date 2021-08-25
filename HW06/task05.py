# Урок 6. Объектно-ориентированное программирование
#
# 5. Реализовать класс Stationery (канцелярская принадлежность).
#  
#  - определить в нём атрибут title (название) и метод draw (отрисовка). 
#    Метод выводит сообщение «Запуск отрисовки»;
#  - создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#  - в каждом классе реализовать переопределение метода draw. 
#    Для каждого класса метод должен выводить уникальное сообщение;
#  - создать экземпляры классов и проверить, 
#    что выведет описанный метод для каждого экземпляра.
#

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашем')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


pen = Pen('ручка')
pencil = Pencil('карандаш')
marker = Handle('маркер')

print(f'У нас есть: {pen.title}, {pencil.title}, {marker.title}')
pen.draw()
pencil.draw()
marker.draw()

