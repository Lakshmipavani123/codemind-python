n=input()
c=[]
f=0
for i in n:
    if n.count(i)==1:
        f=1
        c.append(n.index(i))
if f==1:
    print(c[0])
else:
    print("-1")
    