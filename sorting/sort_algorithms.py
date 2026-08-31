def bubble_sort(numbers: list[int]) -> list[int]:
    """Return a sorted copy using Bubble Sort."""
    result = numbers.copy()

    for i in range(len(result)):
        swapped = False

        for j in range(0, len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        if not swapped:
            break

    return result


def selection_sort(numbers: list[int]) -> list[int]:
    """Return a sorted copy using Selection Sort."""
    result = numbers.copy()

    for i in range(len(result)):
        minimum_index = i

        for j in range(i + 1, len(result)):
            if result[j] < result[minimum_index]:
                minimum_index = j

        result[i], result[minimum_index] = (
            result[minimum_index],
            result[i],
        )

    return result


def insertion_sort(numbers: list[int]) -> list[int]:
    """Return a sorted copy using Insertion Sort."""
    result = numbers.copy()

    for i in range(1, len(result)):
        current = result[i]
        position = i - 1

        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1

        result[position + 1] = current

    return result


def merge_sort(numbers: list[int]) -> list[int]:
    """Return a sorted copy using Merge Sort."""
    if len(numbers) <= 1:
        return numbers.copy()

    middle = len(numbers) // 2

    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list."""
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def quick_sort(numbers: list[int]) -> list[int]:
    """Return a sorted copy using Quick Sort."""
    if len(numbers) <= 1:
        return numbers.copy()

    pivot = numbers[len(numbers) // 2]

    smaller = [number for number in numbers if number < pivot]
    equal = [number for number in numbers if number == pivot]
    larger = [number for number in numbers if number > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)