def partition(a,low,high):
    p = a[high]
    i=low
    for j in range(low,high):
        if a[j]<=p:
            a[i],a[j] = a[j],a[i]
            i+=1
    a[high],a[i] = a[i],a[high]
def quick(a,low,high):
    if low<high:
        pi = partition(a,low,high)
        quick(a,low,pi-1)
        quick(a,pi+1,high)
n = int(input())
a = list(map(int, input().split()))
quick(a,0,n-1)
print(*a)

# ----------------------------------------------------------------------------

def partition(a,low,high):
    p=a[high]
    i=low
    for j in range(low,high):
        if a[j]<=p:
            a[i],a[j]=a[j],a[i]
            i+=1 
    a[high],a[i]=a[i],a[high]
    return i 
def quick(a,low,high):
    if low<high:
        pi=partition(a,low,high)
        quick(a,low,pi-1)
        quick(a,pi+1,high)

n=int(input())
a=list(map(int,input().split()))
quick(a,0,n-1)
print(*a)
