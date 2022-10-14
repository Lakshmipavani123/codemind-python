T=int(input())
for i in range(T):
    n,a,b,k=map(int,input().split())
    x=(n//a and n//b)
    a=n//a
    b=n//b
    kl=(a+b-x)
    if(kl>=k):
        print("Win")
    else:
        print("Lose")