# Part 1:
# For this part I found it easiest to go after the current direction 'facing1' function first.
# Then just move your specified distance.
import math
directions = ['N', 'E', 'S', 'W']
# This function just uses the 'directions' list to loop through based on the rotation multiple of 90 deg.
def facing1(input, cur_dir):
    if input[0] == 'L':
        new_dir = directions[(int(directions.index(cur_dir) - int(input[1:])/90))%4]
    else:
        new_dir = directions[(int(directions.index(cur_dir) + int(input[1:])/90))%4]
    return new_dir

with open('2020 inputs/Day 12.txt') as f:
    db = f.read().split()

x = int()
y = int()
cur_dir = 'E'
for i in db:
    if i[0] == 'L' or i[0] == 'R':
        cur_dir = facing1(i, cur_dir)
        continue
    # We wanted to get the current direction first incase the previous command changed direction
    if i[0] == 'F':
       i = cur_dir + i[1:]

    if i[0] == 'N':
        y += int(i[1:])
    elif i[0] == 'S':
        y -= int(i[1:])
    elif i[0] == 'E':
        x += int(i[1:])
    elif i[0] == 'W':
        x -= int(i[1:])
print('The total distance is: ' + str(abs(x) + abs(y)))

# Part 2:
# So similar to part #1, but this time we use a list for [x, y].
# 'facing2' is just a rotation matrix for whatever the angle input was.
# Would be simpler to just implement multiples of -1 and 1 since sin and cos will always just flip
# the values in this case. However, easy to use a rotation matrix even if there was angle inputs that
# were not integer multiples of 90 deg.
def facing2(input, way_point):
    new_point = [0, 0]
    ang = math.radians(int(input[1:]))
    # Based on the rotation direction (clockwise = negative rotation) flip new_point values.
    if input[0] == 'R':
        new_point[0] = round(math.cos(-1*ang) * way_point[0] - math.sin(-1*ang) * way_point[1])
        new_point[1] = round(math.sin(-1*ang) * way_point[0] + math.cos(-1*ang) * way_point[1])
    else:
        new_point[0] = round(math.cos(ang) * way_point[0] - math.sin(ang) * way_point[1])
        new_point[1] = round(math.sin(ang) * way_point[0] + math.cos(ang) * way_point[1])
    return new_point

way_point = [10, 1]
boat = [0, 0]

for i in db:
    # Again, check you facing direction first.
    if i[0] == 'L' or i[0] == 'R':
        way_point = facing2(i, way_point)
        continue
    elif i[0] == 'F':
        boat[0] += way_point[0] * int(i[1:])
        boat[1] += way_point[1] * int(i[1:])
    elif i[0] == 'N':
        way_point[1] += int(i[1:])
    elif i[0] == 'S':
        way_point[1] -= int(i[1:])
    elif i[0] == 'E':
        way_point[0] += int(i[1:])
    elif i[0] == 'W':
        way_point[0] -= int(i[1:])

distance = abs(boat[0]) + abs(boat[1])
print('The total distance is: ' + str(distance))
