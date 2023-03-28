n=int(input())
l=[]
m=0
for i in range(n):
    p,d=map(int,input().split())
    m=max(m,d)
    l.append([p,d]) 
slot=[0]*(m+1)
l.sort(reverse=True)
for i in range(n):
    if slot[ l[i][1] ]==0: 
        slot[ l[i][1] ]=l[i][0]
    else:
        for j in range(l[i][1]-1,0,-1):
            if slot[j]==0:
                slot[j]= l[i][0]
                break 
print(sum(slot))
