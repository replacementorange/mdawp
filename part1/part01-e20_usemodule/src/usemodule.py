#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from here
    print(triangle.hypotenuse(12,4))
    print(triangle.area(12.4))

if __name__ == "__main__":
    main()
