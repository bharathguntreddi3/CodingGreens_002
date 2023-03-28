n = int(input())
a = list(map(int, input().split()))
p = int(input())
c = 0
num = 0
i = 0
a.sort(reverse=True)
while i<n and p>0:
    num = p//a[i]
    c+=num
    p = p-num*a[i]
    i+=1
if p!=0:
    print('no solution')
else:
    print(c)