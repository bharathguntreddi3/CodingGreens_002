# import operator
# T = int(input())
# A = []
# for i in range(T):
#     n, s = input().split()
#     s = int(s)
#     A.append([n, s])
# A.sort(key=operator.itemgetter(1,0))
# for i in A:
#     print(*i)

T = int(input())
A = []
for i in range(T):
    n, s = input().split()
    A.append((n, int(s)))

A.sort(key=lambda x: (x[1], x[0]))
for i in A:
    print(i[0], i[1])
