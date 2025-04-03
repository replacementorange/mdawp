#!/usr/bin/env python3

def transform(s1, s2):
    return [int(s1_item) * int(s2_item) for s1_item, s2_item in zip(map(int, s1.split()), map(int, s2.split()))]

def main():
    print(transform("1 5 3", "2 6 -1")) # [2, 30, -3]

if __name__ == "__main__":
    main()
