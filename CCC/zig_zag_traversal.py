def ZigZag(root):
    s1,s2 = []
    s1.append(root)
    while s1!=[] or s2!=[]:
        while s1!=[]:
            x = s1.pop()
            print(x.data,end=' ')
            if x.left:
                s2.append(x.left)
            elif x.right:
                s2.append(x.right)
        while s2!=[]:
            x = s2.pop()
            print(x.data, end=' ')
            if x.right:
                s1.append(x.right)
            elif x.left:
                s1.append(x.left)