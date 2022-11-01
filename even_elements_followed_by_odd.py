n=int(input())
s=list(map(int,input().split()))
even=[]
odd=[]
for i in s:
       if i%2==0:
           even.append(i)
       else:
           odd.append(i)
for i in even:
    print(i,end=" ")
for i in odd:
    print(i,end=" ")