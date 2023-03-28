from datetime import datetime
import operator
T = int(input())
dates = []
for i in range(T):
    dd, mm, yyyy = map(int, input().split())
    dates.append((dd,mm,yyyy))
dates.sort(key=lambda x:(x[2],x[1],x[0]))
for date in dates:
    print("{:02d}/{:02d}/{}".format(date[0],date[1],date[2]))