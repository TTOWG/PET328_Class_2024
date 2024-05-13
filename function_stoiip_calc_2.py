# TTOWG!!!

########  A function to compute Stock Tank Oil Initially In-Place (STOIIP), N ########
### This function accepts a single argument; being a
### a dictionary
def stoiip_2(data):
    N = (7758*data['area']*data['thickness']*data['poro']*(1-data['swi']))/data['boi']
    return round(N, 2)

# Sample call
# Uncomment the following lines to run them
#data_dict = {'area': 40, 'thickness': 15, 'poro': 0.28, 'swi': 0.3, 'boi': 1.2}
#print(stoiip_2(data_dict))

