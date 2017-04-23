"""
RANDOM DISTRIBUTION GENRATOR

The following code generates three types of random distrubutions:

1. A random floating point distribution that generates a equally distributed histogram
2. A uniform distirbution that generates a histogram with two peaks
3. A exponential distribution that generates a histogram with exponentially decreasing peaks for frequencies

NumPy random number generator modules are used to genrate random numbers between 0 and 1
"""

import matplotlib.pyplot as plt
import numpy
import matplotlib.mlab
import random

#random
rand_random = numpy.random.ranf(1000)
plt.hist(rand_random)
plt.show()

#uniform
rand_uniform = numpy.random.uniform([0,1,1000])
plt.hist(rand_uniform)
plt.show()

#exponential
rand_exponential = numpy.random.exponential(1,1000)
plt.hist(rand_exponential)
plt.show()





