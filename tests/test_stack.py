import pytest


def test_stack():
    stack = []
    stack.append('a')
    stack.append('b')


    assert stack.pop() == 'b'
    assert stack.pop() == 'a'
    

def test_stack_emptiness():
    stack = []
    assert not stack
    stack.append('a')
    assert bool(stack)


    stack.pop()
    assert not stack


def test_pop_with_empty_stack():
    stack = []


    with pytest.raises(IndexError):
        stack.pop()

