class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
count = 0
class LinkedList:
    def __init__(self):
        self.head = None
        last = self.head
    def countt(self,last):
        last = self.head 
        while (last.next):
            last = last.next
            countval = countval + 1
llist = LinkedList()
llist.head = Node(1)
e2 = Node(2)
e3 = Node(3)

# Link first Node to second node
llist.head.next = e2

# Link second Node to third node
e2.next = e3
print(llist.countt)
