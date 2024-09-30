class Node:
    data : int
    next_node : "Node"
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    head = "None"

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node


    def bubble_sort(self):
        current_node = self.head
        swapped = True

        while swapped:
            swapped = False
            previous_node = None
            current_node = self.head

            while current_node is not None and current_node.next_node is not None:
                next_node = current_node.next_node

                if current_node.data > next_node.data:
                    if previous_node is None:
                        aux_node = next_node.next_node
                        self.head = next_node
                        previous_node = current_node
                        next_node.next_node = current_node
                        current_node.next_node = aux_node
                    else:
                        aux_node = next_node.next_node
                        previous_node.next_node = next_node
                        next_node.next_node = current_node
                        current_node.next_node = aux_node
                    swapped = True
                previous_node = current_node
                current_node = current_node.next_node

node4 = Node(1)
node3 = Node(2,node4)
node2 = Node(3, node3)
node1 = Node(4, node2)


linked_list_object = LinkedList(node1)
linked_list_object.print_structure()
print("After bubble sort")
linked_list_object.bubble_sort()
linked_list_object.print_structure()