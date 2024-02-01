import math


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None
    @staticmethod
    def proverka_vel(a):
        if not (isinstance(a,int) or isinstance(a,float)):
            raise TypeError("Не верный тип данных")
        if a<0:
            raise ValueError("Отрицательное значение")
        return a
class Rectangle(Figure):
    """ Производный класс. Прямоугольник. """

    def __init__(self,a,b): # TODO определить конструктор и перегрузить метод area
        self.a=super().proverka_vel(a)
        self.b=super().proverka_vel(b)
    def area(self):
        super().area()
        print(f'Площать прямоугольника равна {self.a*self.b}')
class Circle(Figure):
    """ Производный класс. Круг. """

    # TODO определить конструктор и перегрузить метод area
    def __init__(self,a): # TODO определить конструктор и перегрузить метод area
        self.a=super().proverka_vel(a)
    def area(self):
        super().area()
        print(f'Площать круга равна {math.pi*self.a**2:.2f}')

if __name__ == "__main__":
    fig = Figure()
    fig.area()

    rect = Rectangle(5, 10)
    rect.area()

    circle = Circle(5)
    circle.area()
