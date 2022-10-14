n=int(input())
if n>=3:
    for i in range(-n+1,n):
        if(i<=0):
            for j in range(n+i):
                print('*',end="")
        else:
            for j in range(n-i):
                print('*',end="")
        print()
else:
    print("The pattern is not possible")