#TTOWG

# A script to classify gridblocks in a discretized
# oil reservoir; based on the position of the gridblock
# relative to the reservoir boundaries.

# Receive inputs from user:
i = int(input('What is the column index of the gridblock?'))
j = int(input('What is the row index of the gridblock?'))
nx = int(input('How may columns are there in the discerized reservoir?'))
ny = int(input('How may rows are there in the discerized reservoir?'))

# Classify gridblock
if (i == 1 and j == 1) or (i == 1 and j == ny) or (i == nx and j == 1) or (i == nx and j == ny):
    block_cat = 'IV'
elif j==1 or j==ny:
    block_cat = 'II'
elif i==1 or i==nx:
    block_cat = 'III'
else:
    block_cat = 'I'
