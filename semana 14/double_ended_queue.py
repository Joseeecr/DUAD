class Node:
    data : str
    next: "Node"

    def __init__(self, data, next= None, prev = None):
        self.data = data
        self.next = next


class DoubleEndedQueue:
    head: Node
    tail: Node

    def __init__(self, head):
        self.head = head
        self.tail = None

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def pop_left(self):
        if self.head:
            self.head = self.head.next

    def push_left(self, new_node):
        current_node = self.head
        new_node.next = current_node
        self.head = new_node

    def pop_right(self):
        current_node = self.head

        while current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None
        self.tail = current_node

    def push_right(self, new_node):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node


third_node= Node("I'm the third node")
second_node = Node("I'm the second node", third_node)
first_node = Node("I'm the first node", second_node)
new_node = Node("New node")
new_node_2 = Node("New node 2")
stack_structure = DoubleEndedQueue(first_node)



stack_structure.push_left(new_node)
stack_structure.push_right(new_node_2)
stack_structure.print_structure()
print("\nPopped left and right")
stack_structure.pop_left()
stack_structure.pop_right()

stack_structure.print_structure()