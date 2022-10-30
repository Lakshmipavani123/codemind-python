n=int(input())
l=len(str(n))
c=0
s=0
while n:
    d=n%10
    if d==0 or d==2 or d==4 or d==6 or d==8:
        c=c+1
    else:
        s=s+1
    n=n//10
if c==l:
    print("Even")
elif s==l:
    print("Odd")
else:
    print("Mixed")