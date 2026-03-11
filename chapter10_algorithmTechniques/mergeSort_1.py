def merge_sort(array):
    """
    Sort the array using the Merge sort algorithm

    Parameters:
    - array: The array to be sorted

    Returns: The sorted array.
    """
    if len(array) <= 1:
        return array[:]

    mid = len(array) // 2

    # Recursively sort left and right halves
    left_sorted = merge_sort(array[:mid])
    right_sorted = merge_sort(array[mid:])

    # Merge the two sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0

    # Merge while both lists have elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result
