n=int(input())
m=list(map(int,input().split()))
k=len(m)
c=0
for i in m:
    if i==0 or i==1:
        c+=1
if c==k:
    print('True')
else:
    print('False')