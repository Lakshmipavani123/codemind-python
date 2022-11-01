n=int(input())
s=list(map(int,input().split()))
c=0
co=0
for i in s:
    c+=i
a=c/n
for i in s:
    if i<=a:
        co+=1
print(co)