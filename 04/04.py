f = open('input.txt', 'r')
inputData = f.read()
f.close()


def one():
    lines = inputData.split("\n")
    valid = 0
    for line in lines:
        words = {}
        lineWords = line.split()
        invalid = False
        for word in lineWords:
            try:
                x = words[word]
                invalid = True
            except:
                words[word] = None

        if (invalid is False):
            valid += 1

    print valid


def two():
    lines = inputData.split("\n")
    valid = 0
    for line in lines:
        words = {}
        lineWords = line.split()
        invalid = False
        for word in lineWords:
            sWord = ''.join(sorted(word))
            try:
                x = words[sWord]
                invalid = True
            except:
                words[sWord] = None

        if (invalid is False):
            valid += 1

    print valid

one()
two()
