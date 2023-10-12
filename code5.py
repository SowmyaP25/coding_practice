n = int(input('Enter a 4 digit number: '))
m = n
rev = 0
while(n>0):
    a = n%10
    rev = rev * 10 +a
    n = n//10
print(rev)
if(rev==m):
    print('The reverse is true')
else:
    print('The reverse is false')


