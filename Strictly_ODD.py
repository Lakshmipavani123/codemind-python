n=int(input())
l=list(map(int,input().split()))
s=len(l)
c=0
m=0
for i in range(s):
    if l[i]%2!=0:
        if i%2!=0:
            c=c+1
        m=m+1
if m==c:
    print("True")
else:
    print("False")


       