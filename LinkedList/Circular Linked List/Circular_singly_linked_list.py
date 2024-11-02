class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class CircularSLL:
    def __init__(self):
        self.head = None
    
        
    def PrintLL(self):
        if not self.head:
            return None
        curr = self.head
        while curr:
            print(curr.data,end="-->")
            curr = curr.next
            if curr == self.head:
                break
        print(curr.data)
    
    
    def insertAtBegin(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            return
        
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        
        curr.next = new_node
        new_node.next = self.head
        self.head = new_node
        
    def inserAtEnd(self,val):
        new_node = Node(val)
        pass
    
    
    
myCLL = CircularSLL()
myCLL.insertAtBegin(12)
myCLL.insertAtBegin(23)
myCLL.insertAtBegin(34)

myCLL.PrintLL()
        
        
        
    