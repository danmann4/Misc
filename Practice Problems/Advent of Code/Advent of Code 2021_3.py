# Part 1:
with open('2021 inputs/Day 3.txt') as f:
    db = f.read().split('\n\n')
bits = [x.replace('\n', '') for x in db]

col = list()
gamma = str()
epsilon = list()
# For a list of every n bits, count the max number.
for n in range(12):
    col = bits[0][n::12]
    gamma += (max(col, key=col.count))
# Flip the bits for epsilon.
epsilon = ''.join('0' if x == '1' else '1' for x in gamma)

print("The power consumption is: " + str(int(gamma, 2) * int(epsilon, 2)))

# Part 2:
# This one is not clean since we have two separate for loops dealing with oxy and CO2 separately. Ideally we combine
# the search in one loop, but quick to copy paste for this scenario.
bitslist = db[0].split('\n')
oxy = str()
CO2 = str()
colcount = list()
maxcount = str()
mincount = str()
bitlistpop = list()
for n in range(12):
    colcount = [a[n] for a in bitslist]
    # Make sure first the count(1) == count(0), otherwise we go for the max of the two.
    if colcount.count('0') == colcount.count('1'):
        maxcount = '1'
    else:
        maxcount = (max(colcount, key=colcount.count))
    for y in range(len(bitslist)):
        # Making a second reverse sorted list each loop to know which indexes we need to remove.
        # Must reverse sort so the index values don't change as we pop.
        if bitslist[y][n] != maxcount:
            bitlistpop.append(y)
    for index in sorted(bitlistpop, reverse=True):
        del bitslist[index]
    bitlistpop = []
    oxy += maxcount
bitslist = db[0].split('\n')
colcount = []

# Same for C02, again not the most efficient format but its easy.

for n in range(12):
    colcount = [a[n] for a in bitslist]
    if colcount.count('0') == colcount.count('1'):
        mincount = '0'
    else:
        mincount = (min(colcount, key=colcount.count))
    for y in range(len(bitslist)):
        if bitslist[y][n] != mincount:
            bitlistpop.append(y)
    for index in sorted(bitlistpop, reverse=True):
        del bitslist[index]
    bitlistpop = []
    CO2 += mincount
print('The life support rating is: ' + str(int(oxy,2) * int(CO2,2)))
