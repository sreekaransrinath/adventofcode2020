inputFile = open("input.txt", 'r')
lines = inputFile.readlines()
seatID = []

# Part 1

for line in lines:
    vLo = 0
    vHi = 127
    hLo = 0
    hHi = 7
    for letter in line.strip():
        if letter == 'F':
            vHi = (vHi + vLo + 1) / 2 - 1
        elif letter == 'B':
            vLo = (vHi + vLo + 1) / 2
        elif letter == 'L':
            hHi = (hHi + hLo + 1) / 2 - 1
        else:
            hLo = (hHi + hLo + 1) / 2
    seatID.append(vHi * 8 + hHi)
print(max(seatID))

# Part 2

seatID.sort()
seatID = list(set(range(1024)) - set(seatID))
for i in range(1, len(seatID) - 1):
    if (seatID[i + 1] != seatID[i] + 1) and (seatID[i - 1] != seatID[i] - 1):
        print(seatID[i])
    