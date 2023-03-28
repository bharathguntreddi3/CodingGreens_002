def tm(A,k):
    l=0
    h=len(A)-1
    while l<=h:
        m=(l+h)//2
        if A[m]==k:
            return 1
        elif A[m]>k:
                h=m-1
        else:
            l=m+1
    return 0
T = int(input())
A = list(map(int, input().split()))
m = int(input())
C = list(map(int, input().split()))
A.sort()
for i in C:
    if tm(A,i):
        print("Happy Halloween!")
    else:
        print("Tricky!")