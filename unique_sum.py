n=int(input())
m=list(map(int,input().split()))
k=set(m)
c=0
for i in k:
    c+=i
print(c)
    