# Implementation using classes

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        


class Bst:
    def __init__(self):
        self.root=None
        
    def insert(self,val):
        if not self.root:
            self.root=Node(val)
        else:
            self.insert_rec(self.root,val)                                                     
            
    def insert_rec(self,node,val):
        if val<node.data:
            if node.left is None:
                node.left=Node(val)
            else:
                self.insert_rec(node.left,val)
        else:
            if node.data==val:
                return
            if node.right is None:
                node.right=Node(val)
            else:
                self.insert_rec(node.right,val)
                
    def contains(self,val):
        return self.contains_rc(self.root,val)
    
    def contains_rc(self,node,val):
        if not node:
            return False
        if val==node.data:
            return True
        elif val<node.data:
            return self.contains_rc(node.left,val)
        elif val>node.data:
            return self.contains_rc(node.right,val) 
    
    def minvalnode(self,node):
        curr=node
        while curr.left is not None:
            curr=curr.left
        return curr
        
    def delete(self,val):
        self.root=self.delete_rc(self.root,val)
        
    def delete_rc(self,node,val):
        if node is None:
            return None
        if val<node.data:
            node.left=self.delete_rc(node.left,val)
        elif val>node.data:
            node.right=self.delete_rc(node.right,val)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            minnode=self.minvalnode(node.right)
            node.data=minnode.data
            node.right=self.delete_rc(node.right,minnode.data)
        return node
    
    def findclosest(self,target):
        return self.findclosest_rc(self.root,target)
    
    def findclosest_rc(self, node, target, closest=None):
        if node is None:
            return closest
        if closest is None:
            closest = node.data
        if abs(target - closest) > abs(target - node.data):
            closest = node.data
        if target < node.data:
            return self.findclosest_rc(node.left, target, closest)
        elif target > node.data:
            return self.findclosest_rc(node.right, target, closest)
        else:
            return closest
        
    def is_bst(self):
        return self.is_bst_rc(self.root,float('-inf'),float('inf'))
    
    def is_bst_rc(self,node,left,right):
        if node is None:
            return True
        if not (left<node.data<right):  
            return False
        return (self.is_bst_rc(node.left,left,node.data)) and (self.is_bst_rc(node.right,node.data,right))
    
    def inorder(self):
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        if node is not None:
            self._inorder_recursive(node.left, values)
            values.append(node.data)
            self._inorder_recursive(node.right, values)
            
    def preorder(self):
        values=[]
        self.preorder_rc(self.root,values)
        return values
    
    def preorder_rc(self,node,values):
        if node is not None:
            values.append(node.data)
            self.preorder_rc(node.left,values)
            self.preorder_rc(node.right,values)
        
            
    def postorder(self):
        values=[]
        self.postorder_rc(self.root,values)
        return values
        
    def postorder_rc(self,node,values):
        if node is not None:
            self.postorder_rc(node.left,values)
            self.postorder_rc(node.right,values)
            values.append(node.data)


    def sumofnodes(self):
        return self.sum_rc(self.root)  
    
    def sum_rc(self,node):
        if node is None:
            return 0
        return (node.data + self.sum_rc(node.left) + self.sum_rc(node.right))
    
    
    def count(self):
        return self.count_rc(self.root)
    
    def count_rc(self,node):
        if node is None:
            return 0
        return (1+self.count_rc(node.left)+self.count_rc(node.right))        
        
        
    def countofleaf(self):
        return self.cntofleaf(self.root)
    
    def cntofleaf(self,node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return (self.cntofleaf(node.left)+self.cntofleaf(node.right))  
    
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)

    def find_kth_largest(self,k):
        self.k = k
        self.cnt = 0
        self.result = None
        self._reverse_inorder(self.root)
        return self.result

    def _reverse_inorder(self,node):
        if node is None or self.cnt>=self.k:
            return
        self._reverse_inorder(node.right)
        self.cnt += 1

        if self.cnt == self.k:
            self.result = node.data     
            return
        
        self._reverse_inorder(node.left)
        
            
            
bst=Bst()
bst.insert(99)
bst.insert(34)
bst.insert(34)
bst.insert(15)
bst.insert(25)
bst.insert(17)
bst.insert(17)
bst.insert(98)
bst.delete(15)
print(bst.minvalnode(bst.root).data)
print(bst.findclosest(16))
print(bst.is_bst())
print(bst.inorder())
print(bst.preorder())
print(bst.postorder())
print(bst.sumofnodes())
print(bst.count())
print(bst.countofleaf())
print(bst.height())
print(bst.find_kth_largest(3))

            
            
        
 