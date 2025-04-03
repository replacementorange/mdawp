#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    # discriminant
    d = (b**2) - (4*a*c)
    
    solution1 = (-b + math.sqrt(d)) / (2 * a)
    solution2 = (-b - math.sqrt(d)) / (2 * a)
 
    return (solution1, solution2)


def main():
	print(solve_quadratic(1,-3,2))  #(2.0,1.0)
	print(solve_quadratic(1,2,1))   #(-1.0,-1.0)

if __name__ == "__main__":
    main()
