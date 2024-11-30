#Hash Table with seperate chaining
class Hash:
    def __init__(self,size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_func(self,key):
        return hash(key)%self.size
    
    def insert(self,key,value):
        index = self.hash_func(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key,value])

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
                return True
        return False
    

    def display(self):
        for i,items in enumerate(self.table):
            print(f"Index{i}: {items}")



hash_table = Hash(10)

hash_table.insert("apple", 100)
hash_table.insert("banana", 200)
hash_table.insert("grape", 300)

hash_table.display()
print("Value for 'apple':", hash_table.get("apple"))
hash_table.remove("banana")
print("After removing 'banana':")
hash_table.display()
