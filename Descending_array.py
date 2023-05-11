n=int(input())
l=list(map(int,input().split()))
m=sorted(l,reverse = True)
if m==l:
    print("yes")
else:
    print("no")
