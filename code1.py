a =int(input('Enter a value: '))
b =int(input('Enter b value: '))
c =int(input('Enter c value: '))
if(a>b and a>c):
    print('A is oldest')
elif(b>a and b>c):
    print('B is oldest')
else:
    print('C is oldest')