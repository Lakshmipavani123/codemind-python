def palin(n):
    s=0
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    return s
n=int(input())
m=list(map(int,input().split()))
c=0
for i in m:
    if i==palin(i):
        c+=1
print(c)