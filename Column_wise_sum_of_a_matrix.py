r,c=map(int,input().split())
m=[]
cs=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(c):
    c=0
    for j in range(r):
        c+=m[j][i]
    cs.append(c)
print(*cs)
