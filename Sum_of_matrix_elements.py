def rowsum(d,r,c):
    res=[0 for i in range(r)]#it creates an array with zeros if r=3-->[0,0,0]
    for i in range(r):#index r=3-->0 1 2
        for j in range(c):#c=4-->0 1 2 3 
            res[i]+=d[i][j]  
    return res                  
r=int(input())
c=int(input())
row=[1 for i in range(c)]
d=[row.copy() for i in range(r)]
for i in range(r):
    vals=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=vals[j]
res=rowsum(d,r,c)
ss=0
for i in res:
    ss+=i    
print(ss)#*res)