def merge(a,low,mid,high):
    b=[]
    i,j=low,mid+1 
    while i<=mid and j<=high:
        if a[i]<=a[j]: b.append(a[i]);i+=1 
        else:b.append(a[j]);j+=1 
    while i<=mid : b.append(a[i]);i+=1 
    while j<=high: b.append(a[j]);j+=1 
    j=low
    for i in b:
        a[j]=i;j+=1
def mergesort(a,low,high):
    if low<high:
        mid=(low+high)//2 
        mergesort(a,low,mid)
        mergesort(a,mid+1,high)
        merge(a,low,mid,high)

n=int(input())
a=list(map(int,input().split()))
mergesort(a,0,n-1)
print(*a)


# -----------------------------------------------------------------------------------

# find number of inversions
def merge(a,low,mid,high):
    b=[]
    c=0
    i,j=low,mid 
    while i<mid and j<=high:
        if a[i]<=a[j]: b.append(a[i]);i+=1 
        else:
            c+=(mid-i)
            b.append(a[j]);j+=1 
    while i<mid : b.append(a[i]);i+=1 
    while j<=high: b.append(a[j]);j+=1 
    j=low
    for i in b:
        a[j]=i;j+=1
    return c
def mergesort(a,low,high):
    c=0
    if low<high:
        mid=(low+high)//2 
        c+=mergesort(a,low,mid)
        c+=mergesort(a,mid+1,high)
        c+=merge(a,low,mid+1,high)
    return c

n=int(input())
a=list(map(int,input().split()))
x=mergesort(a,0,n-1)
print(x)
