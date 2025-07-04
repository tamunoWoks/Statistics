# Import square root function from the math module:
from math import sqrt

# Sample dataset:
data3 = [13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]

def mean(data):
    """
    Calculates the mean (average) of a list of numbers.
    """
    return sum(data) / len(data)

def variance(data):
    """
    Calculates the variance of a list of numbers.
    Variance measures the average squared deviation from the mean.
    """
    mu = mean(data)  # Compute the mean of the dataset
    squared_diffs = [(x - mu) ** 2 for x in data]  # Square of each deviation from the mean
    return mean(squared_diffs)  # Average of squared deviations

def stddev(data):
    """
    Calculates the standard deviation of a list of numbers.
    Standard deviation is the square root of the variance.
    """
    return sqrt(variance(data))  # Use math.sqrt() to get the standard deviation

# Print output
print("Standard Deviation:", stddev(data3))
