import math
class Figure:
    sides_count = 0
    def __init__(self, color, *sides, filled = False):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Некорректный цвет. Цвет не изменен.")

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print("Некорректные стороны. Стороны не изменены.")

    def __is_valid_color(self, r, g, b): # Валидация цвета
        return all(isinstance(c, int) and 0 <= c <= 255 for c in [r, g, b])

    def __is_valid_sides(self, *new_sides): # Валидация сторон
        return (len(new_sides) == self.sides_count and
            all(isinstance(s, int) and s > 0 for s in new_sides))

    def __len__(self): # Метод для вычисления периметра (сумма всех сторон)
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference, filled=False):
        super().__init__(color, circumference, filled=filled)
        self.__radius = circumference / (2 * math.pi)

    def get_square(self): # Вычисление площади круга
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled=filled)

    def get_square(self): # Вычисление площади треугольника по формуле Герона
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length, filled=False):
        super().__init__(color, *([side_length] * 12), filled=filled)

    def get_volume(self): # Вычисление объёма куба
        side = self.get_sides()[0]  # Все стороны одинаковы
        return side ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
