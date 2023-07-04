n=input()
k=list(n)
p="AEIOUaeiou"
l=[]
for i in k:
    if i in p:
        l.append(i)
s=[]
for i in l:
    if i not in s:
        s.append(i)
print(*s)