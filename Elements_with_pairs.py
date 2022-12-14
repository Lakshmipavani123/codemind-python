n=int(input())
a=list(map(int,input().split()))
if n%2!=0:
    for i in range(n+1):
        a.append(0)
        break
print(*a)
