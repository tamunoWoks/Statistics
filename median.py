data1=[1,2,5,10,-20,5,5]

def median(data):
    """
    Returns the median of a list of numbers.
    The median is the middle value in an ordered list.
    If the list has an even number of elements, the median is the average of the two middle values.
    """

    # Handle edge case (empty list): 
    if not data:
        return None  # Could also raise a ValueError if preferred

    # Sort the data (creates a new sorted list):
    sorted_data = sorted(data)

    # Calculate the midpoint index:
    n = len(sorted_data)
    mid = n // 2

    # Return median based on even/odd length:
    if n % 2 == 1:
        # Odd number of elements: return the middle one
        return sorted_data[mid]
    else:
        # Even number of elements: return the average of the two middle values
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2

print(median(data1))
