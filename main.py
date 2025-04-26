from shapes import Sphere, Cylinder, Cube
import random

vals_for_shapes = [random.randint(1, 3) for _ in range(10)]
shapes = []

for val in vals_for_shapes:
    if val == 1:
        rad = random.randint(1, 10)
        shapes.append(("Sphere", Sphere(rad)))

    elif val == 2:
        rad = random.randint(1, 10) 
        hgth = random.randint(5, 20)  
        shapes.append(("Cylinder", Cylinder(rad, hgth)))

    else:
        side = random.randint(1, 10)
        shapes.append(("Cube", Cube(side)))

for shape in shapes:
    print(shape[0])
    print(round(shape[1].surface_area(), 2))
    print(round(shape[1].volume(), 2))
    print("-----------------------")