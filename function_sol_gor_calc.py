# TTOWG!

# A function to compute solution gas-oil ratio, Rs
# Note: temperature must be in degree Fahreiheit
def sol_gor(temperature, pressure, gas_gravity, oil_gravity, pb): # where pb is bubble point pressure.
    api = (141.5/oil_gravity)-131.5
    y = (0.00091*temperature)-(0.0125*api)
    if pressure<pb:
        rs = gas_gravity*(((pressure)/(18*(10**y)))**1.204)
        return round(rs,2)
    else:
        rsb = gas_gravity*(((pb)/(18*(10**y)))**1.204)
        return round(rsb,2)
