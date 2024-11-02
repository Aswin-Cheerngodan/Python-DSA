class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class CircularDLL:
    def __init__(self):
        self.head = None
        
        
    def printCSLL(self):
        if not self.head:
            print("List is empty")
            return
        curr = self.head
        
        while curr:
            print(curr.data,end="-->")
            curr = curr.next
            if curr == self.head:
                break
        print(curr.data)
        
        
    def insertAtEnd(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
            return
        
        tail = self.head.prev
        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.head
        self.head.prev = new_node
        
        
    def insertAtBeg(self,val):
        new_node = Node(val)
        
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
            return
        
        tail = self.head.prev
        self.head.prev = new_node
        new_node.next = self.head
        new_node.prev = tail
        tail.next = new_node
        self.head = new_node
        
        
    def delete_wkey(self,val):
        if not self.head:
            print("List is empty")
            return
        
        curr = self.head
        while curr:
            if curr.data == val:
                if curr.data == val and curr.next == self.head:
                    self.head = None
                elif curr == self.head:
                    tail = curr.prev
                    self.head = curr.next
                    self.head.prev = tail
                    tail.next = self.head
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                print("Node deleted")
                return
            curr = curr.next
        print("Node not found")
            
        
        

cdll = CircularDLL()

cdll.insertAtEnd(1)
cdll.insertAtEnd(2)
cdll.insertAtEnd(3)
cdll.insertAtEnd(4)
cdll.insertAtEnd(15)

cdll.insertAtBeg(12)

cdll.printCSLL()

cdll.delete_wkey(2)

            
        