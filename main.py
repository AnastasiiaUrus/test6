from figures import (Triangle, Rectangle, Trapezoid, Parallelogram, Circle,
                    Ball, TriangularPyramid, QuadrangularPyramid,
                    RectangularParallelepiped, Cone, TriangularPrism)

def create_shape(shape_type: str, params: list) -> 'Figure':
    """
    Create shape object based on type and parameters
    Створити об'єкт фігури на основі типу та параметрів
    """
    params = [float(p) for p in params]  # Convert strings to float
    
    if shape_type == "Triangle":
        return Triangle(*params)
    elif shape_type == "Rectangle":
        return Rectangle(*params)
    elif shape_type == "Trapeze":
        return Trapezoid(*params)
    elif shape_type == "Parallelogram":
        return Parallelogram(*params)
    elif shape_type == "Circle":
        return Circle(*params)
    elif shape_type == "Ball":
        return Ball(*params)
    elif shape_type == "TriangularPyramid":
        return TriangularPyramid(*params)
    elif shape_type == "QuadrangularPyramid":
        return QuadrangularPyramid(*params)
    elif shape_type == "RectangularParallelepiped":
        return RectangularParallelepiped(*params)
    elif shape_type == "Cone":
        return Cone(*params)
    elif shape_type == "TriangularPrism":
        return TriangularPrism(*params)
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")

def process_file(filename: str):
    """
    Process input file and find shape with maximum volume
    Обробити вхідний файл та знайти фігуру з найбільшим об'ємом
    """
    shapes = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if not parts:  # Skip empty lines
                    continue
                shape_type = parts[0]
                params = parts[1:]
                try:
                    shape = create_shape(shape_type, params)
                    shapes.append(shape)
                except (ValueError, TypeError) as e:
                    print(f"Error processing shape {shape_type}: {e}")
    except FileNotFoundError:
        print(f"File {filename} not found")
        return
    
    if not shapes:
        print("No valid shapes found in the file")
        return
    
    # Find shape with maximum volume (area for 2D, volume for 3D)
    max_volume_shape = max(shapes, key=lambda s: s.volume())
    
    print(f"\nResults for {filename}:")
    print(f"Shape with maximum volume/area:")
    print(f"Type: {type(max_volume_shape).__name__}")
    print(f"Dimension: {max_volume_shape.dimension()}D")
    
    if max_volume_shape.dimension() == 2:
        print(f"Area: {max_volume_shape.volume():.2f}")
        print(f"Perimeter: {max_volume_shape.perimeter():.2f}")
    else:
        print(f"Volume: {max_volume_shape.volume():.2f}")
        print(f"Surface area: {max_volume_shape.square_surface():.2f}")
        print(f"Base area: {max_volume_shape.square_base():.2f}")
        print(f"Height: {max_volume_shape.height():.2f}")

def main():
    """
    Main function to process all input files
    Головна функція для обробки всіх вхідних файлів
    """
    input_files = ["input01.txt", "input02.txt", "input03.txt"]
    for filename in input_files:
        process_file(filename)

if __name__ == "__main__":
    main() 