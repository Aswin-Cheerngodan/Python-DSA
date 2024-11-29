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
    def del_value(self,val):
        if not self.head:
            return
        
        if self.head.data == val:
            self.head = self.head.next
            return
        
        curr = self.head
        while curr.next:
            if curr.next.data == val:
                curr.next = curr.next.next
                continue
            curr = curr.next

    #Nth Node from start
    def nth_start(self,n):
        if not self.head:
            return print("Linked list does not exists")
        cnt = 1
        curr = self.head
        while curr.next and cnt<n:
            curr = curr.next
            cnt += 1
        if cnt==n:
            print(curr.data)
        else:
            print(f"There is no {n} th node")

    # Nth node from end
    def nth_end(self,n):
        if not self.head:
            return
        
        curr1 = self.head
        curr2 = self.head

        for i in range(1,n):
            curr1 = curr1.next
            if curr1 is None:
                return print("No nth point from end")
            
        while curr1.next:
            curr1 = curr1.next
            curr2 = curr2.next
        print(curr2.data)

    # Middle of the linked list
    def middle(self):
        if not self.head:
            return print("Linked List does not exists")
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print(slow.data)

    #Count of value
    def count(self,val):
        if not self.head:
            return
        curr = self.head
        cnt = 0
        while curr:
            if curr.data == val:
                cnt += 1
            curr = curr.next
        return cnt

    #Reverse 
    def reverse(self):
        if not self.head:
            return print("Linked List does not exists")
        curr = self.head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node
        self.head = prev


list1 = LinkedList()
list1.add_end(1)
list1.add_end(2)
list1.add_end(3)
list1.add_end(4)
list1.add_end(4)
list1.display()
#Deleting all fours
# list1.del_value(4)
# list1.display()
list1.nth_start(4)
list1.nth_end(12)
list1.middle()
list1.count(3)
# list1.reverse()
# list1.display()