inputFile = open("input.txt", 'r')
lines = inputFile.readlines()

# Part 1

treeCount = i = 0
for line in lines:
    line = line.strip()
    if line[i % len(line)] == '#':
        treeCount += 1
    i += 3
print(treeCount)

# Part 2

shiftList = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
prod = 1
for shiftSet in shiftList:
    treeCount = i = j = 0
    while j < len(lines):
        lines[j] = lines[j].strip()
        if lines[j][i % len(lines[j])] == '#':
            treeCount += 1
        i += shiftSet[0]
        j += shiftSet[1]
    prod *= treeCount
print(prod)