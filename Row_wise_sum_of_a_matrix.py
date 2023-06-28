r,c=map(int,input().split())
mat=[]
for i in range(r):
    b=list(map(int,input().split()))
    mat.append(b)
s=[]
for i in range(r):
    s.append(sum(mat[i]))
print(*s)