#!/usr/bin/env python3

def merge(L1, L2):
	list = []
	i = 0
	j = 0

	while i < len(L1) and j < len(L2):
	    if L1[i] < L2[j]:
	        list.append(L1[i])
	        i += 1
	    else:
	        list.append(L2[j])
	        j += 1

	list += L1[i:] + L2[j:]
	return list

def main():
    L1 = [1,2,3,4]
    L2 = [5,6,7,8]
    print(merge(L1,L2))

if __name__ == "__main__":
    main()
