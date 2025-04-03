#!/usr/bin/env python3

import pandas as pd

def cities():
    index = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]
    population_series = pd.Series([643272, 279044, 231853, 223027, 201810], index)
    area_series = pd.Series([715.48, 528.03, 689.59, 240.35, 3817.5], index)
    
    return pd.DataFrame({"Population": population_series, "Total area": area_series})
    
def main():
    #print(cities())
    cities()
    
if __name__ == "__main__":
    main()
