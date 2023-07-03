n=input().split(" ")
for i in range(len(n)):
    n[i]=n[i].lower()
s=''
for i in n:
    s=s+i
x=0
for i in s:
    if(s.count(i)==1):
        x=x+1
print(x)