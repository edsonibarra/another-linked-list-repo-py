import pytest
from node import Node
from linked_list import LinkedList


@pytest.fixture
def populated_linked_list() -> LinkedList:
    """Returns a populated linked list"""
    ll : LinkedList = LinkedList()
    for n in range(1, 11):
        ll.append(n)
    return ll
