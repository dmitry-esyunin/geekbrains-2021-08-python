# Урок 6. Объектно-ориентированное программирование
# 
# 3. Реализовать базовый класс Worker (работник).
#  
#  - определить атрибуты: name, surname, position (должность), income (доход);
#  - последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: 
#    оклад и премия, например, {"wage": wage, "bonus": bonus};
#  - создать класс Position (должность) на базе класса Worker;
#  - в классе Position реализовать методы получения полного имени сотрудника 
#    (get_full_name) и дохода с учётом премии (get_total_income);
#  - проверить работу примера на реальных данных: создать экземпляры класса Position,
#    передать данные, проверить значения атрибутов, вызвать методы экземпляров.
# 

class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0, "bonus": 0}


class Position(Worker):

    def get_full_name(self):
        return self.name

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


John = Position()
John.name = 'John Smit'
John._income = {"wage": 1000, "bonus": 200}
John.position = 'expert IT'

print(f'Полное имя работника: {John.get_full_name()}, его зарплата: {John.get_total_income()}')
