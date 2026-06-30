"""Задание 2: Полиморфизм (OCP)

У тебя есть функция, которая вычисляет площадь фигур. Сейчас она нарушает OCP. 
Перепиши код, используя классы и полиморфизм, чтобы добавление новой фигуры 
(например, треугольника) не требовало изменения функции calculate_total_area.

"""

# Плохой код
def calculate_total_area(shapes):
    total_area = 0
    for shape in shapes:
        if shape['type'] == 'circle':
            total_area += 3.14 * shape['radius'] ** 2
        elif shape['type'] == 'rectangle':
            total_area += shape['width'] * shape['height']
    return total_area

shapes = [
    {'type': 'circle', 'radius': 5},
    {'type': 'rectangle', 'width': 4, 'height': 6}
]
print(calculate_total_area(shapes))

### рефакторинг OCP

# shape base
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    "Абстрактный базовый класс для фигур"

    @abstractmethod
    def get_area(self) -> float:
        pass

# shapes
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self) -> float:
        shape_area = math.pi * self.radius ** 2
        return shape_area

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def get_area(self) -> float:
        shape_area = self.width * self.height
        return shape_area

# calc
def calculate_total_area(shapes: list[Shape]):
    total_area = 0
    
    for shape in shapes:
        total_area += shape.get_area()
    
    return total_area