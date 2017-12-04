f = open('input.txt', 'r')
inputData = f.read()
f.close()


lines = inputData.split("\n")
valid = 0
for line in lines:
    words = {}
    lineWords = line.split()
    invalid = False
    for word in lineWords:
        try:
            print words[word]
            invalid = True
        except:
            words[word] = None

    if (invalid is False):
        valid += 1

print valid
