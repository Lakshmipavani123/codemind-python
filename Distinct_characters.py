n=input()
s=list(n.lower())
l=[]
for i in s:
    if i not in l and i!=" ":
        l.append(i)
d=sorted(l)
print("".join(d))