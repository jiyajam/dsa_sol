def interpolation_search(array, value):
    """
    Performs an Interpolation search in the the array for the given value

    Parameters:
    - array: The array where to perform the search
    - value: The value being searched

    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    low = 0
    high = len(array) - 1

    while low <= high and array[low] <= value <= array[high]:

        # Avoid division by zero
        if array[high] == array[low]:
            if array[low] == value:
                return low
            else:
                return None

        # Estimate the position
        pos = low + ((value - array[low]) * (high - low)) // (array[high] - array[low])

        # If out of bounds, stop
        if pos < low or pos > high:
            return None

        if array[pos] == value:
            return pos
        elif array[pos] < value:
            low = pos + 1
        else:
            high = pos - 1

    return None