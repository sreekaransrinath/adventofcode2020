inputFile = open("input.txt", 'r')
lines = inputFile.readlines()

# Part 1

for i in range (len(lines)):
    for j in range (i, len(lines)):
        if int(lines[i]) + int(lines[j]) == 2020:
            print (int(lines[i]) * int(lines[j]))

# Part 2

for i in range (len(lines)):
    for j in range (i, len(lines)):
        for k in range(j, len(lines)):
            if int(lines[i]) + int(lines[j]) + int(lines[k]) == 2020:
                print(int(lines[i]) * int(lines[j]) * int(lines[k]))