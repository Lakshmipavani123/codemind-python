n=int(input())
s=list(map(int,input().split()))
l=[]
d=[]
for i in s:
    if i not in l:
        l.append(i)
    else:
        d.append(i)
print(*d)