#!/usr/bin/env python
import numpy as np

def mandel_z(complex_number):
    """
    Takes a complex coordinate and returns the number of iterations it
    takes to determine whether that point is outside of the Mandelbrot set.
    """
    z = complex_number
    it = 0
    maxit = 256
    while abs(z) < 2 and it < maxit:
       z = z*z + complex_number
       it += 1
    return it
    
def grid(xvals, yvals):
    data = np.zeros(len(xvals)*len(yvals), np.complex128)
    index = 0
    for x in xvals:
        for y in yvals:
            data[index] = complex(x,y)
            index += 1
    return data
    
def create_mandel(min_x, max_x, min_y, max_y, size):
    
    x_vals = np.linspace(min_x, max_x, size)
    y_vals = np.linspace(min_y, max_y, size)
    
    data = grid(x_vals, y_vals)
    
    z = map(mandel_z, data)
    
    return z
    
            