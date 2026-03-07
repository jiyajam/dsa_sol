class Queue:
    def __init__(self):
        self._head = None   # New elements inserted here
        self._tail = None   # Old elements removed from here
        self._size = 0

    def enqueue(self, data):
        new_node = ListNode(data)

        if self._size == 0:
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

        self._size += 1

    def dequeue(self):
        if self._size == 0:
            return None

        removed_node = self._tail

        if self._size == 1:
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None

        self._size -= 1
        return removed_node.data

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = []
        current = self._head

        while current:
            values.append(str(current.data))
            current = current.next

        return f'<Queue ({self._size} element{plural}): [{", ".join(values)}]>'
