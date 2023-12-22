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

def test_print_linked_list(populated_linked_list):
    ll = populated_linked_list
    ll.print_list()
    current_node = ll.head
    for n in range(1, 11):
        assert current_node.data == n
        current_node = current_node.next
