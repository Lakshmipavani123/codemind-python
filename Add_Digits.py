def add_dig(m):
    s=0
    while m:
        d=m%10
        s=s+d
        m=m//10
    return s
n=int(input())
a=add_dig(n)
while a>9:
    a=add_dig(a)
else:
    print(a)