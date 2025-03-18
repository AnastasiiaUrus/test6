from abc import ABC, abstractmethod
import math

class Figure(ABC):
    """
    Abstract base class for all geometric figures
    Абстрактний базовий клас для всіх геометричних фігур
    """
    @abstractmethod
    def dimension(self) -> int:
        """Return dimension of the figure (2 or 3)"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate perimeter of the figure"""
        pass

    @abstractmethod
    def square(self) -> float:
        """Calculate area of the figure"""
        pass

    @abstractmethod
    def square_surface(self) -> float:
        """Calculate surface area of 3D figure"""
        pass

    @abstractmethod
    def square_base(self) -> float:
        """Calculate base area of 3D figure"""
        pass

    @abstractmethod
    def height(self) -> float:
        """Return height of 3D figure"""
        pass

    @abstractmethod
    def volume(self) -> float:
        """Calculate volume for 3D figure or area for 2D figure"""
        pass

class Figure2D(Figure):
    """Base class for 2D figures / Базовий клас для двовимірних фігур"""
    
    def dimension(self) -> int:
        return 2

    def square_surface(self) -> None:
        return None

    def square_base(self) -> None:
        return None

    def height(self) -> None:
        return None

    def volume(self) -> float:
        return self.square()

class Figure3D(Figure):
    """Base class for 3D figures / Базовий клас для тривимірних фігур"""
    
    def dimension(self) -> int:
        return 3

    def perimeter(self) -> None:
        return None

    def square(self) -> None:
        return None

class Triangle(Figure2D):
    """Triangle class defined by three sides"""
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

    def square(self):
        # Using Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Rectangle(Figure2D):
    """Rectangle class defined by two sides"""
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def square(self):
        return self.length * self.width

class Trapezoid(Figure2D):
    """Trapezoid class defined by two bases and two sides"""
    def __init__(self, a: float, b: float, c: float, d: float):
        self.a = a  # base 1
        self.b = b  # base 2
        self.c = c  # side 1
        self.d = d  # side 2
        if not self._is_valid():
            raise ValueError("Invalid trapezoid sides")

    def _is_valid(self):
        if any(side <= 0 for side in [self.a, self.b, self.c, self.d]):
            return False
        if abs(self.c - self.d) >= abs(self.a - self.b):
            return False
        return True

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        h = self._height()
        return (self.a + self.b) * h / 2

    def _height(self):
        a, b = max(self.a, self.b), min(self.a, self.b)
        c, d = self.c, self.d
        p = (a - b) / 2
        h1 = math.sqrt(c * c - p * p)
        h2 = math.sqrt(d * d - p * p)
        return (h1 + h2) / 2

class Parallelogram(Figure2D):
    """Parallelogram class defined by two sides and height"""
    def __init__(self, base: float, side: float, height: float):
        self.base = base
        self.side = side
        self.height = height

    def perimeter(self):
        return 2 * (self.base + self.side)

    def square(self):
        return self.base * self.height

class Circle(Figure2D):
    """Circle class defined by radius"""
    def __init__(self, radius: float):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi * self.radius * self.radius

class Ball(Figure3D):
    """Ball (sphere) class defined by radius"""
    def __init__(self, radius: float):
        self.radius = radius

    def square_surface(self):
        return 4 * math.pi * self.radius * self.radius

    def square_base(self):
        return math.pi * self.radius * self.radius

    def height(self):
        return 2 * self.radius

    def volume(self):
        return 4/3 * math.pi * self.radius * self.radius * self.radius

class TriangularPyramid(Triangle, Figure3D):
    """Regular triangular pyramid with equilateral triangle base"""
    def __init__(self, side: float, height: float):
        super().__init__(side, side, side)
        self._height = height

    def square_surface(self):
        # Lateral surface area
        slant_height = math.sqrt(self._height * self._height + (self.a / math.sqrt(3)) ** 2)
        return 3 * self.a * slant_height / 2

    def square_base(self):
        return super().square()

    def height(self):
        return self._height

    def volume(self):
        return super().square() * self._height / 3

class QuadrangularPyramid(Rectangle, Figure3D):
    """Regular quadrangular pyramid with rectangle base"""
    def __init__(self, length: float, width: float, height: float):
        super().__init__(length, width)
        self._height = height

    def square_surface(self):
        # Lateral surface area
        l_slant = math.sqrt(self._height * self._height + (self.length/2) ** 2)
        w_slant = math.sqrt(self._height * self._height + (self.width/2) ** 2)
        return self.length * l_slant + self.width * w_slant

    def square_base(self):
        return super().square()

    def height(self):
        return self._height

    def volume(self):
        return super().square() * self._height / 3

class RectangularParallelepiped(Rectangle, Figure3D):
    """Rectangular parallelepiped defined by three edges"""
    def __init__(self, length: float, width: float, height: float):
        super().__init__(length, width)
        self._height = height

    def square_surface(self):
        return 2 * (self.length * self.width + 
                   self.length * self._height + 
                   self.width * self._height)

    def square_base(self):
        return super().square()

    def height(self):
        return self._height

    def volume(self):
        return super().square() * self._height

class Cone(Circle, Figure3D):
    """Regular cone defined by base radius and height"""
    def __init__(self, radius: float, height: float):
        super().__init__(radius)
        self._height = height

    def square_surface(self):
        # Lateral surface area
        slant = math.sqrt(self._height * self._height + self.radius * self.radius)
        return math.pi * self.radius * slant

    def square_base(self):
        return super().square()

    def height(self):
        return self._height

    def volume(self):
        return super().square() * self._height / 3

class TriangularPrism(Triangle, Figure3D):
    """Regular triangular prism"""
    def __init__(self, a: float, b: float, c: float, height: float):
        super().__init__(a, b, c)
        self._height = height

    def square_surface(self):
        return self.perimeter() * self._height

    def square_base(self):
        return super().square()

    def height(self):
        return self._height

    def volume(self):
        return super().square() * self._height 