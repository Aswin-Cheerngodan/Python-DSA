class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
        

class LinkedList:
    def __init__(self):
        self.head = None
        
    #Array to LinkedList    
    def arr_to_ll(self,arr):
        if not arr:
            return
        
        self.head = Node(arr[0])
        curr = self.head
        
        for i in arr[1:]:
            curr.next = Node(i)
            curr = curr.next
            
    #DisplayLL
    def display(self):
        curr = self.head
        while curr:
            print(curr.data,end=" --> ")
            curr = curr.next
        print(curr)
        
        
    # Operations with value given
        
    #Add Node at end
    def add_end(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        #Traversing
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    
    #Add Node at Beggining
    def add_begg(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
    #Delete with value
    





list1 = LinkedList()
list1.add_end(1)
list1.add_end(2)
list1.add_end(3)
list1.add_end(4)
list1.display()