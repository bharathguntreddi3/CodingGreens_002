T = int(input())
A = list(map(int, input().split()))
X = A[-1]
j = 0
for i in range(T-1):
    if A[i]<=X:
        A[i],A[j] = A[j],A[i]
        j+=1
A[j],A[T-1] = A[T-1],A[j]
print(*A)