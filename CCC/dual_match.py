T = int(input())
A = list(map(int, input().split()))
k = int(input())
ans = 0
A.sort() 
def dm(x):
    l, h=0, T-1
    while l < h:
        mid = (l + h) // 2
        if A[mid] < x:
            l = mid + 1
        else:
            h = mid
    if A[l] >= x:
        return l
    else:
        return T

for i in range(T):
    j = dm(k - A[i])
    if j < T and A[j] == k - A[i]:
        ans += 1
print(ans)
