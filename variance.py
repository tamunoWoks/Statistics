data3=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]

# Define mean():
def mean(data):
    return sum(data)/len(data)

# Define variance():
def variance(data):
    """
    Returns the variance of a list of numbers.
    Variance measures how far each number in the list is from the mean.
    Formula: sum((x - mean)^2) / n
    """

    # Handle edge case (empty list):
    if not data:
        return None  # Handle empty list

    # Compute mean:
    m = mean(data)
    
    # Square the differences from mean:
    squared_diffs = [(x - m) ** 2 for x in data]

    # Return average of squared differences:
    return sum(squared_diffs) / len(data)
