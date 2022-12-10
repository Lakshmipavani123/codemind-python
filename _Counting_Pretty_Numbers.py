t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    c=0
    for i in range(n,m+1,1):
        a=i%10
        if a==2 or a==3 or a==9:
            c+=1
    print(c)
        