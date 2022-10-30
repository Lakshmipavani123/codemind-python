def reverse(m):
    rev=0
    while m:
        d=m%10
        rev=rev*10+d
        m=m//10
    return rev
a=int(input())
b=int(input())
for i in range(a,b):
    if i==reverse(i):
        print(i,end=" ")