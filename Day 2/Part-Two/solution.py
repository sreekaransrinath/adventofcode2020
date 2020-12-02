inputFile = open("input.txt", 'r')
lines = inputFile.readlines()
passCount = 0

for line in lines:
    dashIndex = line.index('-')
    space1Index = line.index(" ")
    colonIndex = line.index(':')
    index1 = int(line[:dashIndex])
    index2 = int(line[dashIndex + 1: space1Index])
    key = line[space1Index + 1]
    password = line[colonIndex + 2:]
    count = 0
    if (password[index1 - 1] == key or password[index2 - 1] == key) and not (password[index1 - 1] == key and password[index2 - 1] == key):
        passCount += 1

print(passCount)