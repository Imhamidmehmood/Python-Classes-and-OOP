# Q7. Shape Calculator - Abstraction

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(6, 4)

    print(f"Circle (radius 5): area={circle.area():.2f}, perimeter={circle.perimeter():.2f}")
    print(f"Rectangle (6 x 4): area={rectangle.area():.2f}, perimeter={rectangle.perimeter():.2f}")

    try:
        shape = Shape()
    except TypeError as error:
        print(f"Cannot instantiate Shape: {error}")

    # Shape is abstract, so Python prevents creating an object until
    # all abstract methods are implemented by a child class.
