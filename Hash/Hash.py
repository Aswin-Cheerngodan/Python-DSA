#Hash Table with array seperate chaining
class Hash:
    def __init__(self,size):
        self.capacity = size
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def hash_func(self,key):
        key = str(key)
        total = 0
        for i in key:
            total += ord(i)
        return total%self.capacity
    
    def insert(self,key,value):
        index = self.hash_func(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key,value])
        self.size += 1

        if self.size > 0.7*self.capacity:
            self.resize()

    def get(self,key):
        index = self.hash_func(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]

        return None

    def remove(self,key):
        index = self.hash_func(key)
        for i,item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                self.size -= 1
                return True
        
        return False
    

    def display(self):
        for i,items in enumerate(self.table):
            print(f"Index{i}: {items}")

    
    def resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [[] for i in range(self.capacity)]
        self.size = 0
        for pair in old_table:
            for key,value in pair:
                self.insert(key,value)



# hash_table = Hash(3)

# hash_table.insert("apple", 100)
# hash_table.insert("banana", 200)
# hash_table.insert("grape", 300)

# hash_table.display()
# print("Value for 'apple':", hash_table.get("apple"))
# hash_table.remove("banana")
# print("After removing 'banana':")
# hash_table.display()


#Hash table with linked list seperate chaining
class Node:
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.next = None

class Hash_LL:
    def __init__(self,size):
        self.capacity = size
        self.size = 0
        self.table = [None]*size

    def __hash(self,key):
        key = str(key)
        total = 0
        for i in key:
            total += ord(i)
        return total%self.capacity

    def add(self,key,val):
        index = self.__hash(key)
        if not self.table[index]:
            self.table[index] = Node(key,val)
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.data = val
                    return
                if not current.next:
                    break
                current = current.next
            current.next = Node(key,val)
    
    def get(self,key):
        index = self.__hash(key)
        if not self.table[index]:
            return "Key is not found !"
        current = self.table[index]
        while current:
            if current.key == key:
                return current.data
            current = current.next
        return "Key is not found !"
    
    def display(self):
        for i,bucket in enumerate(self.table):
            print(f"bucket {i}",end=" ")
            current = bucket
            while current:
                print(f"[{current.key}:{current.data}] ->",end="")
                current = current.next
            print()

        
hash_ll = Hash_LL(10)
hash_ll.add('Broto',148600)
hash_ll.add('Bridgon',65000)
hash_ll.add('Luminar',80000)
print(hash_ll.get('Luminar'))
hash_ll.display()


