n=input()
d=n.split()
maxs=0
mins=0
for i in d:
    mins+=ord(min(i))
    maxs+=ord(max(i))
print(maxs-mins)
