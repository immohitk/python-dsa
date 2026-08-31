class Node:
    """A single node in a singly linked list."""

    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list implementation."""

    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        """Return True if the linked list contains no nodes."""
        return self.head is None

    def append(self, data: int) -> None:
        """Add a node to the end of the linked list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def prepend(self, data: int) -> None:
        """Add a node to the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, target: int) -> bool:
        """Return True if target exists in the linked list."""
        current = self.head

        while current is not None:
            if current.data == target:
                return True

            current = current.next

        return False

    def delete(self, target: int) -> bool:
        """Delete the first node containing target.

        Return True if a node was deleted, otherwise False.
        """
        if self.head is None:
            return False

        if self.head.data == target:
            self.head = self.head.next
            return True

        current = self.head

        while current.next is not None:
            if current.next.data == target:
                current.next = current.next.next
                return True

            current = current.next

        return False

    def to_list(self) -> list[int]:
        """Return the linked list contents as a regular Python list."""
        values = []
        current = self.head

        while current is not None:
            values.append(current.data)
            current = current.next

        return values

    def __len__(self) -> int:
        """Return the number of nodes in the linked list."""
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count