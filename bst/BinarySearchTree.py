# Implementation using functions
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
def insert(root,value):
    if root is None:
        return Node(value)
    if root.data==value:
        return root
    if value<root.data:
        root.left=insert(root.left,value)
    elif value>root.data:
        root.right=insert(root.right,value)
    return root

def isempty(node):
    return node is None

def isleaf(node):
    if node:
        return node.left is None and node.right is None

def minvalnode(node):
    if node.left is None:
        return node
    else:
        return minvalnode(node.left)

def maxvalnode(node):
    if node.right is None:
        return node
    else:
        return maxvalnode(node.right)
    

def delete(root,node):
    if root is None:
        return root
    if node<root.data:
        root.left=delete(root.left,node)
    elif node>root.data:
        root.right=delete(root.right,node)
    else:
        print(root.data)
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        minval=minvalnode(root.right)
        root.data=minval.data
        root.right=delete(root.right,minval.data)
    return root
            
def contains(root,val):
    if root is None or root.data==val:
        return root is not None
    if val<root.data:
        return contains(root.left,val)
    return contains(root.right,val)
   
        

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")

def findclosest(root,val):
    closest=root.data
    while root:
        if abs(val-root.data) < abs(val-closest):
            closest=root.data
        if val<root.data:
            root=root.left
        elif val>root.data:
            root=root.right
        else:
            break
    return closest
            
def isBst(self, left=float('-inf'), right=float('inf')):
        if self is None:
            return True
        if not (left < self.data < right):
            return False
        return self.left.isBst(left, self.data) and self.right.isBst(self.data, right)
        
        
        
tr=Node(50)
a=[10,20,30,40,60,70,80,90]
for i in a:
    insert(tr,i)
    
inorder(tr)
print()
preorder(tr)
delete(tr,40)
print() 
postorder(tr)
print()
print(minvalnode(tr).data)
print(maxvalnode(tr).data)
print(contains(tr,90))
print(findclosest(tr,8))
print(isBst(tr))

        