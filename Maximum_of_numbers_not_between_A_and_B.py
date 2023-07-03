a=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
flag=0
li=[]
for i in l:
    if i<a or i>b:
        flag=1
        li.append(i)
        d=max(li)
if flag==1:
    print(d)
else:
    print(-1)