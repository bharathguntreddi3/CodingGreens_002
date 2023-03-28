def bs(a,k):
    if a[-1]<k: return n 
    l,h=-1,len(a)-1
    while h-l>1:
        m=(l+h)//2
        if a[m]>=k: h=m 
        else: l=m 
    return h 
n=int(input())# size of the array or list
a=list(map(int,input().split()))#sorted list
k=int(input())# inserting key 
pos=bs(a,k)
print(pos)
