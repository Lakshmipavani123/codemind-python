n=input()
d=n.split()
maxs=0
mins=0
for i in d:
    print(ord(max(i))-ord(min(i)),end=" ")
    