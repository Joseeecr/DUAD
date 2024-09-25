class Node:
    data : str
    next: "Node"

    def __init__(self, data, next= None):
        self.data = data
        self.next = next


class Stack:
    top: Node

    def __init__(self, top):
        self.top = top

    def print_structure(self):
        current_node = self.top

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def pop(self):
        if self.top:
            self.top = self.top.next

    def push(self, new_node):
        current_node = self.top
        new_node.next = current_node
        self.top = new_node


third_node= Node("I'm the third node")
second_node = Node("I'm the second node", third_node)
first_node = Node("I'm the first node", second_node)

stack_structure = Stack(first_node)

fourth_node = Node("Im new!")
stack_structure.push(fourth_node)
print("PUSH")
stack_structure.print_structure()
print("POP")
stack_structure.pop()
stack_structure.print_structure()