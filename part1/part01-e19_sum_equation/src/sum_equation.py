#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0:
        return "0 = 0"
    items = list(map(str, L))
    return " + ".join(items) + " = " f"{sum(L)}"

def main():
    print(sum_equation([1,5,7]))
    print(sum_equation([]))

if __name__ == "__main__":
    main()
