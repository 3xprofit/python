# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class triangle:
    def __init__(self, A, B, C):# функция конструктор, где АВС координаты вершин треугольника

        def lenSide(peak1, peak2): # Вычисление длины стороны по координатам (Х.У)
            return math.sqrt((peak1[0] - peak2[0]) ** 2 + (peak1[1] - peak2[1]) ** 2)
        self.A = A
        self.B = B
        self.C = C

        self.AB = lenSide(self.A, self.B)
        self.BC = lenSide(self.B, self.C)
        self.CA = lenSide(self.C, self.A)


    def perimeterTriangle(self): # Вычисление периметра треугольника
        return self.AB + self.BC + self.CA


    def areaTriangle(self): # Вычисление площади треугольника(формула Герона)
        halfPerimeter = self.perimeterTriangle() / 2
        return math.sqrt(halfPerimeter * (halfPerimeter - self.AB) * (halfPerimeter - self.BC) * (halfPerimeter - self.CA))



    def heightTriangle(self): # Вычисление высоты треугольника по формуле
        return 2 * self.areaTriangle() / self.CA

triangleExample = triangle((1, 1), (4, 10), (7, 3)) # задание координат треугольника


print("\nЗадача 1")

print('Площадь треугольника АВС равна {}'.format(triangleExample.areaTriangle()))
print('Высота треугольника АВС, проведенная из угла В равна {}'.format(triangleExample.heightTriangle()))
print('Периметр треугольника АВС равен {}'.format(triangleExample.perimeterTriangle()))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math

class trape:
    def __init__(self, A, B, C, D):# функция конструктор, где АВСD - координаты вершин трапеции

        def lenSide(peak1, peak2): # Вычисление длины стороны по координатам (Х.У)
            return math.sqrt((peak1[0] - peak2[0]) ** 2 + (peak1[1] - peak2[1]) ** 2)

        def areaTriangle(len1, len2, len3):
            halfPerimeter = (len1 + len2 + len3) / 2
            return math.sqrt(halfPerimeter * (halfPerimeter - len1) * (halfPerimeter - len2) * (halfPerimeter - len3))

        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.AB = lenSide(self.A, self.B)
        self.BC = lenSide(self.B, self.C)
        self.CD = lenSide(self.C, self.D)
        self.DA = lenSide(self.D, self.A)
        self.lenDiagonalAC = lenSide(self.A, self.C)
        self.lenDiagonalBD = lenSide(self.B, self.D)
        self.perimeter = self.AB + self.BC + self.CD + self.DA # Вычисление периметра трапеции
        self.area = areaTriangle(self.AB, self.lenDiagonalBD, self.DA) \
                    + areaTriangle(self.lenDiagonalBD, self.BC, self.CD) # рассчитываем площать трапеции:
        #... она равна как площадь двух треугольников площади которых и складываем


    def trapeIsosceles(self): # Проверка равнобочности трапеции
        if self.lenDiagonalAC == self.lenDiagonalBD:
            return True
        return False

trapeExample = trape((1, 1), (4, 10), (6, 10), (9, 1))

print("\nЗадача 2")

print('Длинна строны АВ = {}, ВС = {}, СD = {}, DA = {}'.format(trapeExample.AB, trapeExample.BC, trapeExample.CD, trapeExample.DA))
print('Периметр трапеции ABCD = {}'.format(trapeExample.perimeter))
print('Трапеция ABCD равнобочная = {}'.format(trapeExample.trapeIsosceles()))
print('Площадь трапеции  = {}'.format(trapeExample.area))
