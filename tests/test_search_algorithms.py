from searching.search_algorithms import (
    binary_search,
    binary_search_recursive,
    linear_search,
)


def test_linear_search_finds_existing_value():
    numbers = [10, 20, 30, 40, 50]

    assert linear_search(numbers, 30) == 2


def test_linear_search_returns_minus_one_when_missing():
    numbers = [10, 20, 30, 40, 50]

    assert linear_search(numbers, 99) == -1


def test_linear_search_finds_first_duplicate():
    numbers = [10, 20, 30, 20, 40]

    assert linear_search(numbers, 20) == 1


def test_linear_search_empty_list():
    assert linear_search([], 10) == -1


def test_binary_search_finds_existing_value():
    numbers = [10, 20, 30, 40, 50, 60, 70]

    assert binary_search(numbers, 40) == 3


def test_binary_search_finds_first_value():
    numbers = [10, 20, 30, 40, 50]

    assert binary_search(numbers, 10) == 0


def test_binary_search_finds_last_value():
    numbers = [10, 20, 30, 40, 50]

    assert binary_search(numbers, 50) == 4


def test_binary_search_returns_minus_one_when_missing():
    numbers = [10, 20, 30, 40, 50]

    assert binary_search(numbers, 99) == -1


def test_binary_search_empty_list():
    assert binary_search([], 10) == -1


def test_binary_search_recursive_finds_existing_value():
    numbers = [10, 20, 30, 40, 50, 60, 70]

    assert binary_search_recursive(numbers, 60) == 5


def test_binary_search_recursive_finds_first_value():
    numbers = [10, 20, 30, 40, 50]

    assert binary_search_recursive(numbers, 10) == 0


def test_binary_search_recursive_finds_last_value():
    numbers = [10, 20, 30, 40, 50]

    assert binary_search_recursive(numbers, 50) == 4


def test_binary_search_recursive_returns_minus_one_when_missing():
    numbers = [10, 20, 30, 40, 50]

    assert binary_search_recursive(numbers, 99) == -1


def test_binary_search_recursive_empty_list():
    assert binary_search_recursive([], 10) == -1