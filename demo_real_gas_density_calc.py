#...TTOWG!

# Real gas density function definition
# Note: pressure must be in psia and temperature in degree Rankine

def gas_density(gravity, pressure = 14.7, temperature = 520, z = 1):
    density = (2.70*pressure*gravity)/(z*temperature)
    return round(density,4)
