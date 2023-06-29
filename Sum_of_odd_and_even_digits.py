n=int(input())
s=list(map(int,input().split()))
o=0
e=0
for i in range(len(s)):
    if i%2!=0:
        o+=s[i]
    else:
        e+=s[i]
if o-e==0 or e-o==0:
    print("YES")
else:
    print("NO")
        