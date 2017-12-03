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
    return True if (number % dividedBy) == 0 else False


def Two():
    print isDivisible(number=9, dividedBy=2)

    lines = inputData.split("\n")
    for line in lines:
        lineWords = line.split('\t')


One()
Two()
