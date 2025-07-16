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

# Function to calculate the standard deviation using variance
def stddev(data):
    return sqrt(variance(data))

# Function to simulate flipping N fair coins
def flip(N):
    # For each flip, generate a random number between 0 and 1
    # If it's less than 0.5, treat it as 1 (heads), else 0 (tails)
    return [1 if random.random() < 0.5 else 0 for _ in range(N)]

# Number of coin flips to simulate
N = 1000

# Perform the simulation and store results in list 'f'
f = flip(N)

# Print the mean (should be close to 0.5 for fair coin)
print(mean(f))

# Print the standard deviation (should be close to sqrt(0.25) ≈ 0.5)
print(stddev(f))
