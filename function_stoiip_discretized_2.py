#...TTOWG!
 
def stoiip_discretized_2(Lx, Ly, h, nx, ny, boi, poro_list, swi_list):
    
    # discretizing the reservoir
    delta_x = Lx/nx
    delta_y = Ly/ny

    # calculating the area per block
    area = delta_x*delta_y

    # initializing output variables
    total_stoiip = 0
    stoiip_dict ={}
    
    # the 'for' loop
    for j in range(1,ny+1):
        for i in range(1,nx+1):
            block_n_order = (nx*(j-1))+i
            block_label = 'Block'+str(block_n_order) # to be used as key in stoiip_dict
            poro = poro_list[(block_n_order - 1)] 
            sw = swi_list[(block_n_order - 1)]  
            block_stoiip = (7758*area*h*poro*(1-sw))/boi
            stoiip_dict[block_label] = block_stoiip  
            total_stoiip = total_stoiip + block_stoiip
    return (total_stoiip, stoiip_dict)

# Sample call:
poro_vals = [0.18, 0.21, 0.32, 0.28]
swi_vals = [0.23, 0.25, 0.29, 0.31]
print(stoiip_discretized_2(100, 100, 15, 2, 2, 1.2, poro_vals , swi_vals))
