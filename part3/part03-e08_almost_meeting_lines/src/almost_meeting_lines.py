#!/usr/bin/python3

import numpy as np

def almost_meeting_lines(a1, b1, a2, b2):
    # 3.6 copy
    a = np.array([[-a1, 1], [-a2, 1]])
    b = np.array([b1, b2])
    #x = np.linalg.solve(a, b)
    #return x
    # numpy.linalg.lstsq Return the least-squares solution to a linear matrix equation.
    try:
        return (np.linalg.solve(a, b), True) # 3.6
    except:
        return (np.linalg.lstsq(a, b)[0], False)

def main():
    a1=1
    b1=2
    a2=-1
    b2=0

    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")

    a1=a2=1
    b1=2
    b2=-2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b1)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    a2=1
    b2=1
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

if __name__ == "__main__":
    main()
