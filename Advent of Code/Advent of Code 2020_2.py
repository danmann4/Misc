with open('2020 inputs/Day 2.txt') as f:
    lines = f.readlines()
# Part 1:
count = int()
# Likely more efficient to use something like RegEx, but here is a quick and dirty solution without using libraries.
for i in range(len(lines)):
    # These variables all just find the specific characters we are after based on index.
    colon = lines[i].find(':')
    char = lines[i][colon - 1]
    numstart = 0
    numend = colon - 2
    dash = lines[i].find('-')
    maxchar = int(lines[i][(dash + 1):numend])
    minchar = int(lines[i][numstart:dash])
    if minchar <= lines[i].count(char)-1 <= maxchar:
        count += 1

print('count: ' + str(count))

#Part 2:
count = int()

for i in range(len(lines)):
    colon = lines[i].find(':')
    char = lines[i][colon - 1]
    numstart = 0
    numend = colon - 2
    dash = lines[i].find('-')
    maxchar = int(lines[i][(dash + 1):numend])
    minchar = int(lines[i][numstart:dash])
    if lines[i][(colon + 1 + minchar)] == char or lines[i][(colon + 1 + maxchar)] == char:
        count += 1
    if lines[i][(colon + 1 + minchar)] == char and lines[i][(colon + 1 + maxchar)] == char:
        count -= 1
print('count: ' + str(count))
