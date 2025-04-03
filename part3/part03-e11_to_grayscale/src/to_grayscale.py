#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(image):
    weights = [0.2126, 0.7152, 0.0722] # Use the weights 0.2126, 0.7152, and 0.0722
    grayscale = np.sum(weights * image, axis = 2) # a weighted sum of the red, green, and blue values, and use that as the value of gray
 
    return grayscale

def to_red(image):
	    weights = [1, 0, 0]
	    #red = weights * image # NOT np.sum(weights * image) -> TypeError: Invalid shape () for image data
	    return weights * image
	 
def to_green(image):
    weights = [0, 1, 0]
    #green = weights * image
    return weights * image
	 
def to_blue(image):
    weights = [0, 0, 1]
    #blue = weights * image
    return weights * image

def main():
    painting = plt.imread('src/painting.png') # provide image
	 
	# part 1
    grayscaled = to_grayscale(painting)
    plt.imshow(grayscaled)
    plt.show()

    # part 2
    fig, ax = plt.subplots(3, 1)        # subplots for rgb
    ax[0].imshow(to_red(painting))      # top red
    ax[1].imshow(to_green(painting))    # middle green
    ax[2].imshow(to_blue(painting))     # bottom blue
    plt.show()

if __name__ == "__main__":
    main()
