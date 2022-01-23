""" Advanced linked list (Doubly linked list) """

#not complete

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class doubly_linked_list:
    def __init__(self):
        self.head = None
    
    def push(self, new_val):
        NewNode = Node(new_val)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
    
    def listprint(self, node):
        while node is not None:
            print(node.data)
            last = node
            node = node.next

def main():
    dllist = doubly_linked_list()
    dllist.push(12)
    dllist.push(8)
    dllist.push(62)
    dllist.listprint(dllist.head)


if __name__ == "__main__":
    main()