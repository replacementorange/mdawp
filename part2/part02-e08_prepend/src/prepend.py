#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, start: str) -> None:
	    #  initializer stores the parameter in an instance attribute start
	    self.start = start

    def write(self, s: str):
	    # method write(s) which prints the string s prepended with the start string
	    print(f"{self.start}{s}")

def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
