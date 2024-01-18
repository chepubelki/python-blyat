import csv
from classes import Square
from classes import Rectangle
from classes import Circle


def read_file(filename=None):
    list_of_figures = []
    with open(filename) as file:
        # Начало вашего кода
        csv_reader = csv.reader(file)
        for row in csv_reader:
            fogure = row[0].title()
            if fogure == 'Circle':
                list_of_figures.append(Circle(float(row[1])))
            elif fogure == 'Rectangle':
                if float(row[1]) == float(row[2]):
                    list_of_figures.append(Square(float(row[1])))
                else:
                    list_of_figures.append(
                        Rectangle(float(row[1]), float(row[2])))
            elif fogure == 'Square':
                list_of_figures.append(Square(float(row[1])))
            else:
                print(f'{row[0].title()} is unknown figure')
    # Конец вашего кода
    return list_of_figures


def get_perimeters(list_of_figures):
    for i in list_of_figures:
        res = '{0:.2f}'.format(i.calc_perimeter())
        print(f'{i} has following perimeter: {res}')


def get_areas(list_of_figures):
    for i in list_of_figures:
        res = '{0:.2f}'.format(i.calc_area())
        print(f'{i} has following perimeter: {res}')
