def combine_lists(list1, list2):
    merged = []
    i, j = 0, 0  # Pointers for list1 and list2

    # Iterate until we reach the end of one list
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Add any remaining elements from list1
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    # Add any remaining elements from list2
    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged