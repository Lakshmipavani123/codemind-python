s=input()
d=0
for c in s:
    if (c.isdigit()):
        d+=1
if d>=1:
    print('Contains',d,'digit')
else:
    print("Doesn't contain digit")