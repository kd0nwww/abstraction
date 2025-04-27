# Abstraction in Python

## Overview
This repository contains implementation of 3D shapes using object-oriented programming principles, particularly abstraction, inheritance and polymorphism.

## Shape3D (Abstract Base Class)
The `Shape3D` class is an abstract base class that defines the interface for all 3D shapes.

### Methods
- `surface_area()`: Abstract method that returns the surface area of the shape.
- `volume()`: Abstract method that returns the volume of the shape.

## Subclasses

### Sphere
Represents a sphere shape in 3D space.3

#### Methods

- `surface_area()`: Calculate and return the surface area of the sphere.
- `volume()`: Calculate and return the volume of the sphere.

### Cylinder
Represents a cylinder shape in 3D space.

#### Methods

- `surface_area()`: Calculate and return the surface area of the cylinder.
- `volume()`: Calculate and return the volume of the cylinder.

### Cube
Represents a cube shape in 3D space.

#### Methods

- `surface_area()`: Calculate and return the surface area of the cube.
- `volume()`: Calculate and return the volume of the cube.

## `main.py`
The `main.py` file demonstrates the implementation of the 3D shapes. It creates 10 random instances of the three shape classes (Sphere, Cylinder, and Cube) with randomly generated dimensions. The program then calculates and displays the volume and surface area for each shape, showcasing polymorphism in action as each shape implements the abstract methods differently.


## Usage
```python
from shapes import Sphere
# Example usage
sphere = Sphere(5)
print(f"Surface Area: {sphere.surface_area()}") # Output: 314.16
print(f"Volume: {sphere.volume()}") # Output: 523.6
```