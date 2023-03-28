T = int(input())
A = list(map(int, input().split()))
for i in range(T-1):
    m_ind = i
    for j in range(i+1,T):
        if A[m_ind]>A[j]:
            m_ind = j
    A[i],A[m_ind] = A[m_ind],A[i]
print(*A)