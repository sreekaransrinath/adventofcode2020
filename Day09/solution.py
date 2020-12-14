input = [int(line.strip()) for line in open('Day09/input.txt', 'r').readlines()]

def isSumOf(arr, num):
    for i in arr:
        for j in arr[arr.index(i):]:
            if num == i + j:
                return True
    return False

def oddManOut(input):
    for i in range(25, len(input)):
        if not isSumOf(input[i - 25: i], input[i]):
            return input[i]

def findContiguousList(arr):
    num = oddManOut(arr)
    for i in range(len(arr)):
        sum = arr[i]
        for j in range(i + 1, len(arr)):
            sum += arr[j]
            if sum == num:
                return min(arr[i:j]) + max(arr[i:j])

print(findContiguousList(input))