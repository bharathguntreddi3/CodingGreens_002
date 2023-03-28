def levelOrder(root):
    l=[]
    l.append(root)
    while l!=[]:
        x=l.pop(0)
        print(x.info,end=' ')
        if x.left:l.append(x.left)
        if x.right:l.append(x.right)
