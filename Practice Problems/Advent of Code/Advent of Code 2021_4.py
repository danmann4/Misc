import numpy as np
# Part 2: (Part 1 is just the first call of "winner")

def alt_mask(board, mask, call):
    # This function alters the mask(ones) matrix when the 'call' is in it with a 0.
    rowlen = collen = 5
    for r in range(rowlen):
        for c in range(collen):
            if board[r, c] == call:
                mask[r, c] = 0
            else:
                continue
    return mask

def sum_mask(mask):
    # This function just checks each row and col to see if they were called.
    row_sum = np.sum(mask, axis=1)
    col_sum = np.sum(mask, axis=0)
    if any(x == 0 for x in row_sum):
        return True
    elif any(x == 0 for x in col_sum):
        return True
    else:
        return False

with open('2021 inputs/Day 4.txt') as f:
    db = f.read().split('\n\n')
# Clean up the text file, took longer than I would like to admit.
calls = [int(a) for a in db[0].split(',')]
lines = [x.replace('\n',' ') for x in db[1:]]
lines = [y.lstrip() for y in lines]
lines = [y.replace('  ',' ') for y in lines]
line = [a.split(' ') for a in lines]
boards = [[int(a) for a in row] for row in line]
# Use numpy to get into matrix form.
boardsnp = [np.array(x).reshape((5, -5)) for x in boards]
mask = np.ones(np.shape(boardsnp))

sum_check = bool()
last_board = list()
for call in calls:
    # For each bingo number called, check each board index and change the masked matrix if its present.
    # Check the row and column sums. If a board wins just multiply the original matrix board by the altered mask.
    for i in range(len(boardsnp)):
        mask[i] = alt_mask(boardsnp[i], mask[i], call)
        sum_check = sum_mask(mask[i])
        if sum_check:
            # We only want to enter this loop if the board has never won before.
            if not any(x == i for x in last_board):
                last_board.append(i)
                winner = int(np.sum(boardsnp[i] * mask[i]) * call)
            sum_check = False
print("The last winning board value is: " + str(winner))