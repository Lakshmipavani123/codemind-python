n=int(input())
a=map(int,input().split())
s=int(input())
for i in a:
    if i==s:
        print('True')
        break
else:
    print('False')