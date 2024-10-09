class Figure:
    sides_count = 0

    def __init__(self, colour: tuple[int, int, int], *sides):
        self.__sides = tuple([1] * self.sides_count)        # сначала создаю заведомо валидные стороны
        self.set_sides(*sides)                           # потом вношу пользовательские стороны, если валидны
        if self.__is_valid_colour(*colour):
            self.__colour = colour
        self.filled = False

    def get_colour(self) -> tuple:
        return self.__colour

    def __is_valid_colour(self, r: int, g: int, b: int) -> bool:
        if r and g and b in range(0, 256):
            switch = True
        else:
            switch = False
        return switch

    def set_colour(self, r: int, g: int, b: int) -> None:
        check = self.__is_valid_colour(r, g, b)
        if check:
            self.__colour = [r, g, b]
            print("Изменение цвета принято")
        else:
            print("Неверный формат цвета")

    def __is_valid_sides(self, args) -> bool:
        switch = True
        if self.sides_count != len(args):  # проверка на соответствие количества сторон
            switch = False
        else:
            for side in args:
                if side <= 0 or not isinstance(side, int):      # проверка на целое положительное число:
                    switch = False
                    break
        return switch

    def get_sides(self) -> tuple:
        return self.__sides

    def __len__(self) -> float:
        perimeter = sum(self.__sides)
        return perimeter

    def set_sides(self, *new_sides) -> None:
        if new_sides:
            switch = self.__is_valid_sides(new_sides)
        else:
            switch = False
        if switch:
            self.__sides = tuple(new_sides)
            print(f"new sides: {self.get_sides()}")


class Circle(Figure):
    sides_count = 1

    def __init__(self, colour, side):
        super().__init__(colour, side)
        self.radius = self.get_sides()[0] / (2 * 3.14)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, colour, *sides):
        if self.__check_existing_triangle(*sides):
            super().__init__(colour, *sides)
        else:
            print("Такой треугольник не существует")

    def __check_existing_triangle(self, a, b, c) -> bool:        # проверка существует ли треугольник
        if a+b > c and a+c > b and b+c > a:
            return True
        else:
            return False

    def get_square(self) -> float:
        from math import sqrt
        p = self.__len__() / 2      # полупериметр
        a, b, c = self.get_sides()
        area = round(sqrt(p*(p-a)*(p-b)*(p-c)), 4)
        return area


class Cube(Figure):
    sides_count = 12

    def __init__(self, colour: tuple[int, int, int], *side):
        if len(side) != 1:
            sides = 1       # если значений сторон больше - куб будет создаваться по первому
        else:
            sides = side
        super().__init__(colour, *sides)

    def set_sides(self, new_side) -> None:
        sides = [new_side] * self.sides_count
        super().set_sides(*sides)


print('circle1')
circle1 = Circle((200, 200, 200), 10)
print(circle1.__len__())
print(circle1.get_colour())
print(circle1.get_sides())

print('\ntriangle1')
triangle1 = Triangle((128, 128, 128), 5, 4, 7)
print(triangle1.__len__())
print(triangle1.get_sides())
print(triangle1.get_colour())
print(triangle1.get_square())

print('\ncube1')
cube1 = Cube((1, 1, 1), 4)
print(cube1.__len__())
print(cube1.get_sides())
print(cube1.get_colour())

cube1.set_colour(55, 55, 66)
print(cube1.get_colour())

cube1.set_sides(45)
print(cube1.__len__())
print(cube1.get_sides())


# noinspection SpellCheckingInspection
"""
Общее ТЗ:
Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения размеров, цвета и т.д.
Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.

Подробное ТЗ:

Атрибуты класса Figure: sides_count = 0
Каждый объект класса Figure должен обладать следующими атрибутами:
Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
Атрибуты(публичные): filled(закрашенный, bool)
И методами:
Метод get_color, возвращает список RGB цветов.
Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
Метод get_sides должен возвращать значение я атрибута __sides.
Метод __len__ должен возвращать периметр фигуры.
Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.

Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).

Атрибуты класса Triangle: sides_count = 3
Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
Атрибуты класса Cube: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure.
Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
Метод get_volume, возвращает объём куба.

ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
"""