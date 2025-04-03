#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    output = []
    with open(filename, 'r') as f:
        next(f)
        output = [f"{match[0][0]}\t{match[0][1]}\t{match[0][2]}\t{match[0][3]}" # r g b name
	        for match in (re.findall(r'(\d+)\s*(\d+)\s*(\d+)\s*\s(.*)', line) for line in f)]

    return output

def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
