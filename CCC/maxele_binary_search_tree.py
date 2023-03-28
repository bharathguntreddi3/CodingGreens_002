def maxele(root):
    if(root==NULL):return -1;
    r=root.data
    left=maxele(root.left)
    right=maxele(root.right)
    m=max(r,left,right)
    return m