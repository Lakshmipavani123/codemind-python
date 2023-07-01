
def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
m=list(map(int,input().split()))
a=min(m)
b=max(m)
c=0
i1=m.index(a)
i2=m.index(b)
if i1<i2:
    for i in range(i1,i2+1):
        if prime(m[i]):
            c+=1
elif i1>=i2:
    for i in range(i2,i1+1):
        if prime(m[i]):
            c+=1
print(c)

