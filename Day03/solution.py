inputFile = open("input.txt", 'r')
lines = inputFile.readlines()
treeCount = i = 0

for line in lines:
    line = line.strip()

for line in lines:
    if line[i % len(line)] == '#':
        treeCount += 1
    i += 3

print(treeCount)