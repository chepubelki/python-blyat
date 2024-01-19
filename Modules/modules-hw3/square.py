from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side=None):
        # Начало вашего кода
        Rectangle.__init__(self, width=side, height=side)
        self.side = side
        # Конец вашего кода

    def __str__(self):
        # Начало вашего кода
        return f'Square with side {self.side} cm'
        # Конец вашего кода

    @staticmethod
    def get_info():
        # Начало вашего кода
        return 'This class calculates perimeter and area of the square'
        # Конец вашего кода
