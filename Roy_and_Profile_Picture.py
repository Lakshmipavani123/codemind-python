l=int(input())
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a<l or b<l:
        print("UPLOAD ANOTHER")
    else:
        if a==b:
            print("ACCEPTED")
        else:
            print("CROP IT")
    

