######### Assignment 2  ##################

# The purpose of this assignment is to assess your 
# understanding of the principle of sequential execution.

# In this script, some statements are placed in the wrong lines.
# Identify the statements; copy and paste them in the right lines.
# Run the file to be sure it is working.

# Receiving input parameters
poro = input("What is the reservoir porosity")
area = input("What is the acreage of the reservoir")
h = input("What is the thickness of the reservoir")
sw = input("What is the water saturation of the reservoir")
boi = input("What is formation volume factor of the reservoir fluid")

# Calculating STOIIP
N = (7758*area*h*poro*(1-sw))/boi


# The input parameters received with the Function input
# are encoded as strings, not as numbers.
# They needed to be converted to numbers for them
# to be usable in calculation of STOIIP.
# The conversion is done with Function float
poro = float(poro)
area = float(area)
h = float(h)
sw = float(sw)
boi = float(boi)


# Displaying the output
print('The amount of oil initially in place is ', N)

