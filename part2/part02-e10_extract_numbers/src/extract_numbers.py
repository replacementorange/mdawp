#!/usr/bin/env python3

def extract_numbers(s):
    result = []
    # splits orig array and iterates
    for item in s.split():
        try:
            # appends int
            result.append(int(item))
        # raises value error if not int
        except ValueError:
            try:
                # appends floats
                result.append(float(item))
            except:
                continue
    return result

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
