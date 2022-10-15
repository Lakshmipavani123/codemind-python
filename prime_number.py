def is_prime(n):
    if n>1:
        for x in range (2,n-1):
            if n%x==0:
                return 'not a prime'
                break
        else:
            return 'prime'
    elif n==1:
        return 'neither prime nor compodite'
    else:
        return'not a prime'
for y in range(5):
    r=int(input())
    result=is_prime(r)
    print(result)

    
