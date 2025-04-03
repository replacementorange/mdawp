#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    x = (a.shape[1]-1)/2 # x center
    y = (a.shape[0]-1)/2 # y center
    return (y,x)   # note the order: (center_y, center_x)

def radial_distance(a):
    height, weight = a.shape[0], a.shape[1]
    y, x = center(a)

    Y = np.full((weight, height), range(height)).T
    X = np.full((height, weight), range(weight))

    return np.sqrt((Y - y) ** 2 + (X - x) ** 2)

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    a_scaled = np.interp(a, (a.min(), a.max()), (tmin, tmax))
    return a_scaled

def radial_mask(a):
    return scale(1 - radial_distance(a))

def radial_fade(a):
    return a * radial_mask(a)[:,:, np.newaxis]

def main():

    print(center(np.zeros((10, 11, 3)))) # (4.5, 5)

    # Copy of original image
    image = plt.imread("src/painting.png").copy()

    # 3,1 subplot
    f, ax = plt.subplots(3,1)

    ax[0].imshow(image)                 # orig image
    ax[1].imshow(radial_mask(image))    # image with radial mask
    ax[2].imshow(radial_fade(image))    # image with radial fade

    plt.show()

if __name__ == "__main__":
    main()
