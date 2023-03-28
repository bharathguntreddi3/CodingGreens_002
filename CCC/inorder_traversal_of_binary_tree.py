def inorder(a,i):
    if i<len(a) and a[i]!=0:
        inorder(a,2*i+1)
        print(a[i], end=' ')
        inorder(a,2*i+2)
n = int(input())
a = list(map(int, input().split()))
inorder(a,0)
