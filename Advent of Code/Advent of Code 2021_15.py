import heapq # Use heapq to make the binary tree priority queue
from collections import defaultdict

#Going to use version of Dijkstra's/A* shortest path to find the minimum risk getting to the bottom right.
#Soln based on example from u/joshduncan, but tried to include a heuristic manhattan distance component
#to be more similar to A*.

def Solution(maze, squares):
    size_row, size_col = len(maze)*squares, len(maze[0])*squares
    risk_record = defaultdict(int) #defaultdict so we don't get any key errors
    priority_Q = [(0, 0, 0, 0)]
    heapq.heapify(priority_Q)
    visited = set() # Nodes we've already hit
    while len(priority_Q) > 0:
        h_risk, risk, row, col = heapq.heappop(priority_Q) #indicies will be heuristic, risk, row, col
        if (row, col) in visited: # Skip the node if we've already been there
            continue
        visited.add((row, col))
        risk_record[(row, col)] = risk  # record each node's risk in the record
        if row == size_row -1 and col == size_col - 1:
            break # break out once we are at the ending indicies

        # Check the neighbouring nodes and add them to the queue
        for N_row, N_col in [(-1,0), (0,-1), (0, 1), (1, 0)]:
            next_row = row + N_row
            next_col = col + N_col
            if not (0 <= next_row < size_row and 0 <= next_col < size_col):
                continue # skip if the index is beyond boundaries

            # Node risk is its value, plus the square multiple (boost for row and col on entering a deeper square), wrapped from 9 back
            r = next_row % (size_row//squares)
            c = next_col % (size_col//squares)
            boost_row = next_row // (size_row//squares)
            boost_col = next_col // (size_col//squares)
            neighbour_risk = (maze[r][c] + boost_row + boost_col - 1) % 9 + 1
            new_total_risk = risk + neighbour_risk
            #h_risk will just be the normal risk but incentivised to check nodes closer to the bottom right.
            h_risk = new_total_risk + size_row - next_row + size_col - next_col
            heapq.heappush(priority_Q, (h_risk, new_total_risk, next_row, next_col))
    return risk_record[(size_row - 1, size_col - 1)]

#Import the input
with open('2021 inputs/Day 15.txt') as f:
    f = f.read().splitlines()
maze = [[int(x) for x in a] for a in f]

print('Part 1 Solution: ' + str(Solution(maze, 1)))
print('Part 2 Solution: ' + str(Solution(maze, 5)))

