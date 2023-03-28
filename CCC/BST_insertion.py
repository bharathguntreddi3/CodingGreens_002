class node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 
def insert(root,val):
    nn=node(val) 
    if root==None: root=nn 
    else:
        t=root
        while True:
            if t.data>=val:
                if t.left==None:
                    t.left=nn 
                    break 
                t=t.left 
            else:
                if t.right==None:
                    t.right=nn 
                    break 
                t=t.right  
    return root
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
