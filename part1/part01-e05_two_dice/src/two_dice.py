#!/usr/bin/env python3

def main():
	for first_dice in range(1, 7):
	    for second_dice in range(1, 7):
	        if first_dice + second_dice == 5:
	            print(f"({first_dice}, {second_dice})")
                
if __name__ == "__main__":
    main()
