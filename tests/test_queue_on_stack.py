from tasks.implement_queue_using_stacks import MyQueue


def test_queue_on_stack():
    q = MyQueue()
    q.push(5)
    q.push(4)
    q.push(3)
    assert len(q.queue) == 3
    assert q.pop() == 5
    assert q.peek() == 4
    assert q.empty() is False