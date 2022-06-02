
'''

LL([1,57,88])

LinkedList:
    first item: head
        - the first Node is called as head
    last item: tail
        - its next addres is None
        - the last Node is called as tail
Node:
    (data)    (ref/add of next item)

'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

'''
LL = ( Node(1,addr(57)), Node(57,None) )
ll.head = Node(1,None)
ll.tail = Node(1,None)
'''

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)

    def add_node(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        return self.tail
        
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        return ' -> '.join([str(node) for node in self])

ll = LinkedList([1, 57, 88])
print(f'Linked List: {ll}')
for item in ll:
    print(f'Item: {item}, next: {item.next}')
