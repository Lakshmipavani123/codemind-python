n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    s=arr1+arr2
    s.sort()
    print(*s)
    