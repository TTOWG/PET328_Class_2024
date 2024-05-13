########  A function to compute oil formation volume factor, Bo ########
# Note: temperature must be in degree Fahreiheit
# For pressures above or at bubble point, either pb or rs may be skipped; but not both.
# For pressures below bubble point, only rs may be skipped.
# co is required if pressure is above bubble point; otherwise, it must be skipped.

def fvf(pressure, temperature, gas_gravity, oil_gravity, pb = None, rs = None, co = None):
    
    # calling function bubble_pressure if neccessary (i.e. if pb is not specified)
    if pb is None:
        from function_pb_est import bubble_pressure
        pb = bubble_pressure(temperature, pressure, gas_gravity, oil_gravity, rs)

    # calling function sol_gor if neccessary (i.e. if rs is not specified)
    if rs is None:
        import function_sol_gor_calc
        rs = function_sol_gor_calc.sol_gor(temperature, pressure, gas_gravity, oil_gravity, pb)

    # calculating F parameter
    F = (rs*((gas_gravity/oil_gravity)**0.5))+(1.25*temperature)

    if pressure > pb:
        bob = 0.9759+(0.00012*(F**1.2)) # assuming gas_gravity and oil_gravity are constant for all pressures above pb
        # importing needed library
        import math
        bo = bob*(math.exp(co*(pb-pressure)))
    else:
        bo = 0.9759+(0.00012*(F**1.2))

    return round(bo, 4)
