def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
l=[]
m=[]
for i in range(n):
    if prime(i):
        l.append(i)
for j in range(n,n+10):
    if prime(j):
        m.append(j)
t=m[0]
s=l[len(l)-1]
if (n-s)< (t-n):
    print(n-s)
else:
    print(t-n)
    