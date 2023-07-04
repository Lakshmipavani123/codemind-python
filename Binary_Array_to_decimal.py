n=int(input())
l=list(map(int,input().split()))
f=l[::-1]
s=0
for i in range(n):
    s+=(2**i)*(f[i])
print(s)
