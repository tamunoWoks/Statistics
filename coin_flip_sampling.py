# Import necessary modules
import random
from math import sqrt
from plotting import * 

# Function to calculate the mean (average) of a list of numbers
def mean(data):
    return float(sum(data)) / len(data)

# Function to calculate the variance of a list of numbers
def variance(data):
    mu = mean(data)
    return sum([(x - mu) ** 2 for x in data]) / len(data)

# Function to calculate the standard deviation
def stddev(data):
    return sqrt(variance(data))
