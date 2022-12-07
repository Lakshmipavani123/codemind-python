t=int(input())
for j in range(t):
    n=input()
    m=list(n)
    d=len(m)
    c=0
    for i in m:
        if i.isdigit():
            c+=1
    if c==d:
        print('True')
    else:
        print('False')