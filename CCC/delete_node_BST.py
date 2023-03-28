class node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 
def insert(root,val):
    if root==None: return node(val)
    elif val<=root.data: root.left=insert(root.left,val)
    else: root.right=insert(root.right,val)
    return root
def findmax(root):
    while root.left:root=root.left 
    return root
def delete(root,val):
    if root==None: print('val in the tree'); return root
    elif val < root.data:root.left=delete(root.left,val)
    elif val > root.data:root.right=delete(root.right,val)
    else: 
        if root.left and root.right:
            x=findmax(root.left)
            root.data=x.data
            root.left=delete(root.left,x.data)
        else:
            if root.left==None:root=root.right
            else: root=root.left 
    return  root

def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)
n=int(input())
root=None 
for i in range(n):
    x=int(input())
    root=insert(root,x)
inorder(root)
