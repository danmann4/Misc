#Part 1:
# Just going after the first letter in each command to distinguish.

with open('2021 inputs\Day 2.txt') as f:
    db = f.read().splitlines()

y = 0
z = 0
for a in db:
    if a[:1] == "f":
        y += int(a[-1])
    elif a[:1] == "u":
        z -= int(a[-1])
    elif a[:1] == "d":
        z += int(a[-1])
print('Final Depth x Distance multiple = ' + str(y*z))

#Part 2:
y = 0
z = 0
aim = 0
for a in db:
    if a[:1] == "f":
        y += int(a[-1])
        z += aim * int(a[-1])
    elif a[:1] == "u":
        aim -= int(a[-1])
    elif a[:1] == "d":
        aim += int(a[-1])
print('Final Depth x Distance multiple = ' + str(y*z))