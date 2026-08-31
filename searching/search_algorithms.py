def linear_search(numbers: list[int], target: int) -> int:
    """Return the index of target using linear search.

    Return -1 if the target is not found.
    """
    for index, number in enumerate(numbers):
        if number == target:
            return index

    return -1


def binary_search(numbers: list[int], target: int) -> int:
    """Return the index of target using iterative binary search.

    The input list must be sorted in ascending order.
    Return -1 if the target is not found.
    """
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def binary_search_recursive(
    numbers: list[int],
    target: int,
    left: int = 0,
    right: int | None = None,
) -> int:
    """Return the index of target using recursive binary search.

    The input list must be sorted in ascending order.
    Return -1 if the target is not found.
    """
    if right is None:
        right = len(numbers) - 1

    if left > right:
        return -1

    middle = (left + right) // 2

    if numbers[middle] == target:
        return middle

    if numbers[middle] < target:
        return binary_search_recursive(
            numbers,
            target,
            middle + 1,
            right,
        )

    return binary_search_recursive(
        numbers,
        target,
        left,
        middle - 1,
    )