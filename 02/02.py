f = open('input.txt', 'r')
inputData = f.read()
f.close()


def One():
    checksumNums = []

    lines = inputData.split("\n")
    for line in lines:
        minValue = None
        maxValue = None
        difference = None

        lineWords = line.split('\t')
        for num in lineWords:
            minValue = int(num) if (int(num) < minValue) or minValue is None else minValue
            maxValue = int(num) if (int(num) > maxValue) or maxValue is None else maxValue

        difference = maxValue - minValue
        checksumNums.append(difference)

    print 'Answer 1: {sum}'.format(sum=sum(checksumNums))


# 02
def isDivisible(number, dividedBy):
    return True if (int(number) % int(dividedBy)) == 0 else False


def isDivisibleBy(number, dictNumbers):
    for dictNumber in dictNumbers:
        if (int(number) != int(dictNumber)):
            if (isDivisible(number, dictNumber)):
                return (int(number) / int(dictNumber))
    return None


def Two():
    checksumNums2 = []

    lines = inputData.split("\n")
    for line in lines:
        lineWords = line.split('\t')
        for num in lineWords:
            toAppend = isDivisibleBy(num, lineWords)
            if (toAppend is not None):
                checksumNums2.append(int(toAppend))
                print 'continue from ', num, toAppend
                continue

    print 'Answer 2: {sum}'.format(sum=sum(checksumNums2))

One()
Two()
