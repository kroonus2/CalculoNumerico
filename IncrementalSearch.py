import numpy as np


def f(x):
    return 2*(np.exp(x)) - 3


def root(func, a, b, dx):
    z = a
    while True:
        f1 = func(z)
        f2 = func(z + dx)
        if f1*f2 < 0:
            return z, z+dx
        z = z + dx
        if z >= b:
            return (None, None)


x, y = root(f, 0.0, 1.0, 0.2)
print(x, y)
