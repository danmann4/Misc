import re
with open('2020 inputs/Day 4.txt') as f:
    db = f.read()
db = db.split('\n\n')
Passports = [x.replace('\n',' ') for x in db]
# Part 1:
# This is a quick and dirty way based on the total count of colons in the string.
# We should be more generally going after a list comprehension, or a generator function, which has an 'any()' or 'all()'
# condition to check valid prefixes.
valid = 0
for i in range(len(Passports)):
    fields = Passports[i].count(':')
    if fields == 8:
        valid += 1
    if fields == 7 and (Passports[i].count('cid:')) == 0:
        valid += 1
print(valid)

# Part 2:
# Easiest to use regular expressions. Copied these if statements from u/Jerslev's solution.
Passports = [x.replace('\n',' ') for x in db]
valid = 0
for passport in Passports:
    if (re.search(r"byr:19[2-9]\d|byr:200[0-2]", passport) and
            re.search(r"eyr:202\d|eyr:2030", passport) and
            re.search(r"iyr:201\d|iyr:2020", passport) and
            re.search(r"hgt:1[5-8]\dcm|hgt:19[0-3]cm|hgt:59in|hgt:6\din|hgt:7[0-6]in", passport) and
            re.search(r"hcl:#[a-z0-9]{6}", passport) and
            re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", passport) and
            re.search(r"pid:\d{9}\b", passport)):
        valid += 1

print(valid)