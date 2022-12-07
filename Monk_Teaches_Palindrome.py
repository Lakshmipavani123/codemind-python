t=int(input())
for i in range(t):
    a=input()
    c=0
    bb=a[::-1]
    if a==bb:
        for j in a:
            c+=1
        if c%2==0:
            print('YES EVEN')
        else:
            print('YES ODD')
    else:
        print('NO')
    
   
    
    