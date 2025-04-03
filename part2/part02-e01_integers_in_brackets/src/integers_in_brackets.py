#!/usr/bin/env python3
from re import findall

def integers_in_brackets(s):
    result = findall(r"\[\s*([+-]?\d+)\s*\]", s)
    return [int(number) for number in result]

def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
