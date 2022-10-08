x,y,z=map(int,input().split())
s=(x+y+z)/2
area=(s*(s-x)*(s-y)*(s-z))**0.5
res="{:.2f}".format(area)
print(res)