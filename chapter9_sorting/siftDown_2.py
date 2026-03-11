def sift_down(array, start, end):
    """
    This function sinks (if necessary) the given node of a MaxHeap structure

    Parameters:
    - array: The heap array
    - start: The index of the node that should be sinked.
    - end: The end of the heap inside the array. The index of the last node

    Returns: None
    """
    root = start

    while True:
        left = 2 * root + 1
        right = 2 * root + 2
        largest = root

        # Check left child
        if left <= end and array[left] > array[largest]:
            largest = left

        # Check right child
        if right <= end and array[right] > array[largest]:
            largest = right

        # If the largest is still the root, heap property is satisfied
        if largest == root:
            break

        # Swap with the larger child
        array[root], array[largest] = array[largest], array[root]
        root = largest