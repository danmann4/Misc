with open('2020 inputs/Day 6.txt') as f:
    db = f.read().split('\n\n')
# Part 1:
# Use sets which can't have duplicates
questions = 0
for group in db:
    questions += len(set(group.replace('\n','')))
print('The sum of all group questions is ' + str(questions))

#Part 2:
answers = 0
for group in db:
    lines = group.splitlines()
    start = set(lines[0])
    # Easiest to go after updating the set
    for a in lines:
        start &= set(a)
    answers += len(start)
print('The answer is: ' + str(answers))