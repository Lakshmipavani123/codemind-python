n=int(input())
a=list(map(int,input().split()))
os=0
es=0
for i in range(n):
    if i%2!=0:
        os+=a[i]
    else:
        es+=a[i]
if es>os:
    print(es-os)
else:
    print(os-es)

    