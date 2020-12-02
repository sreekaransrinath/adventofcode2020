inputFile = open("input.txt", 'r')
lines = inputFile.readlines()
passCount = len(lines)

for line in lines:
    dashIndex = line.index('-')
    space1Index = line.index(" ")
    colonIndex = line.index(':')
    lowerLimit = line[:dashIndex]
    upperLimit = line[dashIndex + 1: space1Index]
    key = line[space1Index + 1]
    password = line[colonIndex + 2:]
    count = 0
    for letter in password:
        if letter == key:
            count += 1
    if count < int(lowerLimit) or count > int(upperLimit):
        passCount -= 1

print(passCount)
