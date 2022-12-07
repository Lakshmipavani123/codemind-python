n=input()
m=list(n)
c=0
d=0
for i in m:
    if i=='z':
        c+=1
    elif i=='o':
        d+=1
if c*2==d:
    print('Yes')
else:
    print('No')
        