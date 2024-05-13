#...TTOWG!

# function definition
def stoiip_calc(area, thickness, poro, sw, boi):
    STOIIP = (7758*area*thickness*poro*(1-sw))/boi
    return STOIIP

# function call for Reservoir TTOWG_1 (re-use)
oil_inplace_TTOWG_1 = stoiip_calc(40, 15, 0.3, 0.28, 1.2)       # positional argument specification
print('The amount of oil in place in Reservoir TTOWG_1 is', oil_inplace_TTOWG_1, 'STB')


# function call for Reservoir TTOWG_2 (re-use)
oil_inplace_TTOWG_2 = stoiip_calc(80, 10, 0.23, 0.35, 1.1)
print('The amount of oil in place in Reservoir TTOWG_2 is {0:.2f} STB'.format(oil_inplace_TTOWG_2))

drainage_area = 40
payzone_thickness = 15

# function call
print(stoiip_calc(drainage_area, payzone_thickness, 0.3, 0.28, 1.2)) # positional argument specification


# function call with keyworded argument specification (ordered)
print(stoiip_calc(area = 40, thickness = 15, poro = 0.3, sw = 0.28, boi = 1.2)) # positional argument specification


# function call with keyworded argument specification (unordered)
print(stoiip_calc(poro = 0.3, area = 40, boi = 1.2, thickness = 15, sw = 0.28)) # positional argument specification

# function call with mixed argument specification
print(stoiip_calc(poro = 0.3, area = 40, boi = 1.2, thickness = 15, sw = 0.28)) # positional argument specification

stoiip_calc(40, 15, 0.3, 0.28, 1.2)

# Another function definition
def stoiip_calc2(area, thickness, poro, sw, boi):
    BV = area*thickness
    PV = BV*poro
    STOIIP = (7758*PV*(1-sw))/boi
    return PV, STOIIP # returning multiple values




