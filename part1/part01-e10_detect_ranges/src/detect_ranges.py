#!/usr/bin/env python3

def detect_ranges(L):
    sorted_L = sorted(L) # sorted L
    ranges = [] # output


    start = sorted_L[0]
    end = sorted_L[0]

    for num in sorted_L[1:]:
        if num == end + 1:
            end = num
        else:
            if start == end:
                ranges.append(start)
            else:
                ranges.append((start, end + 1))
            start = end = num

    if start == end:
        ranges.append(start)
    else:
        ranges.append((start, end + 1))

    return ranges


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
