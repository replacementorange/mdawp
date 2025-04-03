#!/usr/bin/env python3

def reverse_dictionary(eng_fi_dict): # d
	# d for reversed order
	fi_eng_dict = {}
	# iterating trough original dict
	for eng_word, fin_words in eng_fi_dict.items():
	    # reversing order in fi_eng_dict
	    for fin_word in fin_words:
	        # word not in dictionary
	        if fin_word not in fi_eng_dict:
	            # fi == eng
	            fi_eng_dict[fin_word] = [eng_word]
	        # else append it
	        else:
	            fi_eng_dict[fin_word].append(eng_word)
	# returning reversed dictionary
	return fi_eng_dict

def main():
	d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
	print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
