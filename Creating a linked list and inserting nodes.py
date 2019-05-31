class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        temp = self.head
        while temp is not None:
            print (temp.data)
            temp = temp.next

llist = LinkedList()
llist.head = Node(input("first element ::"))
e2 = Node(input('2nd elements :'))
e3 = Node(input('one more :'))

# Link first Node to second node
llist.head.next = e2

# Link second Node to third node
e2.next = e3

llist.listprint()
