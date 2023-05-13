n=int(input())
l=list(map(int,input().split()))
c=0
ll=[]
for i in l:
    if l.count(i)==i:
        l.remove(i)
        c+=1
'''k=[]
for i in ll:
    if i not in ll:
        k.append(i)'''
print(c)