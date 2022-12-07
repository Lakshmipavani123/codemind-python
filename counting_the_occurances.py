n=input()
s=input()
c=0
for j in n:
    if j==s:
        c+=1
    if s not in n:
        print('-1')
        break
if c>0:
    print(c)