class Rectangle:
    def __init__(self, width=None, height=None):
        # Начало вашего кода
        self.width = width
        self.height = height
        # Конец вашего кода

    def __str__(self):
        # Начало вашего кода
        return f'Rectangle with width {self.width} cm and height {self.height} cm'
        # Конец вашего кода

    def get_area(self):
        # Начало вашего кода
        return self.width * self.height
        # Конец вашего кода

    def get_perimeter(self):
        # Начало вашего кода
        return 2 * (self.width + self.height)
        # Конец вашего кода

    @staticmethod
    def get_info():
        # Начало вашего кода
        return 'This class calculates perimeter and area of the rectangles'
        # Конец вашего кода
