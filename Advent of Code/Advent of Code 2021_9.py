from collections import deque


def low_points(ground):
    #1. deal with corner cases
    #2. deal with edge cases
    #3. deal with internal points
    # Iterate through each index, deal set up if statements for edge cases
    max_col = len(ground[0]) - 1
    max_row = len(ground) - 1
    heights = 0
    lows = []
    for row in range(max_row + 1):
        for col in range(max_col + 1):
            curr = ground[row][col]

            # Check edges and corners
            if not row and not col:
                # top left
                neighbours = [ground[row][col+1], ground[row+1][col]]
            elif not row and col == max_col:
                # top right
                neighbours = [ground[row][col-1], ground[row+1][col]]
            elif row == max_row and not col:
                # bot left
                neighbours = [ground[row-1][col], ground[row][col+1]]
            elif row == max_row and col == max_col:
                # bot right
                neighbours = [ground[row][col-1], ground[row-1][col]]
            elif not row:
                # top edge
                neighbours = [ground[row][col-1], ground[row][col+1], ground[row+1][col]]
            elif row == max_row:
                # bottom edge
                neighbours = [ground[row][col-1], ground[row-1][col], ground[row][col+1]]
            elif not col:
                # left edge
                neighbours = [ground[row-1][col], ground[row][col+1], ground[row+1][col]]
            elif col == max_col:
                # right edge
                neighbours = [ground[row][col-1], ground[row-1][col], ground[row+1][col]]
            else:
                # neighbours: left, up, right, down
                neighbours = [ground[row][col-1], ground[row-1][col], ground[row][col+1], ground[row+1][col]]
            # Check if all neighbhours are larger
            if all([x > curr for x in neighbours]):
                heights += (1 + curr)
                lows.append((row, col))
    return heights, lows

# Just do a BFS through each low point determined in the first part
def basins(lows, graph):
    queue = deque()
    basin = []
    basin_count = 0
    visited = set()
    for low in lows:
        queue.append(low)
        while queue:
            # Loop through the queue, add neighbours if applicable
            row, col = queue.pop()
            if (row, col) in visited or graph[row][col] == 9:
                continue
            else:
                visited.add((row, col))
                basin_count += 1
            curr = graph[row][col]

            #neighbhours: left, up, right, down
            left, up, right, down = (row, col-1), (row-1, col), (row, col+1), (row+1, col)
            if col-1 > -1 and left not in visited:
                queue.appendleft(left)
            if row-1 > -1 and up not in visited:
                queue.appendleft(up)
            # Avoid index errors with try statements
            try:
                test = graph[right[0]][right[1]]
                if (right[0], right[1]) not in visited:
                    queue.appendleft(right)
            except IndexError:
                pass
            try:
                test = graph[down[0]][down[1]]
                if (down[0], down[1]) not in visited:
                    queue.appendleft(down)
            except IndexError:
                pass
        basin.append(basin_count)
        basin_count = 0
    basin.sort(reverse=True)

    ans = basin[0]
    for i in range(1, 3):
        ans *= basin[i]

    return ans


with open('2021 inputs\Day 9.txt') as f:
    data = [[int(points) for points in lines] for lines in f.read().splitlines()]


part_1, lows = low_points(data)
print(f'Part #1: {part_1}')
print(f'Part #2: {basins(lows, data)}')

