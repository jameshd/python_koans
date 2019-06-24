#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#


def triangle(a, b, c):
    sides = set([a, b, c])

    for side in sides:
        if side <= 0:
            raise TriangleError('All sides must be > 0')

    if a+b <= c or a+c <= b or b+c <= a:
        raise TriangleError('The sum of any two sides should be \
            greater than the third')
                    
    length = len(sides)

    if length == 3:
        return 'scalene'
    return 'equilateral' if length == 1 else 'isosceles'


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
