# importing numpy
import numpy as np
from random import randint

# Creating an array of 10 random ints
arr = np.random.rand(10)

print('Random Numbers:')
print(arr)

# Finding the mean, median, and standard deviation of the array
mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)

# Printing out the mean, median, and standard deviation
print("Mean:", mean, ', ', end = '')
print("Median:", median, ', ', end = '')
print("Standard Deviation:", std)