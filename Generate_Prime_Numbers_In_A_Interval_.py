def pr(b):
    if b==1:
        return False
    for i in range(2,int(pow(b,0.5))+1):
        if b%i==0:
            return False
    return True
n=int(input())
m=int(input())
c=0
for i in range(n,m+1,1):
    if pr(i):
        print(i)

        
    