n=int(input())
s=n*n
l=len(str(n))
num=s%(10**l)
if n==num:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
    