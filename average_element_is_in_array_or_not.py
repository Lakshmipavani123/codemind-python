n=int(input())
s=list(map(int,input().split()))
c=0
for i in s:
    c+=i
p=c//n
for i in s:
    if i==p:
        print("True")
        break
else:
    print("False")
    