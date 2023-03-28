T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    # temp = 0
    for i in range(N-1):
        if(A[i]>A[i+1] and A[i]-A[i+1]==1):
            A[i],A[i+1] = A[i+1],A[i]
            # temp += 1
        if(A[i]>A[i+1] and A[i]-A[i+1]>1):
            # temp = 1
            print("No")
            break
    else:
        print("Yes")
        # if(temp==0):
        #     print("Yes")
        # else:
        #     print("No")