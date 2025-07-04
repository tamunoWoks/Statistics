def mode(data):
    """
    Returns the mode(s) of a list of numbers.
    The mode is the value(s) that appear most frequently.
    If multiple values share the highest frequency, all are returned in a list.
    """

    # Handle edge case (empty list):
    if not data:
        return None  # Or raise ValueError if preferred

    # Count occurrences using a dictionary:
    freq = {}
    for num in data:
        freq[num] = freq.get(num, 0) + 1

    # Find the highest frequency:
    max_freq = max(freq.values())
