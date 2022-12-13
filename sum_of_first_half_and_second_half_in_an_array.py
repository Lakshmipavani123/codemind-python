n=int(input())
m=list(map(int,input().split()))
k=len(m)
c=0
s=0
for i in range((k//2)):
    c+=m[i]
for j in range((k//2),k):
    s+=m[j]
print(c)
print(s)