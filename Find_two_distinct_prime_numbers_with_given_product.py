def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
l=[]
c=0
for i in range(n+1):
    if prime(i):
        l.append(i)
for i in range(len(l)):
    for j in range(i):
        if l[i]*l[j]==n:
            print(l[j],l[i])
            c=1
            break
if c==0:
    print("-1")
#print("-1")