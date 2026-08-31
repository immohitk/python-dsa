from linked_lists.linked_list import LinkedList, Node


def test_node_stores_data():
    node = Node(10)

    assert node.data == 10
    assert node.next is None


def test_new_linked_list_is_empty():
    linked_list = LinkedList()

    assert linked_list.is_empty() is True
    assert len(linked_list) == 0


def test_append():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    assert linked_list.to_list() == [10, 20, 30]
    assert len(linked_list) == 3


def test_prepend():
    linked_list = LinkedList()

    linked_list.append(20)
    linked_list.append(30)
    linked_list.prepend(10)

    assert linked_list.to_list() == [10, 20, 30]
    assert len(linked_list) == 3


def test_search_existing_value():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    assert linked_list.search(20) is True


def test_search_missing_value():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)

    assert linked_list.search(50) is False


def test_delete_middle_node():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    assert linked_list.delete(20) is True
    assert linked_list.to_list() == [10, 30]


def test_delete_head_node():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    assert linked_list.delete(10) is True
    assert linked_list.to_list() == [20, 30]


def test_delete_last_node():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    assert linked_list.delete(30) is True
    assert linked_list.to_list() == [10, 20]


def test_delete_missing_value():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)

    assert linked_list.delete(50) is False
    assert linked_list.to_list() == [10, 20]


def test_delete_from_empty_list():
    linked_list = LinkedList()

    assert linked_list.delete(10) is False
    assert linked_list.to_list() == []


def test_linked_list_can_become_empty():
    linked_list = LinkedList()

    linked_list.append(10)

    assert linked_list.delete(10) is True
    assert linked_list.is_empty() is True
    assert len(linked_list) == 0