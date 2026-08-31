def reverse_string(text: str) -> str:
    """Return the string in reverse order."""
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """Return True if the text reads the same forward and backward."""
    cleaned_text = text.lower().replace(" ", "")
    return cleaned_text == cleaned_text[::-1]


def character_frequency(text: str) -> dict[str, int]:
    """Return the frequency of each character in the string."""
    frequency = {}

    for character in text:
        frequency[character] = frequency.get(character, 0) + 1

    return frequency


def are_anagrams(first: str, second: str) -> bool:
    """Return True if two strings contain the same characters."""
    first_cleaned = first.lower().replace(" ", "")
    second_cleaned = second.lower().replace(" ", "")

    return sorted(first_cleaned) == sorted(second_cleaned)


def first_non_repeating_character(text: str) -> str | None:
    """Return the first character that appears only once."""
    frequency = character_frequency(text)

    for character in text:
        if frequency[character] == 1:
            return character

    return None


def remove_duplicate_characters(text: str) -> str:
    """Return the string with duplicate characters removed."""
    seen = set()
    result = []

    for character in text:
        if character not in seen:
            seen.add(character)
            result.append(character)

    return "".join(result)