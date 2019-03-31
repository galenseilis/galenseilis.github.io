from timeit import timeit
from scipy.optimize import bisect
from scipy.optimize import newton
from scipy.optimize import brentq
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.sin(x) * np.exp(-x)


# try out the bisection algorithm

# print(bisect(f, 3, 4))

print(brentq(f, 3, 4))
