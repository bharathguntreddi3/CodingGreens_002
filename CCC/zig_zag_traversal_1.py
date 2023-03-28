T = int(input())
l = [[0,0] for i in range(T+1)]
for i in range(T-1):
    x, y, c = input().split()
    x = int(x)
    y = int(y)
    if c == 'L':
        l[x][0]=y
    else:
        l[x][1] = y
s1 = [];s2 = []
s1.append(1)
while(s1!=[] or s2!=[]):
    while(s1!=[]):
        x = s1.pop()
        print(x,end=' ')
        if l[x][0]:
            s2.append(l[x][0])
        if l[x][1]:
            s2.append(l[x][1])
    while(s2!=[]):
        x = s2.pop()
        print(x,end=' ')
        if l[x][1]:
            s1.append(l[x][1])
        if l[x][0]:
            s1.append(l[x][0])