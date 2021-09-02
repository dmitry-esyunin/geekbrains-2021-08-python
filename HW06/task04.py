# Урок 6. Объектно-ориентированное программирование
#
# 4. Реализуйте базовый класс Car.
#  
#  - у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
#    А также методы: go, stop, turn(direction), которые должны сообщать, 
#    что машина поехала, остановилась, повернула (влево/вправо);
#  - опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#  - добавьте в базовый класс метод show_speed, который должен показывать текущую 
#    скорость автомобиля;
#  - для классов TownCar и WorkCar переопределите метод show_speed. 
#    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться 
#    сообщение о превышении скорости.
#  
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. 
# Вызовите методы и покажите результат.
# 

class Car:

    name = ''

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'{self.name} едет')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        if direction == 'left':
            print(f'{ self.name} повернул налево')
        elif direction == 'right':
            print(f'{self.name} повернул направо')
        else:
            print(f'{self.name} движется {direction}')

    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.speed} км/ч c привышением максимальной допустимой!!!!')


class WorkCar(Car):

    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.speed} км/ч c привышением максимальной допустимой!!!!')


civil = TownCar('седан обыкновенный', 'белый', 100)
truck = WorkCar('камаз кузовной', 'оранжевый', 100)
patrol = Car('патрульный', 'черный', 100, True)

civil.go()
civil.turn('right')
civil.turn('назад')
civil.show_speed()
patrol.show_speed()
