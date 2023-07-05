n1=input()
n=n1.lower()
m=n.split()
c=0
for i in m:
    k=list(i)
    if k[0] in 'aeiou':
        if k[-1] in 'bcdfghjklmnpqrstvwxyz':
            c+=1
print(c)
        
