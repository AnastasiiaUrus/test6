from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Abstract base class for geometric shapes
    Абстрактний базовий клас для геометричних фігур
    """
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of the shape / Розрахувати периметр фігури"""
        pass

    @abstractmethod
    def area(self):
        """Calculate area of the shape / Розрахувати площу фігури"""
        pass

class Triangle(Shape):
    """
    Triangle class defined by three sides
    Клас трикутника, що визначається трьома сторонами
    """
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        if not self._is_valid():
            raise ValueError("Invalid triangle sides")

    def _is_valid(self):
        """Check if triangle is valid using triangle inequality theorem"""
        return (self.a + self.b > self.c and 
                self.b + self.c > self.a and 
                self.a + self.c > self.b)

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Using Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Rectangle(Shape):
    """
    Rectangle class defined by two sides
    Клас прямокутника, що визначається двома сторонами
    """
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

class Trapezoid(Shape):
    """
    Trapezoid class defined by two bases and two sides
    Клас трапеції, що визначається двома основами та двома бічними сторонами
    """
    def __init__(self, a: float, b: float, c: float, d: float):
        """
        Initialize trapezoid with:
        a, b - parallel sides (bases)
        c, d - lateral sides
        """
        self.a = a  # base 1
        self.b = b  # base 2
        self.c = c  # side 1
        self.d = d  # side 2
        if not self._is_valid():
            raise ValueError("Invalid trapezoid sides")

    def _is_valid(self):
        """Check if trapezoid is valid"""
        # Check if sides are positive
        if any(side <= 0 for side in [self.a, self.b, self.c, self.d]):
            return False
        # Check if sum of parallel sides is greater than difference of lateral sides
        if abs(self.c - self.d) >= abs(self.a - self.b):
            return False
        return True

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        # Using formula: A = h(a + b)/2 where h is height
        h = self._height()
        return (self.a + self.b) * h / 2

    def _height(self):
        """Calculate height using lateral sides and bases"""
        a, b = max(self.a, self.b), min(self.a, self.b)  # a is longer base
        c, d = self.c, self.d
        
        # Using formula based on lateral sides and bases
        p = (a - b) / 2  # half difference of parallel sides
        # Height using Pythagorean theorem
        h1 = math.sqrt(c * c - p * p)  # height from first lateral side
        h2 = math.sqrt(d * d - p * p)  # height from second lateral side
        return (h1 + h2) / 2  # average height for more stability

class Parallelogram(Shape):
    """
    Parallelogram class defined by two sides and height
    Клас паралелограма, що визначається двома сторонами та висотою
    """
    def __init__(self, base: float, side: float, height: float):
        self.base = base
        self.side = side
        self.height = height

    def perimeter(self):
        return 2 * (self.base + self.side)

    def area(self):
        return self.base * self.height

class Circle(Shape):
    """
    Circle class defined by radius
    Клас круга, що визначається радіусом
    """
    def __init__(self, radius: float):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius * self.radius 