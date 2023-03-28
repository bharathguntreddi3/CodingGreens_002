def partition(A,low,high):
    P = A[high]
    i= low
    for j in range(low, high):
        if A[j]<=P:
            A[i],A[j] = A[j],A[i]
            i += 1
    A[i],A[high] = A[high], A[i]
    return i
def quick(A,low,high):
    if low<high:
        piy = partition(A,low,high)
        print(piy)
        for i in range(low,high+1):
            print(A[i], end=' ')
        print()
        quick(A, low, piy-1)
        quick(A,piy+1,high)

T = int(input())
A = list(map(int, input().split()))
quick(A,0,T-1)