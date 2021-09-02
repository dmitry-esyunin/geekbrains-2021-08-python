#  Урок 8. ООП. Полезные дополнения
#  
#  7. Реализовать проект «Операции с комплексными числами». 
#  Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения
#  комплексных чисел. 
#  Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив 
#  сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
#

class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __add__(self, other):
        return Complex(self.real + other.real, self.image + other.image)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.image - other.image)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.image * other.image,
                       self.image * other.real + self.real * other.image)

    def __truediv__(self, other):
        k = other.real ** 2 + other.image ** 2
        return Complex((self.real * other.real + self.image * other.image) / k,
                       (self.image * other.real - self.real * other.image) / k)

    def __str__(self):

        real_part = str(self.real) if self.real != 0 else ''
        image_part = '' if self.image == 0 else 'i' if abs(self.image) == 1 else str(abs(self.image)) + 'i'

        if real_part == '':
            middle_part = '' if self.image >= 0 else '-'
        else:
            middle_part = '' if image_part == '' else ' + ' if self.image > 0 else ' - '

        result = real_part + middle_part + image_part
        if result == '':
            return '0'
        else:
            return result


z1 = Complex(7, 2)
z2 = Complex(2, -1)

print(f'Z1 = {z1}\nZ2 = {z2}\nОперации:')
print(f'\tСумма    :\t{z1 + z2}')
print(f'\tРазность :\t{z1 - z2}')
print(f'\tУмножение:\t{z1 * z2}')
print(f'\tДеление  :\t{z1 / z2}')




