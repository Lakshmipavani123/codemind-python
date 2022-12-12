def pr(b):
    if b==1:
        return False
    for i in range(2,int(pow(b,0.5))+1):
        if b%i==0:
            return False
    return True
def rev(m):
    d=0
    while m>0:
        r=m%10
        d=d*10+r
        m=m//10
    return d
n=int(input())
c=0
m=rev(n)
if pr(n):
    c=1
    if pr(m):
        c=2
if c==1:
    print('prime but not a circular prime')
elif c==2:
    print('circular prime')
else:
    print('not prime')

    