# Import square root function from the math module:
from math import sqrt

# Sample dataset:
data3 = [13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]

def mean(data):
    """
    Calculates the mean (average) of a list of numbers.
    """
    return sum(data) / len(data)
