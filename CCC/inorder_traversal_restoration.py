def inorder(S,low,high):
    if low<=high:
        mid = (low+high)//2
        inorder(S,low,mid-1)
        print(end=S[high])
        inorder(S,mid,high-1)
S = input()
n = len(S)
inorder(S,0,n-1)    