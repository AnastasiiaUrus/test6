# Geometric Figures Calculator

This project implements a hierarchy of geometric shapes with calculation of their properties.

## Project Structure

- `figures.py` - Contains all shape classes implementation
- `main.py` - Program to process input files and find shapes with maximum volume
- `diagram.md` - Class hierarchy diagram in Mermaid format
- Input files:
  - `input01.txt`
  - `input02.txt`
  - `input03.txt`

## Class Hierarchy

The project implements the following class hierarchy (see `diagram.md` for visual representation):

1. Base abstract class `Figure`
2. Abstract classes `Figure2D` and `Figure3D`
3. 2D shapes:
   - Triangle
   - Rectangle
   - Trapezoid
   - Parallelogram
   - Circle
4. 3D shapes:
   - Ball (Sphere)
   - TriangularPyramid
   - QuadrangularPyramid
   - RectangularParallelepiped
   - Cone
   - TriangularPrism

## How to Run

1. Make sure you have Python 3.6+ installed
2. Place input files in the same directory as Python files
3. Run the program:
   ```bash
   python3 main.py
   ```

## Input File Format

Each line in input files should contain:
1. Shape name (one of: Triangle, Rectangle, Trapeze, Parallelogram, Circle, Ball, TriangularPyramid, QuadrangularPyramid, RectangularParallelepiped, Cone, TriangularPrism)
2. Parameters for the shape (space-separated)

Example:
```
Triangle 3 4 5
Rectangle 5 4
Circle 3
```

## Output

For each input file, the program will output:
- Shape with maximum volume (for 3D) or area (for 2D)
- Shape type and dimension
- All relevant measurements (area/volume, perimeter/surface area, etc.) 