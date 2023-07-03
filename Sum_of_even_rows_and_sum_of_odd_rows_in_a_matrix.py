r,c=map(int,input().split())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
es=[]
os=[]
for i in range(r):
    if i%2==0:
        es.append(sum(m[i]))
    else:
        os.append(sum(m[i]))
print(sum(es),sum(os))
        