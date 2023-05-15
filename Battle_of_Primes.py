def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
m=int(input())
s=m+n
for i in range(1,20):
    if prime(s+i):
        print(i)
        break