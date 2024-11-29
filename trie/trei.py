# class TrieNode:
#     def __init__(self):
#         self.children={}
#         self.is_leaf=False
        


# class Trie:
#     def __init__(self):
#         self.root=TrieNode()
        
#     def insert(self,word):
#         node=self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char]=TrieNode()
#             # print(node.children[char])
#             node=node.children[char]
            
#         node.is_leaf=True
    
#     def search(self,word):
#         node=self.root
#         for char in word:
#             if char not in node.children:
#                 return False
#             node=node.children[char]
            
#         return node.is_leaf    
    
#     def startwith(self,prefix): 
#         node=self.root
#         for char in prefix:
#             if char not in node.children:
#                 return False
#             node=node.children[char]
#         return True
    
#     def print_st(self,prefix):
#         node=self.root
#         for char in prefix:
#             if char not in node.children:
#                 return False
#             node=node.children[char]
#         self.print_st_hr(node,prefix)
        
#     def print_st_hr(self,node,word):
#         if node.is_leaf:
#             print(word)
#         for char,child in node.children.items():
#             self.print_st_hr(child,word+char)

            
    
    
        
# tr=Trie()
# tr.insert("helllo")
# tr.insert("hellli")
# tr.insert("helllu") 
# print(tr.root.children)
# print(tr.search("helllo"))
# print(tr.search("helllu"))
# print(tr.startwith("helllu"))
# tr.print_st("hell")




print("Hi i am sreya")