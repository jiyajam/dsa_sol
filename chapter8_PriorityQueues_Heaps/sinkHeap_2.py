class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        # Start at the end of the heap
        index = self._size - 1
        # Calculate index of parent element
        parent_index = (index-1) // 2
        # While not at Root node and value less than its parent
        while index > 0 and self._heap[index] < self._heap[parent_index]:
            # swap value with its parent
            self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            # Update indices
            index = parent_index
            parent_index = (index-1) // 2

    def insert(self, value):
        # Add the value to the heap
        self._heap.append(value)
        # Update size of the heap
        self._size += 1
        # And float the last element of the heap
        self._float()

    def _sink(self):
        """
        Sinks the root node of the heap until the heap property is restored.
        """
        index = 0

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            # Check left child
            if left < self._size and self._heap[left] < self._heap[smallest]:
                smallest = left

            # Check right child
            if right < self._size and self._heap[right] < self._heap[smallest]:
                smallest = right

            # If the smallest is still the parent, heap is valid
            if smallest == index:
                break

            # Swap with the smaller child
            self._heap[index], self._heap[smallest] = \
                self._heap[smallest], self._heap[index]

            index = smallest