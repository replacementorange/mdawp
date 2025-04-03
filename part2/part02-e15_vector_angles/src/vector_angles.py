#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):

	dot_product = np.sum(X * Y, axis=1)
	
	magnitude_x = scipy.linalg.norm(X, axis=1)
	magnitude_y = scipy.linalg.norm(Y, axis=1)
	
	theta = dot_product / (magnitude_x * magnitude_y)
	
	clipped_theta = np.clip(theta, -1.0, 1.0)
	
	angle_rad = np.arccos(clipped_theta)
	
	angle_deg = np.degrees(angle_rad)
	
	return angle_deg

def main():
	x = np.arange(6).reshape(2, 3)
	y = np.arange(6, 12).reshape(2, 3)
	print(x)
	print(y)

	print(vector_angles(x, y))

if __name__ == "__main__":
    main()
