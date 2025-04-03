#!/usr/bin/env python3

def word_frequencies(filename):
	# dict for output
	result = {}
    
	# reading file and removing punctuation
	with open(filename, 'r') as f:
	    uncleared = f.read().split()
	
	clear = [item.strip("""!"#$%&'()*,-./:;?@[]_""") for item in uncleared]
	
	# iteration
	for item in clear:
	    # if item exists them add 1
	    if item in result:
	        result[item] += 1
	    # if not them == 1
	    else:
	        result[item] = 1
	
	return result

def main():
    print(word_frequencies("src/alice.txt"))

if __name__ == "__main__":
    main()
