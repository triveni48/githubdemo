class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class sll:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
            print("None")

    def insert_at_begining(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_at_ending(self, data):
        ne = Node(data)
        if self.head is None:
            self.head = ne
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = ne

# Create linked list
L = sll()

# Create nodes and manually link them
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n1.next = n2
n2.next = n3
n3.next = n4

# Set up initial chain
L.head = n1

# Insert at beginning and end
L.insert_at_begining(2)
L.insert_at_ending(38)

# Display the linked list
L.display()
