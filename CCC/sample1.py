# find a triplet among n numbers where the sum of 2 numbers is equal to the 3rd element
def bs(a,k):
    l,h=0, len(a)-1
    while l<=h:
        m=(l+h)//2
        if a[m] == k:
            return 1
        elif a[m]<k:
            l = m+l
    return 0
n = int(input())
a = list(map(int, input().split()))
a.sort()
temp = 0
for i in range(n-1):
    for j in range(i+1,n-1):
        if bs(a,a[i]+a[j]):
            temp+=1
print(temp)

# ------------------------------------------------------------------

def bs(a,k):
    l,h=0,len(a)-1 
    while l<=h:
        m=(l+h)//2 
        if a[m]==k: return 1 
        elif a[m]<k:l=m+1 
        else:h=m-1 
    return 0
n=int(input())
a=list(map(int,input().split()))
a.sort() 
c=0
for i in range(n-1):
    for j in range(i+1,n-1):
        if bs(a,a[i]+a[j]): c+=1 
print(c)
