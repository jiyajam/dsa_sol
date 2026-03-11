def insertion_sort(array):
    """
    Sort the array using the Insertion sort algorithm

    Parameters:
    - array: The array to be sorted

    Returns: Nothing. The array is sorted in-place.
    """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        # Shift elements to the right until the correct position is found
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        # Insert the key in its correct position
        array[j + 1] = key