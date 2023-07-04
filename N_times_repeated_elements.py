n=int(input())
l=list(map(int,input().split()))
k=int(input())
f=0
c=[]
for i in range(len(l)):
    if l.count(l[i])==k:
        c.append(l[i])
        f=1
if f==1:
    print(*(set(c)))
else:
    print("-1")
