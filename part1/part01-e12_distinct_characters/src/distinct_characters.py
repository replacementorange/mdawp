#!/usr/bin/env python3

def distinct_characters(L):
	result = {}
	for item in L:
	    item_set = set(item)
	    result[item] = len(item_set)
	return result

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
