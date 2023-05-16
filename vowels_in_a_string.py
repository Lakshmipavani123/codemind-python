str=input()
s=input()
vo='AEIOUaeiou'
for i in str:
    if i==s and i in vo:
        print('True')
        print(str.index(i))
        break
else:
    print("False")