t=int(input())
for i in range(t):
    a=int(input())
    fact=1
    while a:
        fact=fact*a
        a=a-1
    print(fact)