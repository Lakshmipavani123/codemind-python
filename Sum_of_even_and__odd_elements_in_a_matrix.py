r,c=map(int,input().split())
mat=[]
for i in range(r):
    b=list(map(int,input().split()))
    mat.append(b)
e=0
o=0
for i in range(r):
    for j in range(c):
        if (mat[i][j])%2==0:
            e+=mat[i][j]
        else:
            o+=mat[i][j]
print(e,o,end="")