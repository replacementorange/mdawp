#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
	result = []
	with open(filename, 'r') as f:
	    for line in f:
	        # re search: 
	        # -rwxr-xr-x 1 jttoivon hyad-all    2356 Dec 11 11:50 add_colab_link.py
	        # # did not use \w: `\w` same as `[a-zA-Z0-9_]`, matches one alphanumeric --> no numbers
	        matched = re.search(r"\b(\d+) ([A-Z][a-z][a-z]) \s*(\d{1,2}) (\d{2})\:(\d{2}) (\S+\b)", line)
	        # The method groups() of the match object returns the tuple of all the substrings matched by the groups of the pattern. 
	        group = matched.groups()
	        # Appending in the right format
	        # The call mo.groups() returns a tuple (’45’, ’890’). the call mo.group(1) will return ’45’. 
	        result.append((int(group[0]), group[1], int(group[2]), int(group[3]), int(group[4]), group[5]))
	
	return result

def main():
    listed_file = file_listing()
    for i in listed_file:
	    print(i)

if __name__ == "__main__":
    main()
