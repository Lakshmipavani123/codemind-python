n=int(input())
m=list(map(int,input().split()))
d=[]
for i in m:
    if i!=0:
        d.append(i)
while len(m)!=len(d):
    d.append(0)
print(*d)