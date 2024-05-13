#...TTOWG!

# input statements
poro = input('Enter the value of porosity: ')
area = input('Enter the value of area: ')
paythickness = input('Enter the value of pay zone thickness: ')

area = float(area)
paythickness = float(paythickness)

BV = area*paythickness

# output statement
print('The bulk volume of the reservoir is', BV, 'Acre-ft') 
