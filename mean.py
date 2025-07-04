def mean(data):
    """
    Returns the mean (average) of a list of numbers.
    The mean is calculated as the sum of the numbers divided by the count.
    """

    # Handle edge case: empty list
    if not data:
        return None  # Could also raise a ValueError if preferred
