def isprime(n):
    if n==1:
        return False
    for i in range(2,n):
            if (n%i==0):
                return False
    else:
        return True
n=int(input())
m=list(map(int,input().split()))
c=0
for i in m:
    if isprime(i):
        c+=1
print(c)