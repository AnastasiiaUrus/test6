from shapes import Triangle, Rectangle, Trapezoid, Parallelogram, Circle

def create_shape(shape_type: str, params: list) -> 'Shape':
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
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")

def process_file(filename: str):
    """
    Process input file and find shapes with maximum area and perimeter
    Обробити вхідний файл та знайти фігури з максимальною площею та периметром
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
    
    # Find shape with maximum area
    max_area_shape = max(shapes, key=lambda s: s.area())
    # Find shape with maximum perimeter
    max_perimeter_shape = max(shapes, key=lambda s: s.perimeter())
    
    print(f"\nResults for {filename}:")
    print("Shape with maximum area:")
    print(f"Type: {type(max_area_shape).__name__}")
    print(f"Area: {max_area_shape.area():.2f}")
    
    print("\nShape with maximum perimeter:")
    print(f"Type: {type(max_perimeter_shape).__name__}")
    print(f"Perimeter: {max_perimeter_shape.perimeter():.2f}")

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