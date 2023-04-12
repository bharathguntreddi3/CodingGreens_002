T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    b = 0
    tr = 0
    for i in range(N):
        tr += A[i]
        strt = (tr*100)/(i+1)
        if strt == 100:
            b += 1
    print(b)