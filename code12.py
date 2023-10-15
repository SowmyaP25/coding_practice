h = float(input('Enter height: '))
r = float(input('Enter radius: '))
volume = 3.14 * (r**2) * h
print("volume of the cylinder: ",volume)
cost = volume/1000 * 40
print('Cost is ','Rs',cost)