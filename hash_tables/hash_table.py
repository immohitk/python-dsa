class HashTable:
    """A simple hash table implementation using separate chaining."""

    def __init__(self, capacity: int = 10):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        self._buckets = [[] for _ in range(capacity)]
        self._size = 0

    def _hash(self, key: str) -> int:
        """Return the bucket index for a key."""
        return hash(key) % len(self._buckets)

    def insert(self, key: str, value: object) -> None:
        """Insert a key-value pair or update an existing key."""
        index = self._hash(key)
        bucket = self._buckets[index]

        for position, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[position] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

    def get(self, key: str) -> object:
        """Return the value associated with a key.

        Raises:
            KeyError: If the key does not exist.
        """
        index = self._hash(key)

        for existing_key, value in self._buckets[index]:
            if existing_key == key:
                return value

        raise KeyError(key)

    def contains(self, key: str) -> bool:
        """Return True if the key exists."""
        index = self._hash(key)

        return any(
            existing_key == key
            for existing_key, _ in self._buckets[index]
        )

    def delete(self, key: str) -> bool:
        """Delete a key-value pair.

        Return True if deleted, otherwise False.
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for position, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket.pop(position)
                self._size -= 1
                return True

        return False

    def size(self) -> int:
        """Return the number of stored key-value pairs."""
        return self._size

    def is_empty(self) -> bool:
        """Return True if the hash table contains no items."""
        return self._size == 0