# A script to classify and count 'active' and 'inactive'
# gridblocks in a discretized reservoir

#################### Task 1 ############################
    #Request for reservoir dimensions and discretization parameters

#Lx
Lx = float(input('What is the Length of the reservoir in the x axis '))
# Ly
Ly = float(input('What is the Length of the reservoir in the y axis'))
# Lz
Lz = float(input('What is the Length of the reservoir in the z axis'))
# nx
nx = int(input('What is the number of gridblocks in x axis'))
# ny
ny = int(input('What is the number of gridblocks in y axis'))
# nz
nz = int(input('What is the number of gridblocks in z axis'))


#################### Task 2 ############################
    # Request for the cut-off value
# cut_off
cut_off= float(input('What is the value of cut_off'))

#################### Task 3 ############################
    # Initialize counters

# n_active
n_active = 0
# n_inactive
n_inactive = 0
#################### Task 4 ############################
    # Loop through all blocks (nested loop)          
for  k in range(1, nz+1):
    # Initialize layer counter
    n_active_layer =0
    # two nested loops go here
    for j in range(1, ny+1):
        for i in range(1, nx+1):
            perm = float(input("What is the permeability value?"))
            if perm < cut_off:
               category = 'inactive'
               n_inactive = n_inactive + 1
            else:
                category = 'active'
                n_active = n_active + 1
                n_active_layer = n_active_layer + 1
            
    # Print layer count
    print(n_active_layer)

#################### Task 5 ############################
# Print overall counts
all_blocks = n_active + n_inactive
n_active_percent = (n_active/all_blocks) * 100
round_n_active_percent = round(n_active_percent, 2)
print(f'The percentage of the active blocks in the entire reservoir is {round_n_active_percent}')
