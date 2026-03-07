class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        """
        Float the last element of the heap until the heap is in order
        """
        index = self._size - 1
        while index > 0:
            parent_index = (index-1) // 2
            if self._heap[index] < self._heap[parent_index]:
                self._heap[index], self._heap[parent_index] = self._heap[parent_index],self._heap[index] # Swap
                index = parent_index
            else:
                break

