def isprime(x):
    if x==1:
        return False
    for i in range(2,x):
        if(x%i==0):
            return False
    else:
        return True
n=int(input())
if(isprime(n)):
    while n:
        d=n%10
        n=n//10
        if not isprime(d):
            print("Not Mega Prime")
            break
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")