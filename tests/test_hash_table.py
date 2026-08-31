from hash_tables.hash_table import HashTable


def test_new_hash_table_is_empty():
    table = HashTable()

    assert table.is_empty() is True
    assert table.size() == 0


def test_insert_and_get():
    table = HashTable()

    table.insert("name", "Mohit")

    assert table.get("name") == "Mohit"
    assert table.size() == 1


def test_insert_multiple_items():
    table = HashTable()

    table.insert("name", "Mohit")
    table.insert("role", "Python Developer")
    table.insert("experience", "Entry Level")

    assert table.get("name") == "Mohit"
    assert table.get("role") == "Python Developer"
    assert table.get("experience") == "Entry Level"
    assert table.size() == 3


def test_update_existing_key():
    table = HashTable()

    table.insert("name", "Mohit")
    table.insert("name", "Mohit Kumar")

    assert table.get("name") == "Mohit Kumar"
    assert table.size() == 1


def test_contains_existing_key():
    table = HashTable()

    table.insert("language", "Python")

    assert table.contains("language") is True


def test_contains_missing_key():
    table = HashTable()

    table.insert("language", "Python")

    assert table.contains("database") is False


def test_delete_existing_key():
    table = HashTable()

    table.insert("name", "Mohit")
    table.insert("role", "Python Developer")

    assert table.delete("name") is True
    assert table.contains("name") is False
    assert table.size() == 1


def test_delete_missing_key():
    table = HashTable()

    table.insert("name", "Mohit")

    assert table.delete("unknown") is False
    assert table.size() == 1


def test_delete_from_empty_table():
    table = HashTable()

    assert table.delete("name") is False
    assert table.is_empty() is True


def test_get_missing_key_raises_error():
    table = HashTable()

    try:
        table.get("missing")
        assert False
    except KeyError:
        assert True


def test_empty_table_get_raises_error():
    table = HashTable()

    try:
        table.get("missing")
        assert False
    except KeyError:
        assert True


def test_collision_handling():
    table = HashTable(capacity=1)

    table.insert("first", "value1")
    table.insert("second", "value2")

    assert table.get("first") == "value1"
    assert table.get("second") == "value2"
    assert table.size() == 2


def test_collision_delete_keeps_other_item():
    table = HashTable(capacity=1)

    table.insert("first", "value1")
    table.insert("second", "value2")

    assert table.delete("first") is True
    assert table.get("second") == "value2"
    assert table.size() == 1


def test_invalid_capacity():
    try:
        HashTable(capacity=0)
        assert False
    except ValueError:
        assert True