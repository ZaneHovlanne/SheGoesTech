# TODO
# 1. plot a graph of x and y
# x would be values from -10 to 10 (21 values)
# y would be the cube of x + 5

# you could use a different library than matplotlib but it is the most popular one
# will will explore other ones later on in the course

from matplotlib import pyplot as plt
import numpy as np


def f(x):
    return (x+5)**2


xlist = np.linspace(-10, 10)
ylist = f(xlist)

plt.figure(num=0, dpi=120)

plt.plot(xlist, ylist)
plt.show()
