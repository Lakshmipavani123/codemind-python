n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[]
for i in l:
    if i<a or i>b:
        l1.append(i)
#print(l1)
if len(l1)==0:
    print("-1")
else:
    print(min(l1))