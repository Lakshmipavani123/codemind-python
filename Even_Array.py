n=int(input())
m=list(map(int,input().split()))
k=len(m)
c=0
for i in m:
    if i%2==0:
        c+=1
if k==c:
    print('True')
else:
    print('False')
        
    