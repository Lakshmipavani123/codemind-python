def pri(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in l:
    if pri(i):
        if i<=k:
            c+=1
print(c)