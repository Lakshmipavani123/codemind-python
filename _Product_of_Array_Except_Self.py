def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result
n=int(input())
s=list(map(int,input().split()))
l=[]
for i in range(0,len(s)):
    k=multiplyList(s)
    l.append(int(k/s[i]))
print(*l)