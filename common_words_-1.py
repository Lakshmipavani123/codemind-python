s1=input()
s2=input()
a=s1.lower()
b=s2.lower()
m1=a.split()
m2=b.split()
c=0
for i in m1:
    for j in m2:
        if i==j:
            c+=1
print(c)