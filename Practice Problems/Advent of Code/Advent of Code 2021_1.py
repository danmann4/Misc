#Part 1:
with open('2021 inputs/Day 1.txt') as f:
    db = f.read().splitlines()
sonar = list(map(int, db))
count = 0
# Just convert string to int, then check if the current list value is larger than the
# previous index.
for i in range(1, len(sonar)):
    if sonar[i] > sonar[i-1]:
        count += 1
print('The depth measurement increases ' + str(count) +' times')

#Part 2:
# Same thing for part #2, just change up index values searched.
counter = 0
length = len(sonar)
for i in range(1, length - 1):
    if sum(sonar[i:i+3]) > sum(sonar[i-1:i+2]):
        counter += 1
print('The depth measurement window increases ' + str(counter) +' times')