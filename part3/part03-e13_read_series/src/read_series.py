#!/usr/bin/env python3
import pandas as pd

def read_series():
    series = pd.Series([])

    while True: # reads inputs while true
        text = input()

        if text == "": # stops on empty line
            break

        try: # puts input into series
            index, value = text.split()
            series[index] = value
        except:
            raise Exception

    return series

def main():
    read_series()

if __name__ == "__main__":
    main()
