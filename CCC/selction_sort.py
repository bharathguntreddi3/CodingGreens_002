n = int(input())
a = list(map(int, input().split()))
for i in range(n-1):
    m_ind = i
    for j in range(i+1,n):
        if a[m_ind]>a[j]:
            m_ind = j
    a[i],a[m_ind] = a[m_ind],a[i]
print(*a)