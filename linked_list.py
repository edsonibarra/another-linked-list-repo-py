from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """
        It adds a new node at the end of the linked list
        """
        # The first case is where linked list is empty
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        # head -> 1 -> 2 -> 3 -> new_node -> None
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node


    def prepend(self, data):
        """
        It adds a new node at the beginning of the linked list
        """
        # The first case is where linked list is empty
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        # head -> 1 -> 2 -> None
        # head -> new_node 
        current_node = self.head
        self.head = new_node # head -> new_node -> 1 -> 2 -> None
        new_node.next = current_node

    def print_list(self):
        """
        It prints every data node in the linked list
        """
        if self.head is None:
            return
        # head -> 1 -> 2 -> 3 -> None
        current_node = self.head
        while current_node:
            print(f"[{current_node.data}]", end="->") # [1]->[2]-[3]->None
            current_node = current_node.next
        print("None")
    
    def delete_by_value(self, value):
        """
        It deletes a node based on the value that contains
        """
        if self.head is None:
            return
        
        current_node = self.head
        previous_node = None

        if current_node.data == value:
            self.head = current_node.next
            current_node = None
            return
        
        while current_node and current_node.data != value:
            previous_node = current_node
            current_node = current_node.next
        
        if current_node:
            previous_node.next = current_node.next
            current_node = None
            return
        else:
            return # Node with data == value was not found



def main():
    ll = LinkedList()
    
    # Add the elements at the end of the linked list
    print("-- Adding nodes using append method\n")
    for i in range(1, 6):
        ll.append(i)
        ll.print_list()

    print("\n-- Adding nodes using prepend method\n")
    for i in range(6, 11):
        ll.prepend(i)
        ll.print_list()
    
    print("\nend")


if __name__ == "__main__":
    main()
