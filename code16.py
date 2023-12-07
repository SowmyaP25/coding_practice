# temp = int(input("Enter the values for temperature:"))
# humid = int(input("Enter the value for humidity:"))
def temp_humid(temp,humid):
    if(temp>= 30 and humid>=90):
        a ='Hot and Humid'
        return a
    elif (temp >= 30 and humid < 90):
        b = 'Hot'
        return b
    elif(temp<30 and humid>= 90):
        c = 'Cool and Humid'
        return c
    elif(temp<30 and humid<90):
        d = ('Cool')
        return d

x=temp_humid(23,89)
print(x)

