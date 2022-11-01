n=int(input())
s=list(map(int,input().split()))
e=0
od=0
for i in s:
    if i%2==0:
        e+=1
    else:
        od+=1
print(e,od)