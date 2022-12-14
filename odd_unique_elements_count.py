n=int(input())
a=list(map(int,input().split()))
lst=[]
for i in a:
    if i not in lst:
        if i%2!=0:
            lst.append(i)
print(len(lst))