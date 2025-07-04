def median(data):
    """
    Returns the median of a list of numbers.
    The median is the middle value in an ordered list.
    If the list has an even number of elements, the median is the average of the two middle values.
    """

    # Handle edge case: empty list
    if not data:
        return None  # Could also raise a ValueError if preferred

    # Step 1: Sort the data (creates a new sorted list)
    sorted_data = sorted(data)

    # Step 2: Calculate the midpoint index
    n = len(sorted_data)
    mid = n // 2
