#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x,y):
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:,np.newaxis], y)

    return (model.coef_[0], model.intercept_)
    
def main():
    np.random.seed(0)
    n=20   # Number of data points
    x=np.linspace(0, 10, n)
    y=x*2 + 1 + 1*np.random.randn(n) # Standard deviation 1

    slope, intercept = fit_line(x,y) # 'model coef', intercept
    yfit = slope * x + intercept

    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")

    plt.plot(x,y, 'o')
    plt.plot(x, yfit)
    plt.show()

if __name__ == "__main__":
    main()
