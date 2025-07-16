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

# Function to simulate flipping N fair coins
# Returns a list of boolean values: True for heads, False for tails
def flip(N):
    return [random.random() > 0.5 for _ in range(N)]

# Function to simulate N sets of N coin flips
# Returns a list of the proportion of heads in each set
def sample(N):
    # Perform N experiments, each of N coin flips
    return [mean(flip(N)) for _ in range(N)]
