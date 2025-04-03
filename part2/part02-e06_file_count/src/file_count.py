#!/usr/bin/env python3

import sys

def file_count(filename):
	lines = 0
	words = 0
	chars = 0

	# open file
	with open(filename, 'r') as f:
	    for line in f:
	        # count every line
	        lines += 1
	        # count word in single line
	        words += len(line.split())
	        # counts chars in single line
	        chars += len(line)
	
	return (lines, words, chars)

def main():
    files = sys.argv[1:] # PART 2
    for file in files:
        lines, words, chars = file_count(file)
        # The fields are separated by tabs (\t)
        print(f"{lines}\t{words}\t{chars}\t{file}")

if __name__ == "__main__":
    main()
