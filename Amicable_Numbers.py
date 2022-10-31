a=int(input())
b=int(input())
pfsa=0
pfsb=0
for i in range(1,a):
    if a%i==0:
        pfsa+=i
for i in range(1,b):
    if b%i==0:
        pfsb+=i
if pfsa==b and pfsb==a:
    print("Amicable")
else:
    print("Not Amicable")
    
               