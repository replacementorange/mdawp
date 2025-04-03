#!/usr/bin/env python3


def main():
    for i in range(1,11):
        print("", end=" ")
        for j in range(1,11):
            tulo=i*j
            print(f"{tulo}", end=" ")
        print()

if __name__ == "__main__":
    main()
