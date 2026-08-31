from collections import deque


class Queue:
    """A queue data structure following FIFO (First In, First Out)."""

    def __init__(self):
        self._items = deque()

    def is_empty(self) -> bool:
        """Return True if the queue contains no items."""
        return len(self._items) == 0

    def enqueue(self, item: int) -> None:
        """Add an item to the rear of the queue."""
        self._items.append(item)

    def dequeue(self) -> int:
        """Remove and return the front item.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")

        return self._items.popleft()

    def front(self) -> int:
        """Return the front item without removing it.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot view the front of an empty queue.")

        return self._items[0]

    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self._items)
