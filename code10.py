cp = int(input('Enter cost price: '))
sp = int(input('Enter Selling price: '))
if(sp>cp):
    print('Profit')
elif(sp<cp):
    print('Loss')
else:
    print('No Profit No Loss')