from queues.queue import Queue


def test_new_queue_is_empty():
    queue = Queue()

    assert queue.is_empty() is True
    assert queue.size() == 0


def test_enqueue_adds_item():
    queue = Queue()

    queue.enqueue(10)

    assert queue.is_empty() is False
    assert queue.size() == 1
    assert queue.front() == 10


def test_enqueue_multiple_items():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    assert queue.size() == 3
    assert queue.front() == 10


def test_dequeue_returns_front_item():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    assert queue.dequeue() == 10
    assert queue.size() == 2


def test_queue_follows_fifo():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.dequeue() == 30
    assert queue.is_empty() is True


def test_front_does_not_remove_item():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)

    assert queue.front() == 10
    assert queue.size() == 2
    assert queue.front() == 10


def test_dequeue_empty_queue_raises_error():
    queue = Queue()

    try:
        queue.dequeue()
        assert False
    except IndexError:
        assert True


def test_front_empty_queue_raises_error():
    queue = Queue()

    try:
        queue.front()
        assert False
    except IndexError:
        assert True