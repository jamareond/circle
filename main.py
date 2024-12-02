# -*- coding: utf-8 -*-
"""Jamareon Davis
    3096697
    12/02/2024
    Lab 09
"""

from circle import Circle

def create_user_circle():
    print("Enter the following values for the circle:")
    radius = float(input("Enter radius: "))
    x_pos = float(input("Enter x position: "))
    y_pos = float(input("Enter y position: "))
    return Circle(radius, x_pos, y_pos)

def print_circle_info(circ, name="Circle"):
    print(f"Information for {name}:")
    print(f"  location: ({circ.x_pos}, {circ.y_pos})")
    print(f"  diameter: {circ.diameter()}")
    print(f"  area: {circ.area()}")
    print(f"  circumference: {circ.circumference()}")
    print(f"  distance from the origin: {circ.dist_to_origin()}")

def main():
    print("Create Circle 1:")
    circle1 = create_user_circle()

    print("\nCreate Circle 2:")
    circle2 = create_user_circle()

    print("\nCircle 1 Information:")
    print_circle_info(circle1, "Circle 1")

    if circle1.is_overlap(circle2):
        print("Circle 1 overlaps Circle 2.")
    else:
        print("Circle 1 does not overlap Circle 2.")

if __name__ == "__main__":
    main()
