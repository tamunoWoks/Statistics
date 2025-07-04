def median(data):
    """
    Returns the median of a list of numbers.
    The median is the middle value in an ordered list.
    If the list has an even number of elements, the median is the average of the two middle values.
    """

    # Handle edge case: empty list
    if not data:
        return None  # Could also raise a ValueError if preferred
