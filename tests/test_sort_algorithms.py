from sorting.sort_algorithms import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort,
)


SORT_FUNCTIONS = [
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
]


def test_bubble_sort():
    assert bubble_sort([5, 2, 8, 1, 3]) == [1, 2, 3, 5, 8]


def test_selection_sort():
    assert selection_sort([5, 2, 8, 1, 3]) == [1, 2, 3, 5, 8]


def test_insertion_sort():
    assert insertion_sort([5, 2, 8, 1, 3]) == [1, 2, 3, 5, 8]


def test_merge_sort():
    assert merge_sort([5, 2, 8, 1, 3]) == [1, 2, 3, 5, 8]


def test_quick_sort():
    assert quick_sort([5, 2, 8, 1, 3]) == [1, 2, 3, 5, 8]


def test_sort_empty_list():
    for sort_function in SORT_FUNCTIONS:
        assert sort_function([]) == []


def test_sort_single_element():
    for sort_function in SORT_FUNCTIONS:
        assert sort_function([42]) == [42]


def test_sort_already_sorted_list():
    numbers = [1, 2, 3, 4, 5]

    for sort_function in SORT_FUNCTIONS:
        assert sort_function(numbers) == [1, 2, 3, 4, 5]


def test_sort_reverse_sorted_list():
    numbers = [5, 4, 3, 2, 1]

    for sort_function in SORT_FUNCTIONS:
        assert sort_function(numbers) == [1, 2, 3, 4, 5]


def test_sort_with_duplicates():
    numbers = [4, 2, 4, 1, 2, 4]

    for sort_function in SORT_FUNCTIONS:
        assert sort_function(numbers) == [1, 2, 2, 4, 4, 4]


def test_sort_with_negative_numbers():
    numbers = [3, -1, 5, -7, 0, 2]

    for sort_function in SORT_FUNCTIONS:
        assert sort_function(numbers) == [-7, -1, 0, 2, 3, 5]


def test_sort_does_not_modify_original_list():
    numbers = [5, 3, 1, 4, 2]
    original = numbers.copy()

    for sort_function in SORT_FUNCTIONS:
        sort_function(numbers)
        assert numbers == original


def test_sort_larger_input():
    numbers = [12, 5, 8, 1, 19, 3, 7, 2, 15, 10]

    expected = [1, 2, 3, 5, 7, 8, 10, 12, 15, 19]

    for sort_function in SORT_FUNCTIONS:
        assert sort_function(numbers) == expected