def sumdig(n):
    c=0
    while n:
        r=n%10
        c=c+r
        n=n//10
    return c
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    s=sumdig(i)
    c+=s
print(c)