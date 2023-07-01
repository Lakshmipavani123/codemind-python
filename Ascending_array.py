n=int(input())
l=list(map(int,input().split()))
s=len(l)-1
c=0
for i in range(len(l)-1):
    if l[i+1]>l[i]:
        c+=1
if c==s:
    print("yes")
else:
    print("no")