# Import necessary modules
import random
from math import sqrt

# Function to calculate the mean (average) of a list of numbers
def mean(data):
    return float(sum(data)) / len(data)

# Function to calculate the variance of a list of numbers
def variance(data):
    mu = mean(data)  # Compute the mean first
    return sum([(x - mu)**2 for x in data]) / len(data)
