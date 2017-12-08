f = open('input.txt', 'r')
inputData = f.read()
f.close()
#inputData = '0\n3\n0\n1\n-3'


def one():
    lines = inputData.split("\n")

    i = 0
    steps = 0
    end = len(lines) - 1
    while i <= end:
        v = int(lines[i])
        lines[i] = v + 1
        i += v
        steps += 1

    print steps


def two():
    lines = inputData.split("\n")

    i = 0
    steps = 0
    end = len(lines) - 1
    while i <= end:
        v = int(lines[i])
        lines[i] = v + (-1 if v >= 3 else 1)
        i += v
        steps += 1

    print steps

one()
two()
