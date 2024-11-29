#Stack using arrays
class StackArr:
    def __init__(self):
        self.stack = []


    def push(self,val):
        self.stack.append(val)

    def isEmpty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.isEmpty():
            return  print("Stack is Empty")
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return print("Stack is Empty")
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    

# stack = StackArr()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# print(stack.peek())
# print(stack.isEmpty())
# print(stack.size())
# stack.pop()
# print(stack.size())




#Stack using Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    
class StackLL:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,val):
        new_node = Node(val)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        pop = self.head
        self.head = self.head.next
        self.size -= 1
        
        return pop.data
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.head.data

    def isEmpty(self):
        return self.size == 0
    
    def stackSize(self):
        return self.size
        


myStack = StackLL()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Pop: ", myStack.pop())
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())