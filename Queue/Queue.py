#Queue using arrays
class QueueArr:
    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        self.queue.append(val)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue.pop(0)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    


myQueue = QueueArr()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", myQueue.queue)
print("Dequeue: ", myQueue.dequeue())
print("Peek: ", myQueue.peek())
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())







#Queue using Linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def enqueue(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1

    def isEmpty(self):
        return self.length == 0

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.front.data
    
    def size(self):
        return self.length
    
    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print()




myQueue = QueueLL()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", end="")
myQueue.printQueue()
print("Dequeue: ", myQueue.dequeue())
print("Peek: ", myQueue.peek())
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())