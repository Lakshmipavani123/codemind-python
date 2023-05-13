n=int(input())
l=list(map(int,input().split()))
c=0
s=0
ll=[]
for i in l:
    if l.count(i)==i:
        ll.append(i)
g=set(ll)
if len(g)>0:
    for i in g:
        c+=i
        s+=1
    f=c/s
    print("{:.2f}".format(f))
else:
    print("-1")