f = open('example.txt', 'r')
inputData = f.read()
f.close()


class Node():
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.parent = None

    def addChild(self, child):
        child.setParent = self
        self.children.append(child)

    def setParent(self, parent):
        self.parent = parent


lines = inputData.split('\n')

blocks = {}
for line in lines:
    parts = line.split(',')
    name = parts[0]
    final = ''.join(parts).split(' ')
    if len(final) < 3:
        continue
    print final



print blocks
