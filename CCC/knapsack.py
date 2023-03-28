n, m = map(int, input().split())
knap = []
for i in range(n):
    p, w = map(int, input().split())
    r=p/w
    knap.append([r, p, w])
knap.sort(reverse=True)
p=0.0
i=0
while i<n and knap[i][2]<=m:
    p += knap[i][1]
    m -= knap[i][2]
    i+=1
if i<n and m>0:
    p+=m*knap[i][0]
print(p)

# O(nlogn)