import scipy

import numpy

def deriv(f, x, eps = 1e-5):
    return (f(x+eps) - f(x)) / eps


def deriv2(f, x, eps = 1e-5):
    return (deriv(f, x+eps, eps) - deriv(f, x, eps)) / eps


def optimize(x0, f, tol = 1e-4):
    x_new = x0 - deriv(f, x0) / deriv2(f, x0)
    x = x0
    while abs(x_new - x) > tol:
        x = x_new
        x_new = x - deriv(f, x) / deriv2(f, x)
    return {"x": x_new,
            'value': f(x_new)}

def some_function(x):
    """create test function for which optimize finds a minimum"""
    y = x**2
    return y

optimize(0, some_function)

help(scipy.differentiate)
help(numpy.linalg.solve)

# numpy.linalg.solve(H, g)