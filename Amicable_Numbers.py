m=int(input())
n=int(input())
s=0
p=0
for i in range(1,m):
    if m%i==0:
        s+=i
#print(s)
for i in range(1,n):
    if n%i==0:
        p+=i
#print(p)
if m==p and n==s:
    print("Amicable")
else:
    print("Not Amicable")
        
