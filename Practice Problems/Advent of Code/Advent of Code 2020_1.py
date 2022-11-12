# Part 1:
import pandas as pd
# Can import as text file, but easy to work with DataFrames.
file = pd.read_csv('2020 inputs/Day 1.csv', header = None)
lines = list()
nums = file[0].values.tolist()
length = len(nums)
# Not the fastest means, but simply to just implement nested for loops
for x in range(length):
    for y in range(length):
        for z in range(length):
            sums = nums[x] + nums[y]
            if sums == 2020:
                ans = nums[x]*nums[y]
                break

print(ans)

# Part 2:
lines = list()
nums = file[0].values.tolist()
length = len(nums)

for x in range(length):
    for y in range(length):
        for z in range(length):
            sums = nums[x] + nums[y] + nums[z]
            if sums == 2020:
                ans = nums[x] * nums[y] * nums[z]
                break

print(ans)