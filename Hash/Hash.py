#Hash Table with seperate chaining
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



hash_table = Hash(3)

hash_table.insert("apple", 100)
hash_table.insert("banana", 200)
hash_table.insert("grape", 300)

hash_table.display()
print("Value for 'apple':", hash_table.get("apple"))
hash_table.remove("banana")
print("After removing 'banana':")
hash_table.display()
