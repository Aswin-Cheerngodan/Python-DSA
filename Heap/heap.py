class MinHeap:
    def __init__(self) -> None:
        self.heap=[]
        
    def build(self,arr):
        self.heap=arr
        for i in range(len(self.heap)//2-1,-1,-1):
            self.heapify(i)
    
    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
        return
            
    def heapify(self,i):
        small=i
        left=2*i+1
        right=2*i+2
        if left<len(self.heap) and self.heap[left]<self.heap[small]:
            small=left
        if right<len(self.heap) and self.heap[right]<self.heap[small]:
            small=right
        if small!=i:
            self.swap(small,i)
            self.heapify(small)

    def insert(self,val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)
    
    def heapify_up(self,i):
        while i>0:
            if self.heap[i]<self.heap[(i-1)//2]:
                self.swap(i,(i-1)//2)
            i=(i-1)//2
            
    def popmin(self):
        self.swap(0,len(self.heap)-1)
        value=self.heap.pop()
        self.heapify(0)
        return value
    
    
                   
a=[12,34,4212,3,45,65,7]            
hp=MinHeap()
hp.build(a)
hp.insert(11)
print(hp.heap)
hp.popmin()
print(hp.heap)





class MaxHeap():
    def __init__(self) -> None:
        self.heap=[]
        
    def build(self,arr):
        self.heap=arr
        for i in range(len(self.heap)//2-1,-1,-1):
            self.heapify(i)
    
    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
        return
            
    def heapify(self,i):
        large=i
        left=2*i+1
        right=2*i+2
        if left<len(self.heap) and self.heap[left]>self.heap[large]:
            large=left
        if right<len(self.heap) and self.heap[right]>self.heap[large]:
            large=right
        if large!=i:
            self.swap(large,i)
            self.heapify(large)
            
    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
        
    def heapify_up(self,i):
        while i>0:
            if self.heap[i]>self.heap[(i-1)//2]:
                self.swap(i,(i-1)//2)
            i=(i-1)//2
            
    def popmax(self):
        self.swap(0,len(self.heap)-1)
        val=self.heap.pop()
        self.heapify(0)
        return val
        
            
            



a=[1,2,3,4,5,6,7]
he=MaxHeap()
he.build(a)
print(he.heap)
he.insert(98)
print(he.heap)
print(he.popmax())
print(he.heap)