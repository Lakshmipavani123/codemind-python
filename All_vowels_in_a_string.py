n=input()
l='aeiou'
l1='AEIOU'
c=''
d=''
for i in l:
    if i in n:
        c+=i
for i in l1:
    if i in n:
        d+=i
if c==l or d==l1:
    print("True")
else:
    print("False")