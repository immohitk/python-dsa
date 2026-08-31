from strings.string_operations import (
    are_anagrams,
    character_frequency,
    first_non_repeating_character,
    is_palindrome,
    remove_duplicate_characters,
    reverse_string,
)


def test_reverse_string():
    assert reverse_string("hello") == "olleh"


def test_is_palindrome():
    assert is_palindrome("madam") is True


def test_is_palindrome_with_spaces_and_capitals():
    assert is_palindrome("Never Odd Or Even") is True


def test_character_frequency():
    assert character_frequency("hello") == {
        "h": 1,
        "e": 1,
        "l": 2,
        "o": 1,
    }


def test_are_anagrams():
    assert are_anagrams("listen", "silent") is True


def test_are_anagrams_with_spaces_and_capitals():
    assert are_anagrams("Dormitory", "Dirty Room") is True


def test_first_non_repeating_character():
    assert first_non_repeating_character("aabbcdde") == "c"


def test_first_non_repeating_character_when_none_exists():
    assert first_non_repeating_character("aabbcc") is None


def test_remove_duplicate_characters():
    assert remove_duplicate_characters("programming") == "progamin"


def test_remove_duplicate_characters_preserves_order():
    assert remove_duplicate_characters("banana") == "ban"