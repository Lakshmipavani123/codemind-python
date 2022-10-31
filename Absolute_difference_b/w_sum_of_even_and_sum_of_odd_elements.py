n=int(input())
a=map(int,input().split())
os=0
es=0
for i in a:
    if i%2!=0:
        os+=i
    else:
        es+=i
if os>es:
    print(os-es)
else:
    print(es-os)