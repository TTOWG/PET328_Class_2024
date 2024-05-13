#...TTOWG!

# input statements
Lx = float(input('What is the length of the reservoir in x-direction?'))
Ly = float(input('What is the length of the reservoir in y-direction?'))
h = float(input('What is the thickness of the reservoir?'))
nx = int(input('How many blocks there are in x-axis?'))
ny = int(input('How many blocks there are in y-axis?'))
boi = float(input('What is the value of initial oil FVF?'))
           
# discretizing the reservoir

delta_x = Lx/nx
delta_y = Ly/ny

# calculating the area per block
area = delta_x*delta_y

# initializing output variable

total_stoiip = 0


# the 'for' loop
for j in range(1,ny+1):
    for i in range(1,nx+1):
        block_n_order = (nx*(j-1))+i
        poro = float(input('What is the value of porosity for Block {0}?'.format(block_n_order)))
        sw = float(input('What is the value of water saturation for Block {0}?'.format(block_n_order)))
        block_stoiip = (7758*area*h*poro*(1-sw))/boi
        total_stoiip = total_stoiip + block_stoiip
        print('The amount of oil in Block {0} is {1:.2f} STB'.format(block_n_order, block_stoiip))

# continuing after the 'for' loop
# displaying the results.
print('The amount of oil in the entire reservoir is {0:.2f} STB'.format(total_stoiip))                       
