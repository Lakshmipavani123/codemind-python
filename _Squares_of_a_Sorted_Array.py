n=int(input())
m=list(map(int,input().split()))
l=[]
for i in m:
    l.append(i*i)
l.sort()
print(*l)