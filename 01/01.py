f = open('input.txt', 'r')
inputData = f.read()
f.close()
inputLen = len(inputData)

# 01
i = 1
savedValues = []
for char in inputData:
    if (i == inputLen):
        if (char == inputData[0]):
            savedValues.append(int(char))
    else:
        if (char == inputData[i]):
            savedValues.append(int(char))
    i += 1

print 'Total for part 1:', sum(savedValues)


# 02
def halfway(current, total):
    half = total / 2
    if (current > half-1):
        return current - half
    else:
        return current + half

newSave = []
x = 0
for char in inputData:
    hw = halfway(x, inputLen)
    if (char == inputData[hw]):
        newSave.append(int(char))
    x += 1

print 'Total for part 2:', sum(newSave)
