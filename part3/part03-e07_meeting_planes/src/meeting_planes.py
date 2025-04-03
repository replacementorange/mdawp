#!/usr/bin/python3

import numpy as np

def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    # if 3.6 was like this
    # -a1x + y = b1
    # -a2x + y = b2
    # Then 3.7
    # -b1x - a1y + z = c1
    # -b2x - a2y + z = c2
    # -b3x - a3y + z = c3
    y, x, z = np.linalg.solve([[a1, b1, -1], [a2, b2, -1], [a3, b3, -1]], [-c1, -c2, -c3])
    
    return x, y, z

def main():
    a1=1
    b1=4
    c1=5
    a2=3
    b2=2
    c2=1
    a3=2
    b3=4
    c3=1

    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"Planes meet at x={x}, y={y} and z={z}")

if __name__ == "__main__":
    main()
