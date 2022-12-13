n=int(input())
m=list(map(int,input().split()))
c=0
for i in m:
    if i%2==0:
        break
    else:
        c+=i
print(c)