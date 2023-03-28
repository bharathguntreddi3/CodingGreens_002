n, k = map(int, input().split())
price = list(map(int, input().split9))
price.sort(reverse=True)
sum =0
c = 1
j = 0
for i in range(n):
    sum += c*price[i]
    j+=1
    if j%k ==0:
        c+=1
print(sum)