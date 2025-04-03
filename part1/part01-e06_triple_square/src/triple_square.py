#!/usr/bin/env python3
def triple(x):
    return x * 3

def square(x):
    return x ** 2

def main():
	for i in range(1, 11):
	    triple_value = triple(i)
	    square_value = square(i)
	
	    if square_value > triple_value:
	        break
	    else:
	        print(f"triple({i})=={triple_value} square({i})=={square_value}")

if __name__ == "__main__":
    main()
