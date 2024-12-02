# -*- coding: utf-8 -*-
"""Jamareon Davis
    3096697
    12/02/2024
    Lab 09
"""

from math import pi, sqrt

class Circle:
    def __init__(self, radius, x_pos, y_pos):
        self.radius = radius
        self.x_pos = x_pos
        self.y_pos = y_pos

    def diameter(self):
        return 2 * self.radius

    def area(self):
        return pi * self.radius ** 2

    def circumference(self):
        return 2 * pi * self.radius

    def dist_to_origin(self):
        return sqrt(self.x_pos ** 2 + self.y_pos ** 2)

    def dist_to_center(self, other):
        return sqrt((self.x_pos - other.x_pos) ** 2 + (self.y_pos - other.y_pos) ** 2)

    def is_inside(self, other_circle):
        distance = self.dist_to_center(other_circle)
        return distance + self.radius <= other_circle.radius

    def is_overlap(self, other_circle):
        distance = self.dist_to_center(other_circle)
        return distance < self.radius + other_circle.radius
