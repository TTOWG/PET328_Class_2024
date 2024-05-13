#...TTOWG!

initial_pressure = input('Enter the value of initial pressure: ')
bubble_pressure = input('Enter the value of bubble-point pressure: ')

initial_pressure = float(initial_pressure)
bubble_pressure = float(bubble_pressure)

if initial_pressure > bubble_pressure:
    print('The reservoir is undersaturated!!!')
else:
    print('The reservoir is saturated!!!')
