def find_max(numbers: list[int]) -> int:
    """Return the largest number in a list."""
    if not numbers:
        raise ValueError("The list cannot be empty.")

    maximum = numbers[0]

    for number in numbers[1:]:
        if number > maximum:
            maximum = number

    return maximum


def find_min(numbers: list[int]) -> int:
    """Return the smallest number in a list."""
    if not numbers:
        raise ValueError("The list cannot be empty.")

    minimum = numbers[0]

    for number in numbers[1:]:
        if number < minimum:
            minimum = number

    return minimum


def calculate_sum(numbers: list[int]) -> int:
    """Return the sum of all numbers in a list."""
    total = 0

    for number in numbers:
        total += number

    return total


def reverse_array(numbers: list[int]) -> list[int]:
    """Return a new list containing the elements in reverse order."""
    return numbers[::-1]


def linear_search(numbers: list[int], target: int) -> int:
    """Return the index of target, or -1 if it is not found."""
    for index, number in enumerate(numbers):
        if number == target:
            return index

    return -1