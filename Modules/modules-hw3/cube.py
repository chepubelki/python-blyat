from square import Square


class Cube(Square):
    def __init__(self, side=None):
        # Начало вашего кода
        Square.__init__(self, side=side)
        self.side = side
        # Конец вашего кода

    def __str__(self):
        # Начало вашего кода
        return f'Cube with side {self.side} cm'
        # Конец вашего кода

    def get_surface_area(self):
        # Начало вашего кода
        return 6*(self.side**2)
        # Конец вашего кода

    def get_volume(self):
        # Начало вашего кода
        return self.side**3
        # Конец вашего кода

    @staticmethod
    def get_info():
        # Начало вашего кода
        return 'This class calculates surface area and volume of the cube'
        # Конец вашего кода
