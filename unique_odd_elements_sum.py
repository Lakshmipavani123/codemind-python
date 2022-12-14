n=int(input())
a=list(map(int,input().split()))
lst=[]
for i in a:
    if i not in lst and i%2:
        lst.append(i)
print(sum(lst))