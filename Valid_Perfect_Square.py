t=int(input())
for i in range(t):
    n=int(input())
    for j in range(n):
        if j*j==n:
            print('True')
            break
    else:
        print("False")