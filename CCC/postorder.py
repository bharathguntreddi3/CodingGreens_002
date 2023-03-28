# def postorder(ino,pre):
#     ri=ino.find(pre[0])
#     if ri!=0: postorder(ino[:ri],pre[1:ri+1])
#     if ri!=len(ino)-1: postorder(ino[ri+1:],pre[ri+1:])
#     print(ino[ri],end='')
# inor=input()
# pre=input()
# postorder(inor,pre)

def twosum(nums, target):
    count =0
    l=[]
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                count=count+1
    return count,l
a=int(input())
b=list(map(int,input().split()))
c=int(input())   
b=sorted(b,key=int)
print(twosum(b,c))