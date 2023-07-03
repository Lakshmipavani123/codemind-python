n=input()
s=n.replace(" ","")
s1=s.lower()
s12=list(s1)
l=[]
for i in s12:
    if s12.count(i)==1:
        l.append(i)
p=sorted(l)
print("".join(p))