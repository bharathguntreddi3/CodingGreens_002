T = int(input())
A = list(map(int, input().split()))
A.sort()
for i in range(0,T,2):
    if i+1<T:
        print(A[i+1], end=' ')
    print(A[i], end=' ')