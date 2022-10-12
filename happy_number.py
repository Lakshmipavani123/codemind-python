def happy(m):
    s=0
    while m:
        r=m%10
        m=m//10
        s=s+r*r
    return s
n=int(input())
x=happy(n)
while x>9:
    x=happy(x)
if x==7 or x==1:
    print("True")
else:
    print("False")