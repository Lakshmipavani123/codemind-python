n=input()
s=list(n.lower())
l=[]
for i in s:
    f=s.count(i)
    if f==1:
        l.append(i)
if len(l)>0:
    print(l[0])
else:
    print('-1')
    