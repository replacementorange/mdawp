#!/usr/bin/env python3

class Rational(object):
    def __init__(self, first: int, second: int) -> None:
	        self.first = first
	        self.second = second
	    
    def __mul__(self, other: "Rational") -> "Rational":
        return Rational(
            self.first * other.first, self.second * other.second
        )

    def __truediv__(self, other: "Rational") -> "Rational":
        return self * Rational(other.second, other.first)

    def __add__(self, other: "Rational") -> "Rational":
        return Rational(
            self.first * other.second + other.first * self.second,
            self.second * other.second,
        )

    def __sub__(self, other: "Rational") -> "Rational":
        return Rational(
            self.first * other.second - other.first * self.second,
            self.second * other.second,
        )

    def __float__(self) -> float:
        return self.first / self.second
    
    def __lt__(self, other: "Rational") -> bool:
        return self.first * other.second < other.first * self.second
    
    def __gt__(self, other: "Rational") -> bool:
        return self.first * other.second > other.first * self.second
    
    def __eq__(self, other: "Rational") -> bool:
        return self.first * other.second == other.first * self.second
    
    def __str__(self) -> str:
        return f"{self.first}/{self.second}"

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
