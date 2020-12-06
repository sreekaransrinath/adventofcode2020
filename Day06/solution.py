inputFile = open("input.txt", 'r')
lines = inputFile.readlines()
inputStr = ""
for line in lines:
    inputStr += line

# Part 1

sum = 0
for answers in inputStr.split("\n\n"):
    union = list(set.union(*map(set, answers.split('\n'))))
    sum += len(union)
print(sum)


#Part 2

sum = 0
for answers in inputStr.split("\n\n"):
    intersection = list(set.intersection(*map(set, answers.split('\n'))))
    sum += len(intersection)
print(sum)