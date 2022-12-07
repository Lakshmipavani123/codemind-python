t=int(input())
for i in range(t):
    n=input()
    f=list(n)
    c=0
    for i in f:
        if i.isdigit():
            c+=1
    if c>0:
        print('Yes')
    else:
        print('No')
   