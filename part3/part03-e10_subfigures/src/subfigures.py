#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    fig, axs = plt.subplots(1, 2)

    # plot - left subfigure
    axs[0].plot(a[:, 0], a[:, 1])
    axs[0].set_title('plot')
    axs[0].set_xlabel('x-axis')
    axs[0].set_ylabel('y-axis')

    # scatter - right subfigure 
    axs[1].scatter(a[:, 0], a[:, 1], c=a[:, 2], s=a[:, 3])
    axs[1].set_title('scatter')
    axs[1].set_xlabel('x-axis')
    axs[1].set_ylabel('y-axis')

    plt.show()

def main():
	array = np.arange(12).reshape(3, 4)
	subfigures(array)

if __name__ == "__main__":
    main()
