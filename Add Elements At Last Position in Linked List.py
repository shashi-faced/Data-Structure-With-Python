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
    def atlast(self,newdata):
        newnode = Node(newdata)
        newnode.next = None # ye line newnode ke next me none kar diya
        e3.next = newnode  # iss line me last node(mtlb e3 ka next =  new node)
        
llist = LinkedList()
llist.head = Node(1)
e2 = Node(2)
e3 = Node(3)

# Link first Node to second node
llist.head.next = e2

# Link second Node to third node
e2.next = e3
print("before adding new elements:")
llist.listprint()
n = int(input('enter number to add end in Linked List :: '))
llist.atlast(n)
llist.listprint()
