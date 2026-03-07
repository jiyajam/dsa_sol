class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def push(self, data):
        """
        Add an element to the stack

        Parameters:
        - 'data': Data/value being added

        Returns: None
        """
        new_node=Node (data,self._top) #new node points to current top
        self._top =new_node #update top to new node
        self._size +=1


    def pop(self):
        """
        Remove the top node from the stack and return its content

        Parameters: None

        Returns: The content of the node or None if stack is empty
        """
        if self._top is None:
            return None

        popped_node = self._top
        self._top = self._top.next        # move top to next node
        self._size -= 1                   # decrease size
        return popped_node.data


    def __repr__(self):
        elements = []
        current = self._top
        while current:
            elements.append(str(current.data))
            current = current.next

        element_word = "element" if self._size == 1 else "elements"
        content = ", ".join(elements)  # join without quotes
        return f"<Stack ({self._size} {element_word}): [{content}]>"