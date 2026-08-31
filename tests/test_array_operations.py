from arrays.array_operations import (
    calculate_sum,
    find_max,
    find_min,
    linear_search,
    reverse_array,
)


def test_find_max():
    assert find_max([4, 8, 2, 10, 6]) == 10


def test_find_min():
    assert find_min([4, 8, 2, 10, 6]) == 2


def test_calculate_sum():
    assert calculate_sum([1, 2, 3, 4, 5]) == 15


def test_reverse_array():
    assert reverse_array([1, 2, 3, 4]) == [4, 3, 2, 1]


def test_linear_search_found():
    assert linear_search([10, 20, 30, 40], 30) == 2


def test_linear_search_not_found():
    assert linear_search([10, 20, 30, 40], 50) == -1


def test_empty_list_for_max():
    try:
        find_max([])
        assert False
    except ValueError:
        assert True


def test_empty_list_for_min():
    try:
        find_min([])
        assert False
    except ValueError:
        assert True