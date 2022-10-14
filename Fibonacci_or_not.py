n=int(input())
s=0
m=1
for i in range(1,n+1):
    next=s+m
    if next==n:
        print("True")
        break
    s=m
    m=next
else:
    print("False")