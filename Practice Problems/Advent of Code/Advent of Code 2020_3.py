# Part 2: (Part 1 is basically a part of this solution)
import numpy as np #Use numpy array's, cleaner to use for matrix

with open('2020 inputs/Day 3.txt') as f:
    db = f.read()

# Clean up the list to transfer into np.array, then reshape into proper dimensions.
# Don't absolutely need numpy, but its convenient for reshape.
db = db.replace('\n','')
db = db.replace('#','1')
db = db.replace('.','0')
# Use '.' = 0, and '#' = 1 with the aim of summing the chosen slope indices
db = list(map(int, db))
lines = np.array(db)
lines = np.reshape(lines,(-1,31))
input = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]] # Slope inputs
mat_size = list(lines.shape)
Trees = 1
for i in range(len(input)): # iterate through the inputs
    # Based on the slope, get the indices of the path matrix we require to check.
    Tobogan_row = np.arange(input[i][0], (mat_size[0]), input[i][0]) # Row indices we need
    Tobogan_col = np.arange(((input[i][1])), round(((mat_size[0])*(input[i][1]))/(input[i][0])), input[i][1]) # Column indices we need
    Tobogan_path = np.concatenate((Tobogan_row.reshape(-1, 1), Tobogan_col.reshape(-1, 1)), axis=1)
    # Sum the matrix elements at the specified indices. This number is all the trees we run into.
    Tobogan_Trees = sum(lines[x, y % mat_size[1]] for x, y in Tobogan_path)
    Trees *= Tobogan_Trees # Multiple various slopes to get final answer 'Trees'
print(Trees)



