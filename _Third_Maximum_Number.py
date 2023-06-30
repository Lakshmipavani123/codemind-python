n=int(input())
m=list(map(int,input().split()))
m.sort()
m2=m[::-1]
m1=[]
for i in m2:
    if i not in m1:
        m1.append(i)
#print(m1)
#print(m1)
#print(len(m))
if len(m1)>=3:
    print(m1[2])
else:
    print(max(m1))
