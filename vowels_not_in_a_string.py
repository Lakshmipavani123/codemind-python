n=input()
v='aeiou'
c=''
for i in v:
    if i not in n:
        c+=i
if len(c):
    for i in c:
        print(i,end=" ")
else:
    print("0")