def rever(n):
    c=0
    while n:
        r=n%10
        c=c*10+r
        n=n//10
    return c
n=int(input())
m=list(map(int,input().split()))
for i in m:
    d=rever(i)
    print(d,end=" ")
        