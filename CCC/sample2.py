# given 2 arrays median of the combined array using binary search

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
total = n+m
if n>m:
    a,b = b,a
half = total//2
l, h = 0, len(a)-1
while True:
    m = (l+h)//2
    x = half-m-2
    al = a[m] if m>=0 else float("-inf")
    ar = a[m+1] if m+1<len(a)-1 else float("+inf")
    bl = b[x] if x>=0 else float("-inf")
    br = b[x+1] if x+1<len(b) else float("+inf")
    if al<=br and bl<=ar:
        if total%2==0:
            print((max(al+bl)+min(ar+br))//2)
        else:
            print(min(ar,br))
            exit()
    elif al>br:
        h=m-1
    else:
        l=m+1