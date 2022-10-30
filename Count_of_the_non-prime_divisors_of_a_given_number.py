def prime(n):
    if n==1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
a=int(input())
c=0
for j in range(1,a+1):
    if a%j==0 and prime(j)==0:
        c=c+1
print(c)