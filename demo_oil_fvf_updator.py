#...TTOWG!

# input statements
p = float(input('What is the value of reservoir initial pressure?'))
pb = float(input('What is the value of reservoir bubble-point pressure?'))
bob = float(input('What is the value of oil FVF at bubble-point pressure?'))
co = float(input('What is the value of oil compressibility?'))
pressure_step = float(input('By how much should pressure be decremented?'))

# importing needed library
import math

while p > pb:
    bo = bob*(math.exp(co*(pb-p)))
    print('The value of oil FVF at {0:.2f} psi is {1:.4f} RB/STB'.format(p, bo))
    p = p - pressure_step   

# continuing after the 'while' block
print('Bubble-point pressure reached! End of simulation')
 
