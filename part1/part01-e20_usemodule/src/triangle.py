# Enter you module contents here
	 
"""Exercise 1.20 (usermodule)
   The module contain two functions: hypotenuse & area. Contains two attributes: version & author.
   hypotenuse() which returns the length of the hypotenuse when given the lengths of two other sides of a right-angled triangle
   area() which returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters."""
 
# importing math for square
from math import sqrt
#math.sqrt(x)
#    Return the square root of x.
# https://docs.python.org/3/library/math.html
 
 
__version__ = "1.0"
__author__ = "Anton Rähmönen"
 
 
# c = (a² + b²)*1/2
def hypotenuse(a: float, b: float):
    """returns the length of the hypotenuse when given the lengths of two other sides of a right-angled triangle"""
    return sqrt(a**2 + b**2)
 
def area(a: float, b: float):
    """returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters."""
    return (a * b) / 2