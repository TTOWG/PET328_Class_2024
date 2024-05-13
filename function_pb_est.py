# TTOWG!

# A function to estimate bubble point pressure, pb
# Note: this function only works if solution gas-oil ratio at a pressure above bubble point (i.e. Rsi (=Rsb) is known)
# Note that temperature is in degree Fahreiheit
def bubble_pressure(temperature, pressure, gas_gravity, oil_gravity, rsb): 
    api = (141.5/oil_gravity)-131.5
    y = (0.00091*temperature)-(0.0125*api)
    pb = (18*(10**y))*((rsb/gas_gravity)**0.83)
    return round(pb,2)
