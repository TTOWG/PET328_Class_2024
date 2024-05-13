#...TTOWG!
 
def stoiip_discretized(Lx, Ly, h, nx, ny, boi, poro_list, swi_list):
    
    # discretizing the reservoir
    delta_x = Lx/nx
    delta_y = Ly/ny

    # calculating the area per block
    area = delta_x*delta_y

    # initializing output variables
    total_stoiip = 0
    stoiip_list =[]
    
    # the 'for' loop
    for j in range(1,ny+1):
        for i in range(1,nx+1):
            block_n_order = (nx*(j-1))+i
            poro = poro_list[(block_n_order - 1)] 
            sw = swi_list[(block_n_order - 1)]  
            block_stoiip = (7758*area*h*poro*(1-sw))/boi
            stoiip_list.append(block_stoiip)  
            total_stoiip = total_stoiip + block_stoiip
    return total_stoiip, stoiip_list

