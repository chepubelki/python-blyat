from math import pi


class Rectangle:
    def __init__(self, width=None, height=None):
        # Начало вашего кода
        self.width = width
        self.height = height
        # Конец вашего кода

    def __str__(self):
        # Начало вашего кода
        return 'Rectangle'
        # Конец вашего кода

    def calc_area(self):
        # Начало вашего кода
        return self.width * self.height
        # Конец вашего кода

    def calc_perimeter(self):
        # Начало вашего кода
        return 2 * (self.width + self.height)
        # Конец вашего кода


class Square:
    def __init__(self, side=None):
        # Начало вашего кода
        self.side = side
        # Конец вашего кода

    def __str__(self):
        # Начало вашего кода
        return 'Square'
        # Конец вашего кода

    def calc_area(self):
        # Начало вашего кода
        return self.side * self.side
        # Конец вашего кода

    def calc_perimeter(self):
        # Начало вашего кода
        return 4 * self.side
        # Конец вашего кода


class Circle:
    def __init__(self, radius=None):
        # Начало вашего кода
        self.radius = radius
        # Конец вашего кода

    def __str__(self):
        # Начало вашего кода
        return 'Circle'
        # Конец вашего кода

    def calc_area(self):
        # Начало вашего кода
        return pi*(self.radius**2)
        # Конец вашего кода

    def calc_perimeter(self):
        # Начало вашего кода
        return 2*(pi*self.radius)
        # Конец вашего кода
