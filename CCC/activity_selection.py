n=int(input())
l=[]
for i in range(n):
    s,e=map(int,input().split())
    l.append([s,e])
l.sort(key=lambda x: x[1])
c=1;i=0
for j in range(1,n):
    if l[j][0]>=l[i][1]:
        c+=1 
        i=j 
print(c)
