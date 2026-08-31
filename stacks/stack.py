class Stack:
    """A stack data structure following LIFO (Last In, First Out)."""

    def __init__(self):
        self._items = []

    def is_empty(self) -> bool:
        """Return True if the stack contains no items."""
        return len(self._items) == 0

    def push(self, item: int) -> None:
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self) -> int:
        """Remove and return the top item.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")

        return self._items.pop()

    def peek(self) -> int:
        """Return the top item without removing it.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")

        return self._items[-1]

    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)