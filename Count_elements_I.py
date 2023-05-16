
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
for i in b:
    if i in a:
        if i not in l:
            l.append(i)
print(len(l))


