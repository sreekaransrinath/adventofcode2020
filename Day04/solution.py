import re
inputFile = open("input.txt", 'r')
lines = inputFile.readlines()
inputString = ""
for line in lines:
    inputString += line
entries = inputString.split('\n\n')

# Part 1

validCount = 0
for entry in entries:
    fD = {}
    for field in entry.split():
        fD[field[:3]] = field[4:]
    if all(item in fD.keys() for item in ['byr', 'iyr', 'eyr', 'pid', 'hgt', 'ecl', 'hcl']):
        validCount += 1

print(validCount)

# Part 2

validCount = 0
for entry in entries:
    fD = {}
    for field in entry.split():
        fD[field[:3]] = field[4:]
    if all(item in fD.keys() for item in ['byr', 'iyr', 'eyr', 'pid', 'hgt', 'ecl', 'hcl']):
        if(int(fD['byr']) in range(1920, 2003) and fD['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and re.fullmatch('^#[0-9a-f]{6}$', fD['hcl']) != None and re.fullmatch('^[0-9]{9}$', fD['pid']) != None and int(fD['iyr']) in range(2010, 2021) and int(fD['eyr']) in range(2020, 2031)):
            if((fD['hgt'][-2:] == 'in' and int(fD['hgt'][:-2]) in range(59, 77)) or (fD['hgt'][-2:] == 'cm' and int(fD['hgt'][:-2]) in range(150, 194))):
                validCount += 1
print(validCount)