#!/usr/bin/python3

import numpy as np

# The equations for the lines are y=a1x+b1 y=a_1x+b_1y = a1​x+b1​ and y= a2x+b2 y= a_2x + b_2y=a2​x+b2
# Computes the “exact” solution, x, of the well-determined, i.e., full rank, linear matrix equation ax = b.
def meeting_lines(a1, b1, a2, b2):
    # example from doc style
    # -a1x + y = b1
    # -a2x + y = b2
    a = np.array([[-a1, 1], [-a2, 1]])
    b = np.array([b1, b2])
    x = np.linalg.solve(a, b)
    return x

def main():
    a1=1
    b1=4
    a2=3
    b2=2

    x, y  = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")

if __name__ == "__main__":
    main()
