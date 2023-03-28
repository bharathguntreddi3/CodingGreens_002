n = int(input())
t1 = [[0,0] for i in range(n+1)]
t2 = [[0,0] for i in range(n+1)]
for i in range(n-1):
    x, y, c = input().split()
    x = int(x)
    y = int(y)
    if c=='L':
        t1[x][0] = y
    else:
        t1[x][1] = y
for i in range(n-1):
    x, y, c = input().split()
    x = int(x)
    y = int(y)
    if c=='L':
        t2[x][0] = y
    else:
        t2[x][1] = y
for i in range(1, n+1):
    if t1[i][0] != t2[i][1] or t1[i][1]!=t2[i][0]:
        print("no")
        break
else:
    print("yes")