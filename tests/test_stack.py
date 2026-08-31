from stacks.stack import Stack


def test_new_stack_is_empty():
    stack = Stack()

    assert stack.is_empty() is True
    assert stack.size() == 0


def test_push_adds_item():
    stack = Stack()

    stack.push(10)

    assert stack.is_empty() is False
    assert stack.size() == 1
    assert stack.peek() == 10


def test_push_multiple_items():
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.size() == 3
    assert stack.peek() == 30


def test_pop_returns_top_item():
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.pop() == 30
    assert stack.size() == 2


def test_stack_follows_lifo():
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.is_empty() is True


def test_peek_does_not_remove_item():
    stack = Stack()

    stack.push(10)
    stack.push(20)

    assert stack.peek() == 20
    assert stack.size() == 2
    assert stack.peek() == 20


def test_pop_empty_stack_raises_error():
    stack = Stack()

    try:
        stack.pop()
        assert False
    except IndexError:
        assert True


def test_peek_empty_stack_raises_error():
    stack = Stack()

    try:
        stack.peek()
        assert False
    except IndexError:
        assert True