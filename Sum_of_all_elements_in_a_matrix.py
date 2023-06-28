r,c=map(int,input().split())
mat=[]
for i in range(r):
    inner_list=list(map(int,input().split()))
    mat.append(inner_list)
s=0
#s=[]
for i in range(r):
    for j in range(c):
        s+=mat[i][j]#.append(mat[i][j])
print(s)#sum(s))